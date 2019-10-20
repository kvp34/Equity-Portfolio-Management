import numpy as np
import pandas as pd
import glob
import os.path
from math import sqrt
import re

#Variables
cash = 5000000
initial_investment = cash / 5
portfolio = ['IBM', 'MSFT', 'GOOG', 'AAPL', 'AMZN']
rebal_inverval = 5
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


# calculate percent change and choose 5 stocks to reinvest in.
check_max = universe.filter(regex= '% change').iloc[5].sort_values()
new_portfolio = universe.filter(regex= '% change').iloc[5].sort_values().keys().get_level_values(0)
print(check_max[:5])
print(type(check_max),'\n')

portfolio = list(new_portfolio[:5])
print(portfolio)
print(type(portfolio))

# print(universe.filter(regex= '% change').iloc[5].sort_values()) # Want to print an index from multiindex ..MultiIndex.get_level_values
# need multiindex from series

    # # Pulling Info at each rebalance
    # i=0
    # c = len(universe)
    # while i < 5:
    #     # print(i)
    #     # print(stock_dict[stock_ticker][stock_ticker + ' % change'].iloc[i+rebal_inverval])
    #     check_max.append(stock_dict[stock_ticker][stock_ticker + ' % change'].iloc[i + rebal_inverval])
    #     print(type(check_max))
    #     print(check_max)
    #     i = i + rebal_inverval

# print(universe)
# print(universe.to_string())
'/n'

'/n'
# # Pulling Info at each rebalance
# i=0
# c = len(universe)
# while i < 6:
#     print(i)
#     print(universe[stock_ticker + ' % change'].iloc[i])
#     i = i + rebal_inverval
'/n'


# initial investment - MTM Loop - Do Not delete
'/n'
for i in range(0,len(portfolio)):
    ticker = portfolio[i]

    close_price = stock_dict[ticker]['Close'].iloc[0]
    stock_shares_dict[ticker + ' Shares'] = float(int(initial_investment/close_price))
    cash_left[ticker] = initial_investment - (stock_shares_dict[ticker + ' Shares'] * close_price)

    cash_list.append(cash_left[ticker])
    shares_list.append(stock_shares_dict[ticker + ' Shares'])
    close_price_list.append(close_price)

    cash_arr = np.asarray(cash_list)
    shares_arr = np.asarray(shares_list)
    close_price_arr = np.asarray(close_price_list)
    MTM = sum(cash_arr) + sum(shares_arr * close_price_arr)
# print(MTM)
'/n'


# initial investment MTM Loop Copy - working on rebalancing
for i in range(0,len(portfolio)):
    ticker = portfolio[i]

    close_price = stock_dict[ticker]['Close'].iloc[0]
    stock_shares_dict[ticker + ' Shares'] = float(int(initial_investment/close_price))
    cash_left[ticker] = initial_investment - (stock_shares_dict[ticker + ' Shares'] * close_price)

    cash_list.append(cash_left[ticker])
    shares_list.append(stock_shares_dict[ticker + ' Shares'])
    close_price_list.append(close_price)

    cash_arr = np.asarray(cash_list)
    shares_arr = np.asarray(shares_list)
    close_price_arr = np.asarray(close_price_list)
    MTM = sum(cash_arr) + sum(shares_arr * close_price_arr)
# print(MTM)
'/n'





# # Cash
# # print(cash_list)
# # print(type(cash_list))
#
# cash_arr = np.asarray(cash_list)
# # print(cash_arr)
# #
# # # Shares
# # print(shares_list)
# # print(type(shares_list))
#
# shares_arr = np.asarray(shares_list)
# # print(shares_arr)
# # print(type(shares_arr))
#
# # Close Price
# # print(close_price_list)
# # print(type(close_price_list))
#
# close_price_arr = np.asarray(close_price_list)
# # print(close_price_arr)
# # print(type(close_price_arr))
#
# MTM = sum(cash_arr) + sum(shares_arr * close_price_arr)
# print(MTM)

#____________________________________MTM Equation_________________________________________________________________
# MTM = cash_left[ticker] + (stock_shares_dict[ticker + ' Shares'] * close_price)
# print(MTM)
#____________________________________MTM Equation_________________________________________________________________
#
# print(close_price)
# print(type(close_price)) #float
#
# print(stock_shares_dict[ticker + ' Shares'])
# print(type(stock_shares_dict[ticker + ' Shares'])) #int
#
# print(cash_left[ticker])
# print(type(cash_left[ticker])) #float





