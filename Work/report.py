# pcost_function.py
#
# using csv reader for much cleaner code.
# Creates a list of tuples

# Exercise 2.9
import csv
import sys


def portfolio_read(filename):
    contents = open(filename, 'rt')
    rows = csv.reader(contents)
    headers = next(rows)
    portfolio = []

    for row in rows:
        holding = (row[0], int(row[1]), float(row[2]))
        portfolio.append(holding)

    contents.close()

    return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/missing.csv'

