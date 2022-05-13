"""
Template for the COMP1730/6730 project assignment, S1 2022.
The assignment specification is available on the course web
site, at https://cs.anu.edu.au/courses/comp1730/assessment/project/

Collaborators: <list the UIDs of ALL members of your project group here>
u7211790
u7167784
"""
import csv

from numpy import sort


def analyse(path_to_file):
    print("Analysing data file", path_to_file)
    with open(path_to_file) as csvfile:
        reader = csv.reader(csvfile)
        table = [row for row in reader]
    table_without_header = [table[i] for i in range(1, len(table))]
    # Question 1
    # print("\nQuestion 1:")
    # unique_locations = count_unique_locations(table_without_header)
    # unique_countries = count_unique_countries(table_without_header)
    # global_vaccince_doses(table_without_header)
    # global_population_vaccinated(table_without_header)
    # global_fully_population_vaccinated(table_without_header)
    # Question 2
    print("\nQuestion 2:")
    vaccinations_by_country(table_without_header)
    # population_partly_vaccinated_by_country(table_without_header)
    # Question 3
    print("\nQuestion 3:")
    earliest_countries(table_without_header)
    # peak_days(table_without_header)
    print("\nQuestion 4:")
    fully_vaccinated_rate(table_without_header)


# 1a
def count_unique_locations(table):
    """
    Count how many unique locations are there in the data file.
    Parameter table: A list of lists (each row).
    Parameter locations: A list of locations (Duplicate removal).
    Return a total number of unique locations.
    """
    locations = [row[0] for row in table] # A list of locations 
    locations = list(set(locations)) # Duplicate removal
    print("Number of unique locations:", len(locations))
    return len(locations)

# 1b
def count_unique_countries(table):
    """
    Count the number of unique countries (that do not have OWID_ prefix in the iso_code).
    Parameter table: A list of lists (each row).
    Parameter countries: A list of countries (Duplicate removal).
    Return a total number of unique countries.
    """
    countries = [row[1] for row in table] # A list of countries
    countries = list(set(countries)) # Duplicate removal
    count = 0
    for country in countries:
        if "OWID_" not in country: # Check countries do not have OWID_ prefix
            count += 1
    print("Number of unique countries:", count)
    return count

# 1c
def global_vaccince_doses(table):
    """
    Count the total number of vaccine doses that have been globally administered in all countries.
    Parameter table: A list of lists (each row).
    Parameter countries_total_vax: A list of countries meet the criteria with its total_vaccinations.
    Parameter result: A list of countries meet the criteria with its biggest total_vaccinations.
    Parameter count: A list of biggest total_vaccinations for each country meets the criteria.
    Return a total number of count.
    """
    countries_total_vax = [[row[1], row[3]] for row in table if "OWID_" not in row[1] and row[3] != ""]
    result = []
    for i in range(len(countries_total_vax)):
        if(i == len(countries_total_vax)-1 or countries_total_vax[i][0] != countries_total_vax[i+1][0]):
            result.append(countries_total_vax[i])
    count = [int(row[1]) for row in result]
    print("Global vaccince doses:", sum(count))
    return sum(count)

# 1d
def global_population_vaccinated(table):
    """
    Count the global number of people who have received at least one dose over all countries in the world.
    Parameter table: A list of lists (each row).
    Parameter countries_people_vaccinated: A list of countries meet the criteria with its people_vaccinated.
    Parameter result: A list of countries meet the criteria with its biggest people_vaccinated.
    Parameter count: A list of biggest people_vaccinated for each country meets the criteria.
    Return a total number of count.
    """
    countries_people_vaccinated = [[row[1], row[4]] for row in table if "OWID_" not in row[1] and row[4] != ""]
    result = []
    for i in range(len(countries_people_vaccinated)):
        if(i == len(countries_people_vaccinated)-1 or countries_people_vaccinated[i][0] != countries_people_vaccinated[i+1][0]):
            result.append(countries_people_vaccinated[i])
    count = [int(row[1]) for row in result]
    print("Global population vaccinated:", sum(count))
    return sum(count)


def global_fully_population_vaccinated(table):
    """
    Count the global number of people who are fully vaccinated.
    Parameter table: A list of lists (each row).
    Parameter countries_people_fully_vaccinated: A list of countries meet the criteria with its people_fully_vaccinated.
    Parameter result: A list of countries meet the criteria with its biggest people_fully_vaccinated.
    Parameter count: A list of biggest people_fully_vaccinated for each country meets the criteria.
    Return a total number of count.
    """
    countries_people_fully_vaccinated = [[row[1], row[5]] for row in table if "OWID_" not in row[1] and row[5] != ""]
    result = []
    for i in range(len(countries_people_fully_vaccinated)):
        if(i == len(countries_people_fully_vaccinated)-1 or countries_people_fully_vaccinated[i][0] != countries_people_fully_vaccinated[i+1][0]):
            result.append(countries_people_fully_vaccinated[i])
    count = [int(row[1]) for row in result]
    print("Global population fully vaccinated:", sum(count))
    return sum(count)


