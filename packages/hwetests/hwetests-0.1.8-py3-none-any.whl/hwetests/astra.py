import numpy as np
import math
import pandas as pd
import scipy.stats as stats
import csv
from matplotlib import pyplot as plt
import seaborn as sns


# need to calculate only on the upper triangle because the matrices are symmetric
def calculate_chi_squared_value(population_amount_, alleles_probabilities_, observed_probability_correction_dict_, cutoff):
    value = 0.0
    amount_of_small_expected_ = 0
    for key, value_list in observed_probability_correction_dict_.items():
        i_str, j_str = key.split('_')
        i = int(i_str)
        j = int(j_str)
        i, j = min(i, j), max(i, j)

        mult = 1
        if i != j:
            mult = 2
        expected = mult * population_amount_ * alleles_probabilities_[i] * alleles_probabilities_[j]
        observed = population_amount_ * observed_probability_correction_dict_[key][0]
        correction = observed_probability_correction_dict_[key][1]
        variance = expected

        if expected * correction < cutoff:
            amount_of_small_expected_ += 1
            continue
        value += (1 / correction) * (((expected - observed) ** 2) / variance)
    return value, amount_of_small_expected_


def run_experiment(alleles_count, population_amount, alleles_probabilities,
                   observed_probability_correction_dict, index_to_allele_, should_save_csv_, cutoff_value_):

    chi_squared_stat, amount_of_small_expected = calculate_chi_squared_value(population_amount_=population_amount,
                                                                             alleles_probabilities_=alleles_probabilities,
                                                                             observed_probability_correction_dict_=observed_probability_correction_dict,
                                                                             cutoff=cutoff_value_)
    couples_amount = (alleles_count * (alleles_count + 1)) / 2 - 1
    dof = couples_amount - amount_of_small_expected

    # print(f' alpha for choice: {alpha_val}')
    # print(f' chi square value: {chi_squared_stat}')

    # crit = stats.chi2.ppf(q=0.95, df=dof)
    # print(f'Critical value: {crit}')

    p_value = 1 - stats.chi2.cdf(x=chi_squared_stat,
                                 df=dof)

    if should_save_csv_:
        if isinstance(should_save_csv_, str):
            file_name = should_save_csv_ + '.csv'
        else:
            file_name = 'alleles_data.csv'
        columns = ['first_allele', 'second_allele', 'observed', 'expected', 'variance']
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(columns)
            for key, value_list in observed_probability_correction_dict.items():
                i_str, j_str = key.split('_')
                i = int(i_str)
                j = int(j_str)
                i, j = min(i, j), max(i, j)

                first_allele = index_to_allele_[i]
                second_allele = index_to_allele_[j]

                mult = 1
                if i != j:
                    mult = 2
                expected = mult * population_amount * alleles_probabilities[i] * alleles_probabilities[j]
                observed = population_amount * observed_probability_correction_dict[key][0]
                correction = observed_probability_correction_dict[key][1]
                writer.writerow([first_allele, second_allele, observed, expected, expected * correction])

    return p_value, chi_squared_stat, dof


def full_algorithm(file_path, cutoff_value=0.0, should_save_csv=False, should_save_plot=False):
    """
    ASTRA Algorithm.

    Performs a modified Chi-Squared statistical test on ambiguous observations.
    :param file_path: A path to a csv file with columns: 1) index or id of a donor (integer or string).
    2) first allele (integer or string). 3) second allele (integer or string). 4) probability (float).
    :param cutoff_value: (optional, default value is 0.0) A float value that decides to not account (O-E)^2 / E in the summation
    of the Chi-Squared statistic if E < cutoff.
    :param should_save_csv: (optional, default value is False) Either boolean or string, if it's True then a csv with the columns:
     [first allele, second allele, observed, expected, variance] is saved (named 'alleles_data.csv')
    and if it's a string then a csv with the given string name is saved.
    :param should_save_plot: (optional, default value is False) Either boolean or string, if it's True then
    a png containing 2 bar plots is saved: for each allele showing its chi squared statistic over degrees of freedom
    (summing over the observations only associated with this allele) and -log_10(p_value).
    If it's a string then a csv with the given string name is saved.
    :return: p-value (float), Chi-Squared statistic (float), degrees of freedom (integer). also saves a csv.
    with columns: first allele, second allele, observed, variance:
    """
    id_to_index = {}
    allele_to_index = {}
    index_to_allele = {}
    # index1_index2 -> [obs_prob, corr]
    i_j_to_observed_probability_correction = {}

    # first read all the rows and get indices of ids and alleles and amounts
    with open(file_path, encoding="utf8") as infile:
        for index, line in enumerate(infile):
            # header
            if index == 0:
                continue
            lst = line.strip('\n').split(',')

            id = lst[0]
            allele_1 = lst[1]
            allele_2 = lst[2]
            # allele_1, allele_2 = min(allele_1, allele_2), max(allele_1, allele_2)
            # probability = float(lst[3])

            if id not in id_to_index:
                id_to_index[id] = len(id_to_index)

            if allele_1 not in allele_to_index:
                # updating the inverse dictionary
                index_to_allele[len(allele_to_index)] = allele_1
                # updating the dictionary
                allele_to_index[allele_1] = len(allele_to_index)
            if allele_2 not in allele_to_index:
                # updating the inverse dictionary
                index_to_allele[len(allele_to_index)] = allele_2
                # updating the dictionary
                allele_to_index[allele_2] = len(allele_to_index)

    alleles_count = len(allele_to_index)
    population_amount = len(id_to_index)

    # {p(i)}
    alleles_probabilities = np.zeros(alleles_count)

    # # {p(i, j)}
    # observed_probabilities = np.zeros(shape=(alleles_count, alleles_count))
    #
    # # correction matrix
    # correction = np.zeros(shape=(alleles_count, alleles_count))

    # calculate {p_k(i,j)}
    with open(file_path, encoding="utf8") as infile:
        for index, line in enumerate(infile):
            if index == 0:
                continue
            lst = line.strip('\n').split(',')

            # id = lst[0]
            allele_1 = lst[1]
            allele_2 = lst[2]
            # allele_1, allele_2 = min(allele_1, allele_2), max(allele_1, allele_2)
            probability = float(lst[3])

            # id_index = id_to_index[id]

            allele_1_index = allele_to_index[allele_1]
            allele_2_index = allele_to_index[allele_2]

            allele_1_index, allele_2_index = min(allele_1_index, allele_2_index), max(allele_1_index, allele_2_index)

            i_j = str(allele_1_index) + '_' + str(allele_2_index)
            if i_j not in i_j:
                i_j_to_observed_probability_correction[i_j] = [0.0, 0.0]

            alleles_probabilities[allele_1_index] += 0.5 * probability
            alleles_probabilities[allele_2_index] += 0.5 * probability

            # observed_probabilities[allele_1_index, allele_2_index] += probability
            # add observed probability
            i_j_to_observed_probability_correction[i_j][0] += probability

            # correction[allele_1_index, allele_2_index] += (probability ** 2)
            i_j_to_observed_probability_correction[i_j][1] += (probability ** 2)

    # p(i) = sum_k_j p_k(i,j) / N
    alleles_probabilities /= population_amount

    for key, list_value in i_j_to_observed_probability_correction.items():
        # normalize observed probability
        i_j_to_observed_probability_correction[key][0] /= population_amount

        observed_probability = i_j_to_observed_probability_correction[key][0]

        # normalize correction
        if observed_probability == 0:
            i_j_to_observed_probability_correction[key][1] = 1.0
        else:
            i_j_to_observed_probability_correction[key][1] /= population_amount * observed_probability


    # for i in range(alleles_count):
    #     for j in range(alleles_count):
    #         observed_probabilities[i, j] /= population_amount
    #         if observed_probabilities[i, j] == 0:
    #             correction[i, j] = 1.0
    #         else:
    #             correction[i, j] /= (population_amount * observed_probabilities[i, j])

    p_value, chi_squared, dof = run_experiment(alleles_count=alleles_count,
                                               population_amount=population_amount,
                                               alleles_probabilities=alleles_probabilities,
                                               observed_probability_correction_dict=i_j_to_observed_probability_correction,
                                               index_to_allele_=index_to_allele,
                                               should_save_csv_=should_save_csv,
                                               cutoff_value_=cutoff_value)

    if should_save_plot:
        # save a bar plot showing for each allele its deviation from HWE
        couples_amount = int((alleles_count * (alleles_count + 1)) / 2 - 1)
        df = pd.DataFrame(index=range(couples_amount), columns=['Alleles', 'Normalized statistic', '-log_10(p_value)'])
        logs_list = []
        for i in range(alleles_count):
            # for allele i: calculate Statistic and p_value
            statistic = 0.0
            amount_of_small_expected = 0
            for j in range(alleles_count):
                t, m = min(i, j), max(i, j)
                t_m = str(t) + '_' + str(m)
                mult = 1
                if t != m:
                    mult = 2
                expected = mult * population_amount * alleles_probabilities[t] * alleles_probabilities[m]
                # if expected < cutoff_value:
                #     amount_of_small_expected += 1
                #     continue
                observed = population_amount * i_j_to_observed_probability_correction[t_m][0]
                correction = i_j_to_observed_probability_correction[t_m][1]
                statistic += (1 / correction) * (((expected - observed) ** 2) / expected)
            # calculate degrees of freedom
            dof = (alleles_count - 1)
            # calculate p_value
            p_value = 1 - stats.chi2.cdf(x=statistic,
                                         df=dof)
            if p_value == 0.0:
                logs_list.append('infty')
            else:
                logs_list.append(-math.log(p_value, 10))
            allele = index_to_allele[i]
            df.iloc[i] = [allele, statistic / dof, 0]

        # sort dataframe according to p_values and take the smallest 20 statistics.
        df = df.sort_values('Normalized statistic').head(min(alleles_count, 20))
        # we need to update the log p-values (some may be infinite, so we set them to the max value from the 20)
        logs_list_ints = [logs_list[i] for i in df.index if isinstance(logs_list[i], (int, float))]
        max_log = max(logs_list_ints)
        for i in df.index:
            if logs_list[i] == 'infty':
                logs_list[i] = max_log
            df.iloc[0, 2] = logs_list[i]
        # plot the dataframe into 2 bar plots
        fig, axes = plt.subplots(1, 2)
        plt.subplot(1, 2, 1)
        sns.set_color_codes('pastel')
        sns.barplot(x='-log_10(p_value)', y='Alleles', data=df,
                    label='Total', color='royalblue', edgecolor='w')
        sns.set_color_codes('muted')
        # invert the order of x-axis values
        ax = plt.gca()
        ax.set_xlim(ax.get_xlim()[::-1])
        # ax.yaxis.set_label_position("right")
        ax.yaxis.tick_right()
        plt.ylabel('')

        # move ticks to the right

        plt.subplot(1, 2, 2)
        sns.barplot(x='Normalized statistic', y='Alleles', data=df,
                    color='slategrey', edgecolor='w')
        # plt.legend(ncol=2, loc='lower right')
        sns.despine(left=True, bottom=True)
        fig.tight_layout()

        if isinstance(should_save_plot, str):
            file_name = should_save_plot + '.png'
        else:
            file_name = 'alleles_barplot.png'
        plt.savefig(file_name, pad_inches=0.2, bbox_inches="tight")

    return p_value, chi_squared, dof
