"""
Template for the COMP1730/6730 project assignment, S1 2022.
The assignment specification is available on the course web
site, at https://cs.anu.edu.au/courses/comp1730/assessment/project/

Collaborators: <list the UIDs of ALL members of your project group here>
u7211790
u7167784
"""
import csv
import datetime


def analyse(path_to_file):
    """
    This function is used to print out the results of the analysis of COVID-19 vaccinations

    :param path_to_file: the complete path to the data file (CSV file) that it should read and analyse
    """
    print("Analysing data file", path_to_file)
    with open(path_to_file) as csvfile:
        reader = csv.reader(csvfile)
        table = [row for row in reader]
    # get the table without header
    table_without_header = [table[i] for i in range(1, len(table))]
    # Question 1
    print("\nQuestion 1:")
    unique_locations = count_unique_locations(table_without_header)
    print("Number of unique locations:", len(unique_locations))
    unique_countries = count_unique_countries(table_without_header)
    print("Number of unique countries:", len(unique_countries))
    global_total_vaccination = global_vaccine_statistics(table_without_header, unique_countries, 3)
    print("Global vaccine doses:", global_total_vaccination)
    global_people_vaccinated = global_vaccine_statistics(table_without_header, unique_countries, 4)
    print("Global population vaccinated:", global_people_vaccinated)
    global_people_fully_vaccinated = global_vaccine_statistics(table_without_header, unique_countries, 5)
    print("Global population vaccinated:", global_people_fully_vaccinated)

    # Question 2
    print("\nQuestion 2:")
    top10_highest_vaccinated_population(table_without_header, unique_countries)

    # Question 3
    print("\nQuestion 3:")
    top10_earliest_vaccinated(table_without_header, unique_countries)

    print("\nQuestion 4:")
    top10_lowest_fully_vaccinated(table_without_header, unique_countries)


# q1a
def count_unique_locations(table):
    """
    This function is used to count how many unique locations are there in the data file

    :param table: A list of lists (each row) of each country's data
    :return: a list of unique locations
    """
    locations = [row[0] for row in table]  # A list of locations
    locations = list(set(locations))  # Duplicate removal
    return locations


# q1b
def count_unique_countries(table):
    """
    This function is used to count the number of unique countries (that do not have OWID_ prefix in the iso_code)

    :param table: A list of lists (each row) of each country's data
    :return: a list of unique countries
    """
    countries = [row[1] for row in table if "OWID_" not in row[1]]  # A list of countries
    countries = list(set(countries))  # Duplicate removal
    return countries


# q1cd
def global_vaccine_statistics(table, countries, index):
    """
    This function is used to global vaccination statistics, with different columns according to different indexes

    :param table: A list of lists (each row) of each country's data
    :param countries: A list of unique countries
    :param index: The index of column that need to be statistically counted
    :return: The Statistical results
    """
    # get a table without blank
    table_without_blank = [[row[1], row[2], row[index]] for row in table if "OWID_" not in row[1] and row[index] != '']
    number_list = []
    # to get each country's data
    for country in countries:
        country_vaccine = [row for row in table_without_blank if row[0] == country]
        if country_vaccine:
            # Sorted by date from late to early. To get the latest data
            country_vaccine.sort(key=lambda x: x[1], reverse=True)
            number_list.append(int(country_vaccine[0][2]))
    return sum(number_list)


# q2
def top10_highest_vaccinated_population(table, countries):
    """
    This function is used to find the top 10 countries with a population of at least 1 million having the highest
    percentage of their population being vaccinated with at least one dose and report the percentage of population
    being partly vaccinated.
    Print the result like: "United Arab Emirates: 98.99% population vaccinated, 2.57% partly vaccinated"

    :param table: A list of lists (each row) of each country's data
    :param countries: A list of unique countries
    """
    # data preprocess according to the requirements
    table_preprocessed = [[row[0], row[1], row[2], row[10], row[11]] for row in table if
                          "OWID_" not in row[1] and row[4] != "" and row[10] != ""
                          and row[11] != "" and float(row[10]) != 0.0 and float(row[4]) / float(row[10]) > 10000]
    result = []
    for country in countries:
        country_vaccine = [row for row in table_preprocessed if row[1] == country]
        if country_vaccine:
            # Sorted by date from late to early. To get the latest data
            country_vaccine.sort(key=lambda x: x[2], reverse=True)
            result.append(country_vaccine[0])
    # Sort the result by the vaccination percentage from large to small
    result.sort(key=lambda x: float(x[3]), reverse=True)

    # print the top 10 result
    for row in result[0:10]:
        print(row[0] + ": " + str(row[3]) + "% population vaccinated,", str(
            round(float(row[3]) - float(row[4]), 2)) + "% partly vaccinated")


