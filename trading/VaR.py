import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm
import fix_yahoo_finance as yf
from tabulate import tabulate

df = yf.download('FB', '2018-01-01', '2019-01-01')
df = df[['Close']]
df['returns'] = df.Close.pct_change()
mean = np.mean(df['returns'])
std_dev = np.std(df['returns'])

# df['returns'].hist(bins=40, normed=True, histtype='stepfilled', alpha=0.5)
# x = np.linspace(mean - 3*std_dev, mean+3*std_dev, 100)
# plt.plot(x, mlab.normpdf(x, mean, std_dev),'r')
# plt.show( )

Var_90 = norm.ppf(1-0.9, mean, std_dev)
Var_95 = norm.ppf(1-0.95, mean, std_dev)
Var_99 = norm.ppf(1-0.99, mean, std_dev)

print(tabulate([['90%', Var_90], ['95%', Var_95], ['99%', Var_99]] , headers=['Confidence Level', 'Value at Risk']))

#https://www.quantinsti.com/blog/calculating-value-at-risk-in-excel-python/
