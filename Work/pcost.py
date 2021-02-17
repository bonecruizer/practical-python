# pcost.py
#
# Exercise 1.27
portfolio = open('Data/portfolio.csv','rt')
headers = next(portfolio)

currentline = []
totalcost = 0

for line in portfolio:
    currentline = line.split(',')
    stockcost = int(currentline[1]) * float(currentline[2])
    print(f'Cost of: {currentline[0]} ,=  {currentline[1]}, x  {currentline[2].strip()} = {stockcost:.2f}')
    totalcost = totalcost + stockcost




portfolio.close()

print(f'Total Cost: {totalcost}')
