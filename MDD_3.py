# pip install mplfinance
# pip install boken
# import pandas_datareader as  web
# import sympy
import pandas as pd
import numpy  as np
import math

import datetime
import matplotlib.pyplot as plt
from   matplotlib import pyplot as DF
from   pandas.core.frame import DataFrame

import mplfinance as mpl
import plotly.graph_objects as go
from   pandas_datareader import data as pdr
import yfinance as yf

start_Oq = "1999-03-10"
# start_Oq = "2010-02-11"
start_Tq = "2010-02-11"
# start_Tq = "2020-02-11"
end      = "2021-10-29"

# tqqq = yf.download('TQQQ')
# ndx  = yf.download('NDX')

tikerName = 'TQQQ'
yf.pdr_override() # PANDAS form download
DF = pdr.get_data_yahoo(tikerName)

# We are going to use a trailing 252 trading day window
#window = 252
window = 22
# fig1 = plt.figure()

# Calculate the max drawdown in the past window days for each day in the series.
# Use min_periods=1 if you want to let the first 252 days data have an expanding window
Roll_Max = DF['Adj Close'].rolling(window, min_periods=1).max()
Daily_Drawdown = DF['Adj Close']/Roll_Max - 1.0

df = DF.drop(['Volume'],axis=1)

# Next we calculate the minimum (negative) daily drawdown in that window.
# Again, use min_periods=1 if you want to allow the expanding window
Max_Daily_Drawdown = Daily_Drawdown.rolling(window, min_periods=1).min()

# Plot the results
Roll_Max.plot()
Max_Daily_Drawdown.plot()
Daily_Drawdown.plot()

# plt.title(tikerName)
# plt.xlabel('Date, View of Hyo Sung Lee, NeoWine')
# plt.ylabel('MDD')
# plt.grid()
# plt.show(block=False)

#________________ Add Slope
# DF.drop(['Volume'],axis=1, inplace=True)
df = DF.drop(['Volume'],axis=1)

df.loc[:,'LoL1'] = 1
df.loc[:,'LoL2'] = 1
df.loc[:,'LoL3'] = 1
df.loc[:,'LoL4'] = 1
print(df.shape, len(df), df.size, df.size/len(df))

LinMin    = df.min();     LinMax    = df.max()
LinMin    = LinMin.min()

LinMaxA0  = LinMax.max()
LinMaxA1  = LinMax.max() + LinMax.max() * 0.23/4
LinMaxA2  = LinMax.max() - LinMax.max() * 0.23/2
LinMaxA3  = LinMax.max() - LinMax.max() * 0.23

# LinMaxA3  = LinMax.max()
LogMaxA0  = math.log(LinMaxA0)
LogMaxA1  = math.log(LinMaxA1)
LogMaxA2  = math.log(LinMaxA2)
LogMaxA3  = math.log(LinMaxA3)

print('Linear Minimum = ',LinMin)
print('Linear Maximum = ',LinMax)
print('Log Maximum    = ',LogMaxA2)

# print(LogMax)
# A = 5.055799799378744
A0 = LogMaxA0
A1 = LogMaxA1
A2 = LogMaxA2
A3 = LogMaxA3

for i in range(len(df)) : 
    df.iloc[i,5] = math.exp((A0/len(df))*i)

for i in range(len(df)) : 
    if ( np.min( df.iloc[i,:] ) < 1 ):
        df.iloc[i,:] = 1

# print(df)
# Log slope calc.
# fig2 = plt.figure()
Start = 1225
Delta = 70 
StartN1 = Start - Delta
StartN2 = Start
StartN3 = Start + Delta

for i in range(len(df)) :
    if (i < (StartN3)) :
        df.iloc[i,6:8] = 1
    else :
        df.iloc[i,6] = math.exp ( A1/ ( len(df) - StartN1 )* (i-StartN1 ) )
        df.iloc[i,7] = math.exp ( A2/ ( len(df) - StartN2 )* (i-StartN2 ) )
        df.iloc[i,8] = math.exp ( A3/ ( len(df) - StartN3 )* (i-StartN3 ) )

plt.plot(df.iloc[:,:]) 
plt.yscale("log")
plt.title(tikerName)
plt.xlabel('Date, View of Hyo Sung Lee, NeoWine')
plt.ylabel('Stock Price. log')
plt.grid()
plt.show(block=False)
# plt.show(block=True)

#############################################
# MDD Plus
df.loc[:,'mOpen'  ] = 1
df.loc[:,'mClose' ] = 1
df.loc[:,'mHigh'  ] = 1
df.loc[:,'mLow'   ] = 1
df.loc[:,'mAClose'] = 1
print(df.shape, len(df), df.size, df.size/len(df))