# 2ab
def vaccinations_by_country(table):
    countries_vaccinations_rate = [[row[0], row[4], float(row[10]), round(float(row[10])-float(row[11]), 2)] for row in table if "OWID_" not in row[1] and row[4] != "" 
    and row[10] != "" and row[11] != "" and float(row[10]) != 0.0 and int(row[4])/float(row[10]) > 10000]
    result = []
    for i in range(len(countries_vaccinations_rate)):
        if(i == len(countries_vaccinations_rate)-1 or countries_vaccinations_rate[i][0] != countries_vaccinations_rate[i+1][0]):
            result.append(countries_vaccinations_rate[i])
    result.sort(key = lambda x:x[2],reverse=True)
    # 2a
    for row in result[0:10]:
        print(row[0]+": "+str(row[2])+"% population vaccinated")
    # 2b
    for row in result[0:10]:
        print(row[0]+": "+str(row[2])+"% population vaccinated,"+str(row[3])+"% partly vaccinated")

    return result[0:10]
    

# 2b
# def population_partly_vaccinated_by_country(table):
#     countries_1stvaccinations_rate = [[row[0], round(float(row[10])-float(row[11]), 2)] for row in table if "OWID_" not in row[1] and row[10] != "" 
#     and row[11] != ""]
#     result = []
#     for i in range(len(countries_1stvaccinations_rate)):
#         if i == len(countries_1stvaccinations_rate) -1 or countries_1stvaccinations_rate[i][0] != countries_1stvaccinations_rate[i+1][0]:
#             result.append(countries_1stvaccinations_rate[i])
    # print(result)

    # top10_countries = vaccinations_by_country(table)

    # for i in range(len(top10_countries)):
    #     for j in range(len(result)):
    #         if result[j][0] == top10_countries[i][0]:
    #             print(top10_countries[i][0]+": "+str(top10_countries[i][2])+"% population vaccinated,"+str(result[j][1])+"% partly vaccinated")


# def fun(x):
#     return x[1]

# 3ab
def earliest_countries(table):
    countries_date = [[row[0], row[8],row[2]] for row in table 
    if "OWID_" not in row[1] and row[3] != "" and int(row[3]) > 0]
    result = []
    # result.append(countries_date[0])
    for i in range(len(countries_date)):
        if(i == 0 or countries_date[i][0] != countries_date[i-1][0]):
            result.append(countries_date[i])
    # top10_countries_date = topN(result, 1, 10, False)
    # for countries_date in top10_countries_date:
    #     print(countries_date[0]+": first vaccinated on",countries_date[1])

    result.sort(key = lambda x:x[2])
    # result.sort(key = fun)

    # 3a
    for row in result[0:10]:
        print(row[0]+": first vaccinated on",row[2])
    # 3b
    for country_date in result[0:10]:
        each_country_daily_vaccinations = [[row[0],int(row[1]),row[2]] for row in countries_date if country_date[0] == row[0] and row[1] != ""]
        max_daily_vaccinations = max(each_country_daily_vaccinations)
        print(country_date[0] + ": first vaccinated on " + country_date[2] + " , " + str(max_daily_vaccinations[1]) + " people vaccinated on " + max_daily_vaccinations[2])

    return result[0:10]
    # date_list = [row[1] for row in result]
    # date_list.sort()
    # date_list = list(set(date_list[0:10]))
    # date_list.sort()
    # top10_countries_date = []
    # for date_value in date_list:
    #     for row in result:
    #         if date_value == row[1]:
    #             top10_countries_date.append([row[0], date_value])
    #             print(row[0]+": first vaccinated on",date_value)
    # return top10_countries_date

# 3b
# def peak_days(table):
#     top10_countries_date = earliest_countries(table)

#     countries_daily_vaccinations = [[row[0], int(row[8]),  row[2]] for row in table if "OWID_" not in row[1] and row[8] != "" and int(row[8]) > 0]
#     for country_date in top10_countries_date:
#         each_country_daily_vaccinations = [row for row in countries_daily_vaccinations if country_date[0] == row[0]]
#         max_daily_vaccinations = max(each_country_daily_vaccinations)
#         print(country_date[0] + ": first vaccinated on " + country_date[1] + " , " + str(max_daily_vaccinations[1]) + " people vaccinated on " + max_daily_vaccinations[2])

# def topN(table, target, N, reverse):
#     target_list = [row[target] for row in table]
#     if reverse == True:
#         target_list.sort(reverse=True)
#     else:
#         target_list.sort()
#     target_list = list(set(target_list[0:N]))
#     if reverse == True:
#         target_list.sort(reverse=True)
#     else:
#         target_list.sort()
#     topN_result = []
#     for data in target_list:
#         for row in table:
#             if data == row[target]:
#                 topN_result.append(row)
#     return topN_result

# 4ab
def fully_vaccinated_rate(table):
    countries_fully_vaccinated = [[row[0], float(row[11])] for row in table if "OWID_" not in row[1] and row[11] != "" and float(row[11]) > 50]
    result = []
    # result.append(countries_date[0])
    for i in range(len(countries_fully_vaccinated)):
        if(i == len(countries_fully_vaccinated)-1 or countries_fully_vaccinated[i][0] != countries_fully_vaccinated[i+1][0]):
            result.append(countries_fully_vaccinated[i])
    result.sort(key = lambda x:x[1])
    # print(result[0:10])
    # 4a
    for row in result[0:10]:
        print(row[0]+": "+str(row[1])+"% population fully vaccinated")
# The section below will be executed when you run this file.
# Use it to run tests of your analysis function on the data
# files provided.

if __name__ == '__main__':
    # test on a CSV file
    analyse('./vaccinations.csv')