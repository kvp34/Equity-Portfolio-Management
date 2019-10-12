import numpy as np
import pandas as pd
import glob as glob

# create empty structures
stockmarket = [] #empty list to be filled with stock tickers
stock_dict ={}   #empty dict to be filled with stock tickers and dataframe data.

for path in glob.glob('*.csv'): #searches directory for *csv files
    cleaned_path = path.strip('.csv')  # cleans file path of .csv
#     print(cleaned_path) #test
    stockmarket.append(cleaned_path) # appends stock names to a list
    stock_dict[cleaned_path] = pd.read_csv(path)

    #     print(csvtodf) #test
print(stock_dict)







# Want to pass stockmarket tickers as keys for dataframe.
# looking for variable variables, variable dictonary keys.. see the following links
# https://stackoverflow.com/questions/3972872/python-variables-as-keys-to-dict
# https://stackoverflow.com/questions/40482738/how-to-name-dataframe-with-variables-in-pandas
# https://www.php.net/manual/en/language.variables.variable.php
#https://stackoverflow.com/questions/1373164/how-do-i-create-a-variable-number-of-variables
# see dict comprehension?
#https://stackoverflow.com/questions/20489609/dictionary-comprehension-in-python-3
#https://www.datacamp.com/community/tutorials/python-dictionary-comprehension
#https://stackoverflow.com/questions/46950173/python-looping-through-directory-and-saving-each-file-using-filename-as-data-fr
