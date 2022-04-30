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
    # Question1
    print("\nQuestion 1:")
    unique_locations = count_unique_locations(table_without_header)
    unique_countries = count_unique_countries(table_without_header)

    pass


def count_unique_locations(table):
    locations = [row[0] for row in table]
    locations = list(set(locations))
    print("Number of unique locations:", len(locations))
    return len(locations)


def count_unique_countries(table):
    countries = [row[1] for row in table]
    countries = list(set(countries))
    count = 0
    for country in countries:
        if "OWID_" not in country:
            count += 1
    print("Number of unique countries:", count)
    return count


# The section below will be executed when you run this file.
# Use it to run tests of your analysis function on the data
# files provided.

if __name__ == '__main__':
    # test on a CSV file
    analyse('./vaccinations.csv')
