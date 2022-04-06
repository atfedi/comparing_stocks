from matplotlib import pylab as plt
import pandas as pd

df1 = pd.read_csv("NKE.csv")
print(df1.head())
df2 = pd.read_csv("PUM.DE.csv")
print(df2.head())
df3 = pd.read_csv("ADS.DE.csv")
print(df3.head())

df1['Date'] = pd.to_datetime(df1.Date)
df2['Date'] = pd.to_datetime(df2.Date)
df3['Date'] = pd.to_datetime(df3.Date)

#mean1 = df1["Close"].mean()
#mean2 = df2["Close"].mean()
#mean3 = df3["Close"].mean()


plt.figure("Nike, Adidas, and Puma Stocks")
plt.plot(df1["Date"], df1["Close"], label = "NKE Stock Price")
plt.plot(df2["Date"], df2["Close"], label = "PUM.DE Stock Price")
plt.plot(df3["Date"], df3["Close"], label = "ADS.DE Stock Price")
plt.xlabel("Years")
plt.legend(loc = "upper left")
plt.show()
