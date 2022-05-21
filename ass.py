"""
Template for the COMP1730/6730 project assignment, S1 2022.
The assignment specification is available on the course web
site, at https://cs.anu.edu.au/courses/comp1730/assessment/project/

Collaborators: <list the UIDs of ALL members of your project group here>
u7211790
u7167784
"""
import csv


def analyse(path_to_file):
    print("Analysing data file", path_to_file)
    with open(path_to_file) as csvfile:
        reader = csv.reader(csvfile)
        table = [row for row in reader]
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
    vaccinations_by_country(table_without_header, unique_countries)
    # Question 3
    print("\nQuestion 3:")
    earliest_countries(table_without_header, unique_countries)
    print("\nQuestion 4:")
    fully_vaccinated_rate(table_without_header, unique_countries)


# def latest_country_vaccine(table):
#     countries = count_unique_countries(table)
#     result = []
#     for country in countries:
#         country_vaccine = [row for row in table if
#                            row[3] != '' and "OWID_" not in row[1] and row[1] == country]
#         country_vaccine.sort(key=lambda x: x[2], reverse=True)
#         result.append(country_vaccine[0])
#     return result


# 1a
def count_unique_locations(table):
    """
    Count how many unique locations are there in the data file.
    Parameter table: A list of lists (each row).
    Parameter locations: A list of locations (Duplicate removal).
    Return a total number of unique locations.
    """
    locations = [row[0] for row in table]  # A list of locations
    locations = list(set(locations))  # Duplicate removal
    return locations


# 1b
def count_unique_countries(table):
    """
    Count the number of unique countries (that do not have OWID_ prefix in the iso_code).
    Parameter table: A list of lists (each row).
    Parameter countries: A list of countries (Duplicate removal).
    Return a total number of unique countries.
    """
    countries = [row[1] for row in table if "OWID_" not in row[1]]
    countries = list(set(countries))
    return countries


# 1cd
def global_vaccine_statistics(table, countries, index):
    table_without_blank = [[row[1], row[2], row[index]] for row in table if "OWID_" not in row[1] and row[index] != '']
    number_list = []
    for country in countries:
        country_vaccine = [row for row in table_without_blank if row[0] == country]
        if country_vaccine:
            country_vaccine.sort(key=lambda x: x[1], reverse=True)
            number_list.append(int(country_vaccine[0][2]))
    return sum(number_list)


# 2ab
def vaccinations_by_country(table, countries):
    table_preprocessed = [[row[0], row[1], row[2], row[10], row[11]] for row in table if
                          "OWID_" not in row[1] and row[4] != "" and row[10] != ""
                          and row[11] != "" and float(row[10]) != 0.0 and float(row[4]) / float(row[10]) > 10000]
    result = []
    for country in countries:
        country_vaccine = [row for row in table_preprocessed if row[1] == country]
        if country_vaccine:
            country_vaccine.sort(key=lambda x: x[2], reverse=True)
            result.append(country_vaccine[0])
    result.sort(key=lambda x: float(x[3]), reverse=True)

    for row in result[0:10]:
        print(row[0] + ": " + str(row[3]) + "% population vaccinated," + str(
            round(float(row[3]) - float(row[4]), 2)) + "% partly vaccinated")


# 3ab
def earliest_countries(table, countries):
    table_preprocessed = [[row[0], row[1], row[2], row[8]] for row in table if
                          "OWID_" not in row[1] and row[3] != "" and int(row[3]) > 0]
    result = []
    for country in countries:
        country_vaccine = [row for row in table_preprocessed if row[1] == country]
        if country_vaccine:
            country_vaccine.sort(key=lambda x: x[2])
            earliest_date = country_vaccine[0][2]
            country_vaccine = [row for row in country_vaccine if row[3] != ""]
            country_vaccine.sort(key=lambda x: int(x[3]), reverse=True)
            max_daily_date = country_vaccine[0][2]
            max_daily_number = country_vaccine[0][3]
            result.append([country_vaccine[0][0], earliest_date, max_daily_number, max_daily_date])
    result.sort(key=lambda x: x[1])

    for row in result[0:10]:
        print(row[0] + ": first vaccinated on " + row[1] + " , " + str(row[2]) + " people vaccinated on " + row[3])


# 4ab
def fully_vaccinated_rate(table, countries):
    table_preprocessed = [[row[0], row[1], row[11]] for row in table if
                          "OWID_" not in row[1] and row[11] != "" and float(row[11]) > 50]
    result = []
    for country in countries:
        country_vaccine = [row for row in table_preprocessed if row[1] == country]
        if country_vaccine:
            country_vaccine.sort(key=lambda x: x[2], reverse=True)
            result.append(country_vaccine[0])
    result.sort(key=lambda x: float(x[2]))

    for row in result[0:10]:
        print(row[0] + ": " + row[2] + "% population fully vaccinated")


# The section below will be executed when you run this file.
# Use it to run tests of your analysis function on the data
# files provided.

if __name__ == '__main__':
    # test on a CSV file
    # analyse('./vaccinations.csv')
    analyse('./vaccinations_shuffled.csv')
