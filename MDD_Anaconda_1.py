# https://datascienceschool.net/03%20machine%20learning/03.02.01%20%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%B2%98%EB%A6%AC%20%EA%B8%B0%EC%B4%88.html
import pandas as pd
import numpy as np
import seaborn as sns
import math

import datetime
import matplotlib.pyplot as plt
from   matplotlib import pyplot as DF
# from   pandas.core.frame import DataFrame
from   pandas_datareader import data as pdr

import yfinance as yf
    
    
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
    
tickerName = 'TQQQ'
yf.pdr_override() # PANDAS download
data = pdr.get_data_yahoo(tickerName); print (data)
# df0  = data.drop(['Volume'],axis=1); print (df0) # Org Data
df0  = data.copy()

for i in range (len(data)) :
    df0.iloc[i,5] = i
    
print(df0)
    
df1=df0.copy();df1.iloc[:,0:4]=df1.iloc[:,0:4]-df1.iloc[:,0:4] # MDD Upside
df2=df0.copy();df2.iloc[:,0:4]=df2.iloc[:,0:4]-df2.iloc[:,0:4] # MDD % data
df3=df0.copy();df3.iloc[:,0:4]=df3.iloc[:,0:4]-df3.iloc[:,0:4] # MDD High Low 1/0
df4=df0.copy();df4.iloc[:,0:4]=df4.iloc[:,0:4]-df4.iloc[:,0:4] # Triange Right Temp 1
df5=df0.copy();df5.iloc[:,0:4]=df5.iloc[:,0:4]-df5.iloc[:,0:4] # Triange Left  Temp 2
df6=df0.copy();df6.iloc[:,0:4]=df6.iloc[:,0:4]-df6.iloc[:,0:4] # (df4 + df5) /2
df7=df0.copy();df7.iloc[:,0:4]=df7.iloc[:,0:4]-df7.iloc[:,0:4] # 
df8=df0.copy();df8.iloc[:,0:4]=df8.iloc[:,0:4]-df8.iloc[:,0:4]
df9=df0.copy();df9.iloc[:,0:4]=df9.iloc[:,0:4]-df9.iloc[:,0:4]


dt3  = df0.copy() ; dt3 = dt3 - dt3 # Triange Right Temp 3
dt4  = df0.copy() ; dt4 = dt4 - dt4 # Triange Left  Temp 4


print (df0.shape,  len(df0),  int(df0.size/len(df0)),   df0.size,  df0.ndim); #print (df_add.shape)
# (2954, 6) 2956 5.0 14765


#1. MDD each : Open High Low Close Adj Close
#2. 1-DAY : max-diff, mean, RaseFall 1/0, 

#1. MDD each : Open High Low Close Adj Close
# Curve
for i in range(1,len(df0)) :
    K=0
    if (df0.iloc[i,K] > df1.iloc[i-1,K]) :
        df1.iloc[i,K] = df0.iloc[i,K] ;        df3.iloc[i,K] = 0
    else :
        df1.iloc[i,K] = df1.iloc[i-1,K] ;      df3.iloc[i,K] = 1
        

#___________________ Percent MDD ______________________________________
# df2.iloc[:,:] = ( df0.iloc[:,:] - df1.iloc[:,:] )/ df1.iloc[:,:]
df2 = abs(( df0 - df1 )/ df1)

for i in range (len(df0)) :
    if (df3.iloc[i-2,K]) and (df3.iloc[i-1,K]) and (df3.iloc[i,K]) and \
       (df3.iloc[i+1,K]) and (df3.iloc[i+2,K]) :
           df4.iloc[i,K] = 1
    else : df4.iloc[i,K] = 0
    
for i in range (len(df0)) :
    if ( df4.iloc[i,K] ) :
        if ( df5.iloc[i,K] >= df2.iloc[i,K].copy() ) :
               df5.iloc[i,K] = df5.iloc[i-1,K].copy()
        else : df5.iloc[i,K] = df2.iloc[i,K].copy()
    else : df5.iloc[i,K] = 0





