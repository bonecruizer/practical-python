# pcost_function.py
#
# Exercise 1.30, 1.31

def portfolio_cost(filename):
    portfolio = open(filename, 'rt')
    headers = next(portfolio)

    currentline = []
    totalcost = 0

    for line in portfolio:
        currentline = line.split(',')
        try:
            stockcost = int(currentline[1]) * float(currentline[2])
            # print(f'Cost of: {currentline[0]} ,=  {currentline[1]}, x  {currentline[2].strip()} = {stockcost:.2f}')
        except ValueError:
            print('Error in file, fields missing?', line)


        totalcost = totalcost + stockcost

    portfolio.close()

    # print(f'Total Cost: {totalcost}')
    return totalcost


cost = portfolio_cost('Data/missing.csv')
print('Total cost: ', cost)