# print(universe.iloc[5]/universe.iloc[0])
# print(type(universe.iloc[5]))
# print(universe.filter(regex='Dividend',axis=1))
# print(universe.filter(regex='Dividend',axis=1).iloc[5])
# print(type(universe.filter(regex='Dividend',axis=1).iloc[5]))
# print(list(universe.filter(regex='Dividend',axis=1).iloc[5]))  #https://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers
# print(universe.get_level_values())



# # print(universe)
# print(div_days_dict.keys())
# print(div_days_dict)

# print(stock_dict['AAPL']['AAPL Dividend'].loc[stock_dict['AAPL']['AAPL Dividend'] > 0]) # returns values from specific dictonary
# print(stock_dict['SAP']['SAP Dividend'].loc[stock_dict['SAP']['SAP Dividend'] > 0]) # returns values from specific dictonary


# for path in glob.glob('*.csv'): #searches directory for *csv files
#     stock_ticker = path.strip('.csv')  # cleans file path of .csv
#     # print(stock_dict[stock_ticker][stock_ticker + ' Dividend'].loc[stock_dict[stock_ticker][stock_ticker + ' Dividend'] > 0])
#     div_ser = stock_dict[stock_ticker][stock_ticker + ' Dividend'].loc[stock_dict[stock_ticker][stock_ticker + ' Dividend'] > 0]
#     # print(type(div_ser))
#     div_days_dict[stock_ticker] = div_ser
#

# print(universe.to_string())


#check types
# print(type(universe)
# print(type(stock_dict))
# print(type(stock_dict['TSLA']))
# print(stock_dict['TSLA'])
# print(type(stock_dict['TSLA']['TSLA Dividend']))
# print(stock_dict['TSLA']['TSLA Dividend'])
# print(stock_dict['TSLA']['TSLA Dividend'].to_string())
# print(dfTSLA.loc[(stock_dict['TSLA']['TSLA Dividend']>0)])





# print(universe['TSLA']['TSLA Dividend'].loc[universe['TSLA']['TSLA Dividend']>0]) # Cannot index with multidimensional key
# print(stock_dict['TSLA']['TSLA Dividend'].loc[stock_dict['TSLA']['TSLA Dividend'] > 0]) # returns values from specific dictonary
# print(stock_dict['TSLA']['TSLA Dividend'].loc[stock_dict['TSLA']]) #https://github.com/pandas-dev/pandas/issues/7981 , ValueError: Cannot index with multidimensional key








# Midterm Directions #1:
# Starting on jan 2 , buy 1 mil of each of these stocks: ['IBM', 'MSFT', 'GOOG', 'AAPL',
# 'AMZN' must buy a whole number of stocks
# remainder of money is left as cast earning zero percent. Add ability toearn interest
# The value of your holdings and cash is defined by the MTM equation
# MTM = cash + sum(shares * close price)



# Midterm Directions
    # make the day you rebalance a variable to simplify
    # finding the optimal number of days before rebalancing
    # See Direction #9

#Trading Strategies:

# 5 day rebalancing of buying low
    # after 5 days rebalance your portfolio
    # determine on the 5th day the %change in Adj Close price for each stock
    # sell portfolio (convert to cash) at the current day's close/adj close
    # determine the 5 stocks which changed the most
    # evenly split cash and buy the 5 stocks which changed the most
    # buy the max shares and hold remainder in cash

# 5 day rebalancing of buying high
    # after 5 days rebalance your portfolio
    # determine on the 5th day the %change in Adj Close price for each stock
    # sell portfolio (convert to cash) at the current day's close/adj close
    # determine the 5 stocks which changed the most
    # evenly split cash and buy the 5 stocks which changed the most
    # buy the max shares and hold remainder in cash
    # #


#  Dividends:
    # Assumption: dividend days are defined from HW#2
    # On dividend days you get a return on stocks held.
    # dividend return defined as dividend = ($1.5x#of shares of stock)
    # stocks bought on dividend day do not qualify for dividend
    # stocks sold on dividend day do qualify for dividend
    # dividend is deposited to cash accound
    # #


# Plotting:
    # created a High Tech Index of the daily averages of the 10 stocks Close price
    # compare MTM to High tech index and plot curves
    # suggestion: to plot curves together convert the series to daily percentage
    # daily percent change with regard to beinging of year
    # #


# Convert to JPY
    # convert your MTM to JPY using Close column
    # plot JPY to USD MTM
    # Convert daily percentage change as well... daily percent change should be same...
    #