# for i in range (1, len(df0)-1) :
#     if   (df1.iloc[i+1,K] > df1.iloc[i,K]) and (df1.iloc[i,K] == df1.iloc[i-1,K]) :
#             df3.iloc[i,K] =  1
#     elif (df1.iloc[i-1,K] == df1.iloc[i,K]) and (df1.iloc[i+1,K] > df1.iloc[i,K]) :
#             df3.iloc[i,K] = -1
#     else :  df3.iloc[i,K] =  0

# for i in range (1, len(df0)-1) :
#     if   (df1.iloc[i,K] == df1.iloc[i-1,K]) :
#             df4.iloc[i,K] =  1
#     else :  df4.iloc[i,K] =  0

# Max = 0
# for i in range (1, len(df0)-1) :
#     if ( df3.iloc[i,K] == 1) :
#         for ( j in range(len(df0)) ) :
#             if (i+j) > len(df0) :
#                 break
#             elif df3.iloc[i,K] ==0 :
#                  df5.iloc[i+j,K] = df5.iloc[i+j,K]
#             elif df3.iloc[i,K] == -1 :
                
            
            
    



#     df5.iloc[:,K]   = df5.iloc[:,K] - df5.iloc[:,K]
#     Max = 0         

#     for j in range( 0,200) :
#         if (df3.iloc[i,K] == -1):
#             Max = df5.iloc[:,K].max()
            
#             if ( df4.iloc[i+j,K] == 1) and (df4.iloc[i+j+1,K] == 0) :
#                    DF4_HighLow = 1
#             else : DF4_HighLow = 0
            
#             print("Max = ", i, j, DF4_HighLow, Max)
#             Max = 0
#             # print( "Min = Start.",i )
#             df5.iloc[:,K]   = df5.iloc[:,K] - df5.iloc[:,K]
#             i = i + j -1
#             break
        
#         else :
#             df5.iloc[i+j,K] = df2.iloc[i+j,K]
        
#         if (df3.iloc[i,K] == -1) : break
        
#     if (i+j > len(df0-5)) : 
#         break




    # Max_index = df5.iloc[i:i+loopSize,K].min()
    # print(Max_index)
    # i = i + loopSize - 1


# for i in range(1,len(df0)) :
#     if (df7.iloc[i,K] != 0) :
#         Leap          = int( df6.iloc[i,K] )      # Period value
#         Max_index     = df2.iloc[i:i+Leap,K].idxmax(axis=0,skipna=True)
#         # iMax_index    = int (Max_index)
#         print(Max_index, df2.iloc[i,5])
#         df8.iloc[i,K] = df7.iloc[i,5]


#___________________ Triangle R  ______________________________________
# for i in range(1,len(df0)) :
#     K=0
#     if (df3.iloc[i,K]) :
#             df4.iloc[i,K] = 0
#     else :  df4.iloc[i,K] = df4.iloc[i-1,K] + 1
    
    # K=K+1
    # if (df3.iloc[i,K]) :
    #         df4.iloc[i,K] = 0
    # else :  df4.iloc[i,K] = df4.iloc[i-1,K] + 1
    
    # K=K+1
    # if (df3.iloc[i,K]) :
    #         df4.iloc[i,K] = 0
    # else :  df4.iloc[i,K] = df4.iloc[i-1,K] + 1
    
    # K=K+1
    # if (df3.iloc[i,K]) :
    #         df4.iloc[i,K] = 0
    # else :  df4.iloc[i,K] = df4.iloc[i-1,K] + 1
    
    # K=K+1
    # if (df3.iloc[i,K]) :
    #         df4.iloc[i,K] = 0
    # else :  df4.iloc[i,K] = df4.iloc[i-1,K] + 1
    
#___________________ Triangle L  ______________________________________
# for i in range( (len(df0)-1), 0, -1 ) :
#     K=0
#     if (df3.iloc[i,K]) :
#             df5.iloc[i,K] = 0
#     else :  df5.iloc[i,K] = df5.iloc[i+1,K] + 1
    
    # K=K+1
    # if (df3.iloc[i,K]) :
    #         df5.iloc[i,K] = 0
    # else :  df5.iloc[i,K] = df5.iloc[i+1,K] + 1
    
    # K=K+1
    # if (df3.iloc[i,K]) :
    #         df5.iloc[i,K] = 0
    # else :  df5.iloc[i,K] = df5.iloc[i+1,K] + 1
    
    # K=K+1
    # if (df3.iloc[i,K]) :
    #         df5.iloc[i,K] = 0
    # else :  df5.iloc[i,K] = df5.iloc[i+1,K] + 1
    
    # K=K+1
    # if (df3.iloc[i,K]) :
    #         df5.iloc[i,K] = 0
    # else :  df5.iloc[i,K] = df5.iloc[i+1,K] + 1

