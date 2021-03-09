# pcost.py
#
# Exercise 2.15, 2.16, 2.17
import csv

def portfolio_cost(filename):

    portfolio = open(filename,'rt')
    rows = csv.reader(portfolio)
    headers = next(rows)

    totalcost = 0

    for rownr,currentline in enumerate(rows):
        record = dict(zip(headers, currentline))

        try:
            #currentline = line.split(',')
            stockcost = int(record['shares']) * float(record['price'])

            print(f"Cost of: {record['name']} ,=  {record['shares']}, x  {record['price'].strip()} = {stockcost:.2f}")
            totalcost = totalcost + stockcost
        except ValueError:
            print(f"Row {rownr}: Couldn\'t convert: {currentline}")




    portfolio.close()

    print(f'Total Cost: {totalcost}')

portfolio_cost('Data/portfoliodate.csv')
#portfolio_cost('Data/missing.csv')
