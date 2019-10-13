import numpy as np
import pandas as pd
import glob as glob

# create empty structures
stockmarket = [] #empty list to be filled with stock tickers
stock_dict ={}   #empty dict to be filled with stock tickers and dataframe data.
universe = pd.DataFrame()


for path in glob.glob('*.csv'): #searches directory for *csv files
    stick_ticker = path.strip('.csv')  # cleans file path of .csv
    stockmarket.append(stick_ticker) # appends stock names to a list
    stock_dict[stick_ticker] = pd.read_csv(path, usecols=['Close','Adj Close']) #assigns stock ticker to dictionary key
    universe = pd.concat(stock_dict,axis=1)   # concatenated axis for each stock ticker to a single dataframe

# Midterm Directions #1:
# Starting on jan 2 , buy 1 mil of each of these stocks: ['IBM', 'MSFT', 'GOOG', 'AAPL',
# 'AMZN' must buy a whole number of stocks
# remainder of money is left as cast earning zero percent. Add ability toearn interest
# The value of your holdings and cash is defined by the MTM equation
# MTM = cash + sum(shares * close price)
'/n'



# Midterm Directions
    # make the day you rebalance a variable to simplify
    # finding the optimal number of days before rebalancing
    # See Direction #9
'/n'
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
'/n'

#  Dividends:
    # Assumption: dividend days are defined from HW#2
    # On dividend days you get a return on stocks held.
    # dividend return defined as dividend = ($1.5x#of shares of stock)
    # stocks bought on dividend day do not qualify for dividend
    # stocks sold on dividend day do qualify for dividend
    # dividend is deposited to cash accound
    # #
'/n'

# Plotting:
    # created a High Tech Index of the daily averages of the 10 stocks Close price
    # compare MTM to High tech index and plot curves
    # suggestion: to plot curves together convert the series to daily percentage
    # daily percent change with regard to beinging of year
    # #
'/n'

# Convert to JPY
    # convert your MTM to JPY using Close column
    # plot JPY to USD MTM
    # Convert daily percentage change as well... daily percent change should be same...
    # #
'/n'