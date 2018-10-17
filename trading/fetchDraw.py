import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import numpy as np

stock = web.DataReader('MRF.BO', 'yahoo', start = '2016-01-01', end = '2017-01-01')
stock = stock.dropna(how='any')
stock.head()
stock['Adj Close'].plot(grid = True)
stock['ret'] = stock['Adj Close'].pct_change()
stock['ret'].plot(grid=True)
# https://www.quantinsti.com/blog/time-series-analysis-introduction-python/