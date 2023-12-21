import pandas as pd
import yfinance as yf
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

crypto = ['BTC-USD', 'ETH-USD', 'XRP-USD', 'SOL-USD', 'ADA-USD', 'AVAX-USD', 'DOGE-USD', 'TRX-USD', 'DOT-USD', 'LINK-USD', 'MATIC-USD', 'SHIB-USD', 'LTC-USD', 'BCH-USD', 'ATOM-USD', 'XLM-USD', 'OKB-USD', 'XMR-USD', 'ETC-USD', 'ICP-USD', 'HBAR-USD', 'CRO-USD', 'INJ-USD', 'NEAR-USD', 'FIL-USD', 'VET-USD', 'LDO-USD', 'OP-USD', 'RUNE-USD', 'ALGO-USD', 'RNDR-USD', 'FTT-USD', 'EGLD-USD', 'AAVE-USD', 'QNT-USD', 'SNX-USD', 'MKR-USD', 'FTM-USD', 'FLOW-USD', 'SAND-USD']
df = pd.DataFrame(index=crypto, columns=range(100))
for i in range(len(df)):
    price = yf.download(crypto[i], period='100d').Close.values
    df.iloc[i] = price

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
kmeans = KMeans(n_clusters=3)
kmeans.fit(df_scaled)
labels = kmeans.labels_
df['Cluster'] = labels

print(df)