df.loc[:,'HLO'    ] = 1
df.loc[:,'HLC'    ] = 1
df.loc[:,'HLH'    ] = 1
df.loc[:,'HLL'    ] = 1
df.loc[:,'HLA'    ] = 1
print(df.shape, len(df), df.size, df.size/len(df))

df.loc[:,'MDOpen'  ] = 1
df.loc[:,'MDClose' ] = 1
df.loc[:,'MDHigh'  ] = 1
df.loc[:,'MDLow'   ] = 1
df.loc[:,'MDAclose'] = 1
print(df.shape, len(df), df.size, df.size/len(df))

for i in range(1,len(DF)) :
    K=0; L=9; H=14 # Open
    if ( df.iloc[i,K] > df.iloc[i-1,L] ) :
           df.iloc[i,L] = df.iloc[i,K]
           df.iloc[i,H] = 1 
    else : 
           df.iloc[i,L] = df.iloc[i-1,L]
           df.iloc[i,H] = 0 

    K=K+1; L=L+1; H=H+1  # Close
    if ( df.iloc[i,K] > df.iloc[i-1,L] ) :
           df.iloc[i,L] = df.iloc[i,K]
           df.iloc[i,H] = 1 
    else : 
           df.iloc[i,L] = df.iloc[i-1,L]
           df.iloc[i,H] = 0 
        
    K=K+1; L=L+1; H=H+1  # High
    if ( df.iloc[i,K] > df.iloc[i-1,L] ) :
           df.iloc[i,L] = df.iloc[i,K]
           df.iloc[i,H] = 1 
    else : 
           df.iloc[i,L] = df.iloc[i-1,L]
           df.iloc[i,H] = 0 
        
    K=K+1; L=L+1; H=H+1  # Low
    if ( df.iloc[i,K] > df.iloc[i-1,L] ) :
           df.iloc[i,L] = df.iloc[i,K]
           df.iloc[i,H] = 1 
    else : 
           df.iloc[i,L] = df.iloc[i-1,L]
           df.iloc[i,H] = 0 

    K=K+1; L=L+1; H=H+1  # Adj Close
    if ( df.iloc[i,K] > df.iloc[i-1,L] ) :
           df.iloc[i,L] = df.iloc[i,K]
           df.iloc[i,H] = 1 
    else : 
           df.iloc[i,L] = df.iloc[i-1,L]
           df.iloc[i,H] = 0 
         
# High Low Show
# fig3 = plt.figure()
# plt.yscale("log")
# plt.grid()
# plt.show(block=False)

# fig4 = plt.figure()
ax=df.iloc[:,0: 4].plot()
# plt.yscale("log")
# plt.grid()

df.iloc[:,5:14].plot(ax=ax)
plt.yscale("log")
plt.grid()
plt.show(block=False)

for i in range(0,len(DF)) :
    M=19; K=0; L=9 
    df.iloc[i,M] = 1 - abs( ( df.iloc[i,K] - df.iloc[i,L] )/ df.iloc[i,L] )
    
    M=M+1; K=K+1; L=L+1
    df.iloc[i,M] = 1 - abs( ( df.iloc[i,K] - df.iloc[i,L] )/ df.iloc[i,L] )

    M=M+1; K=K+1; L=L+1
    df.iloc[i,M] = 1 - abs( ( df.iloc[i,K] - df.iloc[i,L] )/ df.iloc[i,L] )

    M=M+1; K=K+1; L=L+1
    df.iloc[i,M] = 1 - abs( ( df.iloc[i,K] - df.iloc[i,L] )/ df.iloc[i,L] )

    M=M+1; K=K+1; L=L+1
    df.iloc[i,M] = 1 - abs( ( df.iloc[i,K] - df.iloc[i,L] )/ df.iloc[i,L] )


# fig3 = plt.figure()
ax = df.iloc[:,15:19].plot()
df.iloc[:,20:24].plot(ax=ax)
plt.grid()
plt.title(tikerName)
plt.xlabel('Date, View of Hyo Sung Lee, NeoWine')
plt.ylabel('MDD Open')
plt.show(block=True)

# cls_Count = MDD_HighLow_cls ;
# for i in range(len(df))
#   if ( MDD_HighLow_cls(i) ) 
#         clsCount(i) = 0;
#   else  clsCount(i) = clsCount(i) + 1 ; endif
# end


plt.waitforbuttonpress()
plt.close('all')

