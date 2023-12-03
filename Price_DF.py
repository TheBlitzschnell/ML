import yfinance as yf
import pandas as pd

df = yf.download(['GC=F', 'CL=F', 'DX-Y.NYB'], start='2021-01-01', group_by='ticker')
df = df.rename(columns={"GC=F":"GOLD", "CL=F":"OIL", "DX-Y.NYB":"USD"})
df.fillna(value="null", inplace=True)

print(df)