# import pandas as pd
import numpy  as np
import sympy
import math

# import pandas_datareader as  web
import matplotlib.pyplot as plt
import datetime
# pip install mplfinance
# pip install boken
import datetime
import yfinance as yf
import mplfinance as mpl
from   matplotlib import pyplot as DF
import plotly.graph_objects as go

start_Oq = "1999-03-10"
# start_Oq = "2010-02-11"
start_Tq = "2010-02-11"
# start_Tq = "2020-02-11"

end      = "2021-10-29"

qqq  = yf.download( 'QQQ', start_Oq,end)
# tqqq = yf.download('TQQQ', start_Tq,end)
tqqq = yf.download('TQQQ')
# ndx  = yf.download('NDX')


# Get SPY data for past several years
# DF = web.DataReader('SPY', 'yahoo', datetime.date(2007,1,1))
DF = tqqq
tikerName = 'TQQQ'

# We are going to use a trailing 252 trading day window
#window = 252
window = 10
fig1 = plt.figure()

# Calculate the max drawdown in the past window days for each day in the series.
# Use min_periods=1 if you want to let the first 252 days data have an expanding window
Roll_Max = DF['Adj Close'].rolling(window, min_periods=1).max()
Daily_Drawdown = DF['Adj Close']/Roll_Max - 1.0

# Next we calculate the minimum (negative) daily drawdown in that window.
# Again, use min_periods=1 if you want to allow the expanding window
Max_Daily_Drawdown = Daily_Drawdown.rolling(window, min_periods=1).min()

# Plot the results
Daily_Drawdown.plot()
Max_Daily_Drawdown.plot()

plt.title(tikerName)
plt.xlabel('Date')
plt.ylabel('MDD')

plt.grid()
plt.show(block=False)


fig2 = plt.figure()
plt.plot(DF['Close']) 
plt.yscale("log")
plt.title(tikerName)
plt.xlabel('Date')
plt.ylabel('Stock Price. log')
plt.grid()
plt.show(block=False)

#________________ Add Slope
print(DF.min())
# print(math.log(155.16)-math.log(0.7558))
# A = 5.3244
A = 5.0 
for i in range(len(DF)) : 
    DF.iloc[i,5] = math.exp((A/len(DF))*i)
    # DF.iloc[i,6] = 1

for i in range(len(DF)) : 
    if ( np.min( DF.iloc[i,1:6] ) < 1 ):
        DF.iloc[i,0:6] = 1

DS = DF.iloc[:,0:6]

fig3 = plt.figure()
plt.plot(DS.iloc[:,0:6]) 
plt.yscale("log")
plt.title(tikerName)
plt.xlabel('Date')
plt.ylabel('Stock Price. log')
plt.grid()
plt.show(block=False)

plt.waitforbuttonpress()
plt.close('all')

# 11x10 리스트를 생성합니다.  = (11열 10행) 
# (column : 열  row : 행)   , 열은 세로줄, 행은 가로줄입니다.
array_2 = [[0 for col in range(11)] for row in range(10)]
# array_2[3][1] = 1

for y in range(len(DF)) :
    for x in range(len(DF)) :
        array_2[y][x] = y*1000+x

print(array_2)



