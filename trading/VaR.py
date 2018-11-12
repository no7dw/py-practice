import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn 
import matplotlib.mlab as mlab

from scipy.stats import norm

import fix_yahoo_finance as yf

from tabulate import tabulate

df = yf.download('FB', '2012-01-01', '2018-01-01')
df = df[['Close']]
df['returns'] = df.Close.pct_change()
mean = np.mean(df['returns'])
std_dev = np.std(df['returns'])

#https://www.quantinsti.com/blog/calculating-value-at-risk-in-excel-python/
