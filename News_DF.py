from gnews import GNews
import pandas as pd

googlenews = GNews()
googlenews.start_date = (2021, 1, 1)
goldnews = googlenews.get_news('XAUUSD')
oilnews = googlenews.get_news('brent oil')
usdnews = googlenews.get_news('USD index')
df_gold = pd.DataFrame.from_dict(goldnews)
df_oil = pd.DataFrame.from_dict(oilnews)
df_usd = pd.DataFrame.from_dict(usdnews)

frames = [df_gold, df_oil, df_usd]
df = pd.concat(frames)

print(df)