"""
Template for the COMP1730/6730 project assignment, S1 2022.
The assignment specification is available on the course web
site, at https://cs.anu.edu.au/courses/comp1730/assessment/project/

Collaborators: <list the UIDs of ALL members of your project group here>
u7211790
u7167784
"""
import csv
import time


def analyse(path_to_file):
    print("Analysing data file", path_to_file)
    with open(path_to_file) as csvfile:
        reader = csv.reader(csvfile)
        table = [row for row in reader]
    # get the table without header
    table_without_header = [table[i] for i in range(1, len(table))]
    unique_countries = count_unique_countries(table_without_header)
    # Question 3
    print("\nQuestion 3:")
    top10_earliest_vaccinated2(table_without_header, unique_countries)


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


def top10_earliest_vaccinated2(table, countries):
    """
    This function is used to find the top 10 countries that earliest in getting their people vaccinated and
    which day they administered the highest vaccinations across all days in that country.
    Print the result like: "Latvia: first vaccinated on 2020-12-04 , 17035 people vaccinated on 2021-06-02"

    :param table: A list of lists (each row) of each country's data
    :param countries: A list of unique countries
    """
    # data preprocess according to the requirements
    table_preprocessed = [[row[0], row[1], row[2]] for row in table if
                          "OWID_" not in row[1] and row[3] != "" and int(row[3]) > 0]
    result = []
    for country in countries:
        country_vaccine = [row for row in table_preprocessed if row[1] == country]
        if country_vaccine:
            # Sorted by date from early to late
            country_vaccine.sort(key=lambda x: x[2])
            # earliest_date = country_vaccine[0][2]
            # country_vaccine = [row for row in country_vaccine if row[3] != ""]
            # # Sorted by daily_vaccinations from large to small
            # country_vaccine.sort(key=lambda x: int(x[3]), reverse=True)
            # max_daily_date = country_vaccine[0][2]
            # max_daily_number = country_vaccine[0][3]
            result.append(country_vaccine[0])
    # Sort the result by date from early to late
    result.sort(key=lambda x: x[2])

    top10 = result[0:10]
    table_preprocessed = [[row[1], row[8], row[2]] for row in table if
                          "OWID_" not in row[1] and row[8] != ""]
    max_date_list = []
    for country in top10:
        country_vaccine = [row for row in table_preprocessed if row[0] == country[1]]
        country_vaccine.sort(key=lambda x: int(x[1]), reverse=True)
        max_date_list.append([country_vaccine[0][1], country_vaccine[0][2]])


    # print the top 10 result
    for i in range(10):
        print(result[i][0] + ": first vaccinated on " + result[i][2] + " , " + max_date_list[i][0] + "people vaccinated on " + max_date_list[i][1])



# The section below will be executed when you run this file.
# Use it to run tests of your analysis function on the data
# files provided.

if __name__ == '__main__':
    # test on a CSV file
    # analyse('./vaccinations.csv')
    start = time.perf_counter()
    analyse('./vaccinations_shuffled.csv')
    end = time.perf_counter()
    print(end - start)

