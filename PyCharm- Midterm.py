import numpy as np
import pandas as pd
import glob
import matplotlib.pyplot as plt
# import os.path
# from math import sqrt
# import re

#Variables
cash = 5000000
initial_investment = cash / 5
portfolio = ['IBM', 'MSFT', 'GOOG', 'AAPL', 'AMZN']
rebal_inverval = 5
MTM = 0
# Dictonaries
stock_dict = {}
div_days_dict = {}
stock_shares_dict = {}
cash_left = {}
adj_close_percent_change = {}
# Lists
stockmarket = []
cash_list = []
shares_list = []
close_price_list = []
# check_max = []




#creates DF
'/n'
for path in glob.glob('*.csv'):

    stock_ticker = path.strip('.csv')

    stock_dict[stock_ticker] = pd.read_csv(path, usecols=['Date','Close','Adj Close'],index_col='Date')
    stock_dict[stock_ticker].insert(2, 'Close Ratio', stock_dict[stock_ticker]['Close'].shift(+1)/stock_dict[stock_ticker]['Close'])
    stock_dict[stock_ticker].insert(3, 'Adj Close Ratio', stock_dict[stock_ticker]['Adj Close'].shift(+1) / stock_dict[stock_ticker]['Adj Close'])
    stock_dict[stock_ticker].insert(4, stock_ticker + ' Dividend',abs(round((stock_dict[stock_ticker]['Adj Close Ratio'] - stock_dict[stock_ticker]['Close Ratio']), 5)))
    stock_dict[stock_ticker].insert(5,stock_ticker + ' % change', (stock_dict[stock_ticker]['Adj Close'].shift(rebal_inverval) /stock_dict[stock_ticker]['Adj Close'].shift(0) - 1)*100)

    universe = pd.concat(stock_dict,axis=1)

    div_ser = stock_dict[stock_ticker][stock_ticker + ' Dividend'].loc[stock_dict[stock_ticker][stock_ticker + ' Dividend'] > 0]
    div_days_dict[stock_ticker] = div_ser


#insert MTM col
universe.insert(60, 'MTM', 12)

#calculate MTM col
for i in range(0,len(universe)):
    for j in range(0,len(portfolio)):
        ticker = portfolio[j]
        close_price = np.array(universe.iloc[i].loc[ticker]['Close'])
        stock_shares = np.array(float(int(initial_investment / close_price)))
        cash_left = np.array(initial_investment - (stock_shares * close_price))
        MTM += cash_left +(stock_shares * close_price)
    universe.ix[i, 'MTM'] = MTM

# Plotting MTM
'\n'
plt.plot(universe['MTM'])
plt.ylabel('MTM Value')
plt.xlabel('Date')
plt.show()

'\n'

# calculate percent change and choose 5 stocks to reinvest in.
check_max = universe.filter(regex= '% change').iloc[5].sort_values()
new_portfolio = universe.filter(regex= '% change').iloc[5].sort_values().keys().get_level_values(0)
# print(check_max[:5])
# print(type(check_max),'\n')

portfolio = list(new_portfolio[:5])
print(portfolio)
# print(type(portfolio))
