#!/usr/bin/env python3
# pcost_function.py
#
# Exercise 1.30, 1.31

from report import read_portfolio


def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    totalcost = 0
    for row in portfolio:

        try:
            stockcost = (row['shares']) * (row['price'])

        except ValueError:
            print('Error in file, fields missing?', row)

        totalcost += stockcost

    return totalcost



def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    cost = portfolio_cost(args[1])
    print('Total cost: ', cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)

