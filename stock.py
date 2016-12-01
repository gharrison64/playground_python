#!/usr/bin/env python3
'''
Created on Nov 28, 2016

@author: gchiles
'''
import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import Series
import matplotlib.pyplot as plt
from dateutil import parser
from tkinter.constants import BOTH

#Set PANDAS to show all columns in DataFrame
pd.set_option('display.max_columns', None)

data_from_csv = pd.read_csv('data/WIKI-FB.csv')
#print (data_from_csv.columns)

mydates     = []
open_price  = []
high_price  = []
low_price   = []
close_price = []
volume      = []

for index, row in data_from_csv.iterrows():
        mydates.append(row[0])
        open_price.append(row[1])
        high_price.append(row[2])
        low_price.append(row[3])
        close_price.append(row[4])
        volume.append(row[5])

x = [parser.parse(d) for d in mydates]
y = open_price
#print(x)

#print(avgr_list)
avg_ = np.average(open_price)
#print(avg_)

avg_list = [avg_ for i in range(len(x))]

#Ok let's plot the data.
plt.title("StockPrices")
plt.xlabel('Dates')
plt.ylabel('Price')
plt.grid(axis=BOTH)
plt.plot(x,open_price)
plt.plot(x,close_price)
plt.plot(x,avg_list)
plt.show()
