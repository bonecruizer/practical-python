# pcost_function.py
#
# using csv reader for much cleaner code.
#
# Exercise 1.30, 1.31
import csv
import sys


def portfolio_cost(filename):
    portfolio = open(filename, 'rt')
    rows = csv.reader(portfolio)
    headers = next(rows)

    currentline = []
    totalcost = 0

    for row in rows:

        try:
            stockcost = int(row[1]) * float(row[2])
            print(f'Cost of: {row[0]} ,=  {row[1]}, x  {row[2]} = {stockcost:.2f}')
            # print(f'Cost of: {row[0]} ,=  {row[1]}, x  {row[2]} = {stockcost}') unformatted float
        except ValueError:
            print('Error in file, fields missing?', row)

        totalcost = totalcost + stockcost

    portfolio.close()

    # print(f'Total Cost: {totalcost}')
    return totalcost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost: ', cost)