#___________________ Triangle Plus Rectangle ___________________________
# df6.iloc[:,:] = round(( df1.iloc[:,:] + df2.iloc[:,:])/2+0.5)
# df6.iloc[:,0:5] = round( (df4.iloc[:,0:5] + df5.iloc[:,0:5])/2 + 0.5 )

# df1 # MDD Upside
# df2 # MDD % data
# df3 # MDD High Low 1/0
# df4 # Triange Right Temp 1
# df5 # Triange Left  Temp 2
# df6 # (df4 + df5) /2
# df7 # 
# df8
# df9

# df4  = df0.copy() ; df4 = df4 - df4 # Triange Right Temp 1
# df5  = df0.copy() ; df5 = df5 - df5 # Triange Left  Temp 2

# K = 0
# for i in range(1,len(df0)) :
#     if (( df3.iloc[i-1,K] == 1 ) and ( df3.iloc[i,K] == 0 )) :
#             df7.iloc[i,K] = 1
#     elif (( df3.iloc[i-1,K] == 0 ) and ( df3.iloc[i,K] == 1 )) :
#                 df7.iloc[i,K] = -1
#     else :  df7.iloc[i,K] = 0

# K = 0
# # Max_index  = 0
# # iMax_index = 0

# print("Max_index, df7.iloc[i,5]")


# K = 0
# for i in range(1,len(df0)-20) :
#     if (df8.iloc[i,K] != 0) :
#         Max_data = int(df8.iloc[i,K])
#         df9.iloc[Max_data,K] = df2.iloc[Max_data,K]

# print("0:4d} 1:6.4f}.format(i, df9.iloc[i,K])" )
# for i in range(1,len(df0)-20) :
#     if (df9.iloc[i,K] != 0) :
#         print("{0:4d} {1:6.4f}".format(i, df9.iloc[i,K]) )

print('The end')

# for i in range(1,len(df0)-1) :
#     K = 0
    
#     if (( df3.iloc[i-1,K] == 1 ) and ( df3.iloc[i,K] == 0 )) :
#         Leap          = int( df6.iloc[i,K] )      # Period value
#         df7.iloc[i,K] = df6.iloc[i,K]
#         Max_index     = df2.iloc[i:i+Leap,K].idxmax(axis=0,skipna=True)
#         df8.iloc[Max_index,K] = df2.iloc[Max_index,K]
        
#         # df7.iloc[Max_index,0] = df2.iloc[Max_index,0]
#         i             = i + Leap - 1
#         # print(Max_index)
#     else :
        # df7.iloc[i,K] = 0
        # df8.iloc[i,K] = 0

        # Leap          = 0      # Period value
        # Max_index     = 1000000
        # df7.iloc[i,0] = 0
        

# dt3.iloc[:,0:5].plot(); 
# plt.yscale("log",nonposy='clip')
# plt.grid()
# plt.title(tickerName)
# plt.xlabel('DataFrame #dt3, Date, View of Hyo Sung Lee, NeoWine')
# plt.ylabel('MDD Clip. log')
# plt.show(block=False)

R = 2900
fig = plt.figure()
df0.iloc[R:,0].plot(); 
plt.yscale("log",nonposy='clip')
plt.grid()
plt.title(tickerName)
plt.xlabel('DataFrame #df0, Date, View of Hyo Sung Lee, NeoWine')
plt.ylabel('MDD Clip. log')
plt.show(block=False)
           
fig = plt.figure()
df1.iloc[R:,0].plot(); 
plt.yscale("log",nonposy='clip')
plt.grid()
plt.title(tickerName)
plt.xlabel('DataFrame #df1, Date, View of Hyo Sung Lee, NeoWine')
plt.ylabel('MDD Clip. log')
plt.show(block=False)

