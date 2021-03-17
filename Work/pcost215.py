# report.py
#
# using csv reader for much cleaner code.
# Creates a list of tuples

import csv


def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name': record['name'],
                'shares': int(record['shares']),
                'price': float(record['price'])
            }
            portfolio.append(stock)
    return portfolio


def read_prices(filename):
    '''
    Read the current prices from a csv file and returns a list of dictionaries
    '''
    contents = open(filename, 'rt')
    rows = csv.reader(contents)

    prices = {}
    for line in rows:
        if line.__len__() > 0:
            prices[line[0]] = float(line[1])

    contents.close()

    return prices


def make_report(portfolio, prices):
    '''
    create a report with portfolio and prices as input and return a list of tuples
    '''
    report = []

    for item in portfolio:

        name = item['name']
        shares = item['shares']
        orig_price = item['price']
        current_price = float(prices[name])
        change =  float(current_price) - float(orig_price)

        lines = (name,shares,orig_price, current_price, change)
        report.append(lines)

    return report

def print_report(report):
    '''
    Generate and print a report
    '''
    headers = ('Name', 'Shares', 'Price', 'Current', 'Change')

    print(f'{headers[0]:<10s} {headers[1]:<10s} {headers[2]:<10s} {headers[3]:<10s} {headers[4]:>10s} ')
    print(('-' * 10 + ' ') * len(headers))
    for line in report:
        print(f" {line[0]:<10s}  {line[1]:<10}  {line[2]:<8.2f} {line[3]:<10.2f} {line[4]:>10.2f}")


def portfolio_report(portfolio_filename, prices_filename):
    '''
    Combine all functions
    '''
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    report = make_report(portfolio,prices)
    print_report(report)


portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
print('toet')



