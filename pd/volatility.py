## Computing Volatility

# Load the required modules and packages
import numpy as np
import pandas as pd
# import pandas.io.data as web
import json
from pandas.io.json import json_normalize

# Pull NIFTY data from Yahoo finance 
# NIFTY = web.DataReader('^NSEI',data_source='yahoo',start='6/1/2012', end='6/1/2016')
s = open('./trxo.json').read()
dl = json.loads(s)
df= json_normalize(dl)
df = df.drop_duplicates("timestamp.$numberLong")

import datetime as datetime 
def parse_time(st):
    return datetime.datetime.fromtimestamp(float(st)/1000)

df = df.sort_values("timestamp.$numberLong")

df['Date'] =  parse_time(df['timestamp.$numberLong'])
df = df.set_index("Date")


# NIFTY_datetime = [parse_time(i['timestamp']['$numberLong']) for i in  NIFTY2] 
# NIFTY_close = [i['close'] for i in  NIFTY2]
# for i in NIFTY2:
#     t = parse_time(i['timestamp']['$numberLong'])  


# ser = pd.Series(NIFTY_close, index = NIFTY_datetime)
# a = ser.resample('5m').last()
# print(a)

# df = pd.DataFrame(NIFTY_close, index = NIFTY_datetime, columns=['Close'])
# df=df.sort_index()

# def fl(arr):
#     print(arr)
#     if(len(arr)>=1) :
#         return arr[len(arr)-1]
#     return arr

# # Compute the logarithmic returns using the Closing price 
print(df['close'])

df['Volatility'] = df['close'].rolling(10).std()
# print(df)
import matplotlib.pyplot as plt
plt.plot(df['Volatility'])
plt.subplot(2,1,1)
plt.plot(df['Volatility'])
plt.ylabel('Volatility')
plt.subplot(2,1,2)
plt.plot(df['close'])
plt.ylabel('close')
plt.show()
# # Plot the NIFTY Price series and the Volatility
# # df[['Close', 'Volatility']].plot(subplots=True, color='blue',figsize=(8, 6))