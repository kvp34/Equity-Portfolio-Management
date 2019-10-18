import numpy as np
import glob as glob
import pandas as pd
import os.path
from math import sqrt
import glob                                                     # glob is a module that files all pathnames matching a specified pattern
import re




# create empty structures
stockmarket = []  # empty list to be filled with stock tickers
stock_dict = {}  # empty dict to be filled with stock tickers and dataframe data.
div_days_dict = {}
# opening paths and creating dictionaries and dataframes

for path in glob.glob('*.csv'): #searches directory for *csv files
    stock_ticker = path.strip('.csv')  # cleans file path of .csv
    stockmarket.append(stock_ticker) # appends stock names to a list
    stock_dict[stock_ticker] = pd.read_csv(path, usecols=['Date','Close','Adj Close'],index_col='Date') #assigns stock ticker to dictionary key
    stock_dict[stock_ticker].insert(2, 'Close Ratio', stock_dict[stock_ticker]['Close'].shift(+1)/stock_dict[stock_ticker]['Close'])
    stock_dict[stock_ticker].insert(3, 'Adj Close Ratio', stock_dict[stock_ticker]['Adj Close'].shift(+1) / stock_dict[stock_ticker]['Adj Close'])
    stock_dict[stock_ticker].insert(4, stock_ticker + ' Dividend',abs(round((stock_dict[stock_ticker]['Adj Close Ratio'] - stock_dict[stock_ticker]['Close Ratio']), 5)))
    universe = pd.concat(stock_dict,axis=1)   # concatenated axis for each stock ticker to a single dataframe
    div_ser = stock_dict[stock_ticker][stock_ticker + ' Dividend'].loc[stock_dict[stock_ticker][stock_ticker + ' Dividend'] > 0]
    div_days_dict[stock_ticker] = div_ser




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