# q3
def top10_earliest_vaccinated(table, countries):
    """
    This function is used to find the top 10 countries that earliest in getting their people vaccinated and
    which day they administered the highest vaccinations across all days in that country.
    Print the result like: "Latvia: first vaccinated on 2020-12-04 , 17035 people vaccinated on 2021-06-02"

    :param table: A list of lists (each row) of each country's data
    :param countries: A list of unique countries
    """
    # data preprocess according to the requirements
    table_preprocessed = [[row[0], row[1], row[2], row[8]] for row in table if
                          "OWID_" not in row[1] and row[3] != "" and int(row[3]) > 0]
    result = []
    for country in countries:
        country_vaccine = [row for row in table_preprocessed if row[1] == country]
        if country_vaccine:
            # Sorted by date from early to late
            country_vaccine.sort(key=lambda x: x[2])
            earliest_date = country_vaccine[0][2]
            country_vaccine = [row for row in country_vaccine if row[3] != ""]
            # Sorted by daily_vaccinations from large to small
            country_vaccine.sort(key=lambda x: int(x[3]), reverse=True)
            max_daily_date = country_vaccine[0][2]
            max_daily_number = country_vaccine[0][3]
            result.append([country_vaccine[0][0], earliest_date, max_daily_number, max_daily_date])
    # Sort the result by date from early to late
    result.sort(key=lambda x: x[1])

    # print the top 10 result
    for row in result[0:10]:
        print(row[0] + ": first vaccinated on " + row[1] + " , " + str(row[2]) + " people vaccinated on " + row[3])


# q4
def top10_lowest_fully_vaccinated(table, countries):
    """
    This function is to find the 10 countries the lowest percentage of fully vaccinated people, where these percentages
    are greater 50%. And predict how many days they would take to get to 80% population fully vaccinated.
    Print the result like: "Russia: 50.06% population fully vaccinated, ... days to 80%"


    :param table: A list of lists (each row) of each country's data
    :param countries: A list of unique countries
    :reference: "Linear Regression by Hand" (https://towardsdatascience.com/linear-regression-by-hand-ee7fe5a751bf)
    """
    # data preprocess according to the requirements
    table_preprocessed = [[row[0], row[1], row[2], row[11]] for row in table if
                          "OWID_" not in row[1] and row[11] != "" and float(row[11]) > 50]
    result = []
    for country in countries:
        country_vaccine = [row for row in table_preprocessed if row[1] == country]
        if country_vaccine:
            # Sorted by date from late to early. To get the latest data
            country_vaccine.sort(key=lambda x: x[2], reverse=True)
            result.append(country_vaccine[0])
    # Sort the result by fully vaccinated percentage from low to high
    result.sort(key=lambda x: float(x[3]))

    # to get the top 10 lowest countries
    top10_countries = [row[0] for row in result[0:10]]

    table_preprocessed = [[row[0], row[1], row[2], row[11]] for row in table if "OWID_" not in row[1] and row[11] != ""]
    for country in top10_countries:
        country_fully_vaccinated = [[row[2], row[3]] for row in table_preprocessed if row[0] == country]
        country_fully_vaccinated.sort(key=lambda x: x[0])
        latest_fully_vaccinated = country_fully_vaccinated[len(country_fully_vaccinated) - 1][1]

        # build a linear regression model to predict
        start_date = country_fully_vaccinated[0][0]  # the first date of vaccination
        date_list = []  # independent variable
        fully_vaccinated_list = []  # dependent variable
        for row in country_fully_vaccinated:
            # change the date to number of days from start_date
            date_list.append((datetime.datetime.strptime(row[0], "%Y-%m-%d") -
                              datetime.datetime.strptime(start_date, "%Y-%m-%d")).days)
            fully_vaccinated_list.append(float(row[1]))
        # predict function: y = kx + b (y:fully_vaccinated x:number of days)
        # using the formula in the reference above to calculate 'k' and 'b'
        n = len(date_list)
        k = (n * list_times_list(date_list, fully_vaccinated_list) - sum(date_list) * sum(fully_vaccinated_list)) \
            / (n * list_times_list(date_list, date_list) - sum(date_list) ** 2)
        b = (sum(fully_vaccinated_list) - k * sum(date_list)) / n

        # targetY = 80, get the target days from start date
        target_days = (80 - b) / k
        # minus the latest days to get the predicted value
        predict_value = int(target_days) - date_list[len(date_list) - 1] + 1

        print(country + ": " + latest_fully_vaccinated + "% population fully vaccinated,", predict_value, "days to 80%")


def list_times_list(list1, list2):
    """
    This function is to get the sum of two lists multiplied item by item
    * The length of two lists should be same.
    Example: list_times_list([1,2], [2,3]) = 1 * 2 + 2 * 3 = 8

    :param list1: the fist list
    :param list2: the second list
    :return: the sum of two lists multiplied item by item
    """
    sum_value = 0
    for i in range(len(list1)):
        sum_value += list1[i] * list2[i]
    return sum_value


# The section below will be executed when you run this file.
# Use it to run tests of your analysis function on the data
# files provided.

if __name__ == '__main__':
    # test on a CSV file
    analyse('./vaccinations.csv')
    # analyse('./vaccinations_shuffled.csv')