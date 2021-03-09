# pcost_function.py
#
# using csv reader for much cleaner code.
# Creates a list of dictionaries

# Exercise 2.5
import csv
import sys


def portfolio_read(filename):
    contents = open(filename, 'rt')
    rows = csv.reader(contents)

    headers = next(rows)

    portfolio = []

    for row in rows:
        print(row)
        holding = {headers[0]: row[0],
                   headers[1]: row[1],
                   headers[2]: row[2]
                   }
        portfolio.append(holding)

    contents.close()

    return portfolio


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfolio.csv'