fig = plt.figure()
df2.iloc[R:,0].plot(); 
# plt.yscale("log",nonposy='clip')
plt.grid()
plt.title(tickerName)
plt.xlabel('DataFrame #df2, Date, View of Hyo Sung Lee, NeoWine')
plt.ylabel('MDD Percent')
plt.show(block=False)

fig = plt.figure()
df3.iloc[R:,0].plot(); 
# plt.yscale("log",nonposy='clip')
plt.title(tickerName)
plt.xlabel('DataFrame #df3,Date, View of Hyo Sung Lee, NeoWine')
plt.ylabel('MDD High Low')
plt.grid()
plt.show(block=False)

# Triangle
fig = plt.figure()
df4.iloc[R:,0].plot(); 
# plt.yscale("log",nonposy='clip')
plt.title(tickerName)
plt.xlabel('DataFrame #df4,Date, View of Hyo Sung Lee, NeoWine')
plt.ylabel('MDD High Low')
plt.grid()
plt.show(block=False)

fig = plt.figure()
df5.iloc[R:,0].plot(); 
# plt.yscale("log",nonposy='clip')
plt.title(tickerName)
plt.xlabel('DataFrame #df5,Date, View of Hyo Sung Lee, NeoWine')
plt.ylabel('MDD High Low')
plt.grid()
plt.show(block=False)

# fig = plt.figure()
# df6.iloc[:,0].plot(); 
# # plt.yscale("log",nonposy='clip')
# plt.title(tickerName)
# plt.xlabel('DataFrame #df6, View of Hyo Sung Lee, NeoWine')
# plt.ylabel('MDD High Low')
# plt.grid()
# plt.show(block=False)

# fig = plt.figure()
# df7.iloc[:,0].plot(); 
# # plt.yscale("log",nonposy='clip')
# plt.title(tickerName)
# plt.xlabel('DataFrame #df7, View of Hyo Sung Lee, NeoWine')
# plt.ylabel('MDD High Low')
# plt.grid()
# plt.show(block=False)

# fig = plt.figure()
# df8.iloc[:,0].plot(); 
# # plt.yscale("log",nonposy='clip')
# plt.title(tickerName)
# plt.xlabel('DataFrame #df8, View of Hyo Sung Lee, NeoWine')
# plt.ylabel('MDD High Low')
# plt.grid()
# plt.show(block=False)

# fig = plt.figure()
# df9.iloc[:,0].plot(); 
# # plt.yscale("log",nonposy='clip')
# plt.title(tickerName)
# plt.xlabel('DataFrame #df9, View of Hyo Sung Lee, NeoWine')
# plt.ylabel('MDD High Low')
# plt.grid()
# plt.show(block=False)


plt.waitforbuttonpress()
plt.close()






    # K=K+1
    # if (df0.iloc[i,K] > df1.iloc[i-1,K]) :
    #     df1.iloc[i,K] = df0.iloc[i,K] ;        df3.iloc[i,K] = 1
    # else :
    #     df1.iloc[i,K] = df1.iloc[i-1,K] ;      df3.iloc[i,K] = 0

    # K=K+1
    # if (df0.iloc[i,K] > df1.iloc[i-1,K]) :
    #     df1.iloc[i,K] = df0.iloc[i,K] ;        df3.iloc[i,K] = 1
    # else :
    #     df1.iloc[i,K] = df1.iloc[i-1,K] ;      df3.iloc[i,K] = 0

    # K=K+1
    # if (df0.iloc[i,K] > df1.iloc[i-1,K]) :
    #     df1.iloc[i,K] = df0.iloc[i,K] ;        df3.iloc[i,K] = 1
    # else :
    #     df1.iloc[i,K] = df1.iloc[i-1,K] ;      df3.iloc[i,K] = 0

    # K=K+1
    # if (df0.iloc[i,K] > df1.iloc[i-1,K]) :
    #     df1.iloc[i,K] = df0.iloc[i,K] ;        df3.iloc[i,K] = 1
    # else :
    #     df1.iloc[i,K] = df1.iloc[i-1,K] ;      df3.iloc[i,K] = 0
