import yfinance as yf
import pandas as pd
from sklearn import preprocessing
import matplotlib.pyplot as plt

df = yf.download(['GC=F', 'CL=F', 'DX-Y.NYB'], start='2021-01-01', group_by='ticker')
df = df.rename(columns={"GC=F":"GOLD", "CL=F":"OIL", "DX-Y.NYB":"USD"})
df.fillna(value=df.mean(), inplace=True)

normal_gold = (df.GOLD.Close - df.GOLD.Close.mean())/df.GOLD.Close.std()
normal_usd = (df.USD.Close - df.USD.Close.mean())/df.USD.Close.std()
normal_oil = (df.OIL.Close - df.OIL.Close.mean())/df.OIL.Close.std()

plt.plot(normal_gold, color='yellow')
plt.xticks(rotation='vertical')
plt.plot(normal_usd, color='green')
plt.xticks(rotation='vertical')
plt.plot(normal_oil, color='black')
plt.xticks(rotation='vertical')
plt.show()