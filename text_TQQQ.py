import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from pandas.plotting import scatter_matrix

# pip install yfinance
import yfinance as yf

# matplotlib inline
plt.close('all')

start = "2010-02-11"
end = '2021-10-26'
tqqq = yf.download('TQQQ',start,end)
qld = yf.download('QLD',start,end)
qqq = yf.download('QQQ',start,end)

fig = plt.figure()
tqqq['Open'].plot(label = 'TQQQ', figsize = (15,7))
qld['Open'].plot(label = "QLD")
qqq['Open'].plot(label = 'QQQ')
plt.grid()
plt.legend()
plt.title('Stock Prices of TQQQ, QLD and QQQ')
plt.show()

fig = plt.figure()
tqqq['Volume'].plot(label = 'TQQQ', figsize = (15,7))
qld['Volume'].plot(label = "QLD")
qqq['Volume'].plot(label = 'QQQ')
plt.legend()
plt.title('Volume of Stock traded')
plt.grid()
plt.show()


# Market Capitalisation
fig = plt.figure()
tqqq['MarktCap'] = tqqq['Open'] * tqqq['Volume']
qld['MarktCap'] = qld['Open'] * qld['Volume']
qqq['MarktCap'] = qqq['Open'] * qqq['Volume']
tqqq['MarktCap'].plot(label = 'TQQQ', figsize = (15,7))
qld['MarktCap'].plot(label = 'QLD')
qqq['MarktCap'].plot(label = 'QQQ')
plt.title('Market Cap')
plt.legend()
plt.grid()
plt.show()

fig = plt.figure()
tqqq['MA50'] = tqqq['Open'].rolling(50).mean()
tqqq['MA200'] = tqqq['Open'].rolling(200).mean()
tqqq['Open'].plot(figsize = (15,7))
tqqq['MA50'].plot()
tqqq['MA200'].plot()
plt.legend()
plt.grid()
plt.show()

# fig = plt.figure()
data = pd.concat([tqqq['Open'],qld['Open'],qqq['Open']],axis = 1)
data.columns = ['TQQQOpen','QLDOpen','QQQOpen']
scatter_matrix(data, figsize = (8,8), hist_kwds= {'bins':250})
plt.legend()
plt.grid()
plt.show()

#Volatility
fig = plt.figure()
tqqq['returns'] = (tqqq['Close']/tqqq['Close'].shift(1)) -1
qld['returns'] = (qld['Close']/qld['Close'].shift(1))-1
qqq['returns'] = (qqq['Close']/qqq['Close'].shift(1)) - 1
tqqq['returns'].hist(bins = 100, label = 'TQQQ', alpha = 0.5, figsize = (15,7))
qld['returns'].hist(bins = 100, label = 'QLDy', alpha = 0.5)
qqq['returns'].hist(bins = 100, label = 'QQQ', alpha = 0.5)
plt.legend()
plt.show()



