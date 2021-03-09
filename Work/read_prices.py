# pcost_function.py
#
# using csv reader for much cleaner code.
# Creates a ldictionary from csv file

# Exercise 2.6
import csv
import sys
from pprint import pprint


def read_prices(filename):
    contents = open(filename, 'rt')
    rows = csv.reader(contents)
    #headers = next(rows)

    prices = {}
    for line in rows:
        if line.__len__() > 0:

            prices[line[0]] = line[1]

    contents.close()

    return prices


#prices = read_prices('Data/prices.csv')
#pprint(prices)
