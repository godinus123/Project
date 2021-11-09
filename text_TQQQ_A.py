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
end = '2021-10-27'
tqqq = yf.download('TQQQ',start,end)
upro = yf.download('UPRO',start,end)
fngu = yf.download('FNGU',start,end)

fig = plt.figure()
tqqq['Open'].plot(label = 'TQQQ', figsize = (15,7))
upro['Open'].plot(label = 'UPRO')
fngu['Open'].plot(label = 'FNGU')
plt.grid()
plt.legend()
plt.title('Stock Prices of TQQQ, UPRO and QQQ')
plt.show(block=False)

fig = plt.figure()
tqqq['Volume'].plot(label = 'TQQQ', figsize = (15,7))
upro['Volume'].plot(label = 'UPRO')
fngu['Volume'].plot(label = 'FNGU')
plt.legend()
plt.title('Volume of Stock traded')
plt.grid()
plt.show(block=False)


# Market Capitalisation
fig = plt.figure()
tqqq['MarktCap'] = tqqq['Open'] * tqqq['Volume']
upro['MarktCap'] = upro['Open'] * upro['Volume']
fngu['MarktCap'] = fngu['Open'] * fngu['Volume']
tqqq['MarktCap'].plot(label = 'TQQQ', figsize = (15,7))
upro['MarktCap'].plot(label = 'UPRO')
fngu['MarktCap'].plot(label = 'FNGU')
plt.title('Market Cap')
plt.legend()
plt.grid()
plt.show(block=False)

fig = plt.figure()
tqqq['MA50'] = tqqq['Open'].rolling(50).mean()
tqqq['MA200'] = tqqq['Open'].rolling(200).mean()
tqqq['Open'].plot(figsize = (15,7))
tqqq['MA50'].plot()
tqqq['MA200'].plot()
plt.legend()
plt.grid()
plt.show(block=False)

# fig = plt.figure()
data = pd.concat([tqqq['Open'],upro['Open'],fngu['Open']],axis = 1)
data.columns = ['TQQQOpen','UPROOpen','FNGUOpen']
scatter_matrix(data, figsize = (8,8), hist_kwds= {'bins':250})
plt.legend()
plt.grid()
plt.show(block=False)

#Volatility
fig = plt.figure()
tqqq['returns'] = (tqqq['Close']/tqqq['Close'].shift(1)) -1
upro['returns'] = (upro['Close']/upro['Close'].shift(1)) -1
fngu['returns'] = (fngu['Close']/fngu['Close'].shift(1)) -1
tqqq['returns'].hist(bins = 100, label = 'TQQQ', alpha = 0.5, figsize = (15,7))
upro['returns'].hist(bins = 100, label = 'UPRO', alpha = 0.5)
fngu['returns'].hist(bins = 100, label = 'FNGU', alpha = 0.5)
plt.legend()
plt.show(block=False)

plt.waitforbuttonpress()

plt.close('all')

