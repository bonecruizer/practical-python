# pcost_function.py
#
# using csv reader for much cleaner code.
# Creates a dictionary with prices from csv file and a list of stocks to calc. gain/loss

# Exercise 2.7 an d 2.10 (formatted)
import csv


# reads current prices
def read_prices(filename):
    contents = open(filename, 'rt')
    rows = csv.reader(contents)

    prices = {}
    for line in rows:
        if line.__len__() > 0:
            prices[line[0]] = line[1]

    contents.close()

    return prices


# read portfolio with buyin prices
def portfolio_read(filename):
    contents = open(filename, 'rt')
    rows = csv.reader(contents)
    headers = next(rows)
    portfolio = []

    for rownr, row in enumerate(rows):
        record = dict(zip(headers, row))
        holding = (record['name'], int(record['shares']), float(record['price']))
        portfolio.append(holding)

    contents.close()

    return portfolio


def make_report(portfolio, prices):

    report = []

    for item in portfolio:

        name = item[0]
        shares = item[1]
        orig_price = float(item[2])
        current_price = float(prices[name])
        change =  float(current_price) - float(orig_price)

        lines = (name,shares,orig_price, current_price, change)
        report.append(lines)

    return report

portfolio = portfolio_read('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')

report = make_report(portfolio,prices)
headers = ('Name', 'Shares', 'Price', 'Current', 'Change')

print(f'{headers[0]:<10s} {headers[1]:<10s} {headers[2]:<10s} {headers[3]:<10s} {headers[4]:>10s} ')
print('---------- ---------- ---------- ---------- ----------')
for line in report:
    print(f" {line[0]:<10s}  {line[1]:<10}  {line[2]:<8.2f} {line[3]:<10.2f} {line[4]:>10.2f}")



