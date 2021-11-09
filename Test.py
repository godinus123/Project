import mplfinance as mpf

# pip install mplfinance
# pip install bokeh

import datetime
import yfinance as yf
import mplfinance as mpf
from   matplotlib import pyplot as plt

start_Oq = "1999-03-10"
start_Tq = "1999-03-10"
end      = "2021-10-28"

qqq  = yf.download( 'QQQ',start_Oq,end)
tqqq = yf.download('TQQQ',start_Tq,end)

# fig = plt.figure()
# tqqq['Open' ].plot(label ='TQQQ', figsize =(15,7))
# tqqq['Close'].plot(label ='TQQQ', figsize =(15,7))
# tqqq['High' ].plot(label ='TQQQ', figsize =(15,7))
# tqqq['Low'  ].plot(label ='TQQQ', figsize =(15,7))

# plt.grid()
# plt.legend()
# plt.title('Stock Price')
# plt.show(block=False)

df = tqqq
df2 =  qqq


# mpf.plot(df1, type='candle')


# mpf.plot(df1[-100:-1], type='candle', volume=True, figratio=(15, 7), style='yahoo', title='TQQQ, 2020')

# mpf.plot(df[-100:-1], type='candle', volume=True, figratio=(15, 7), style='yahoo', mav=(6, 15), title='Apple, 2020')

  
import plotly.graph_objects as go

candlestick = go.Candlestick(
    x=df.index,
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close']
)

fig1 = go.Figure(data=[candlestick])
fig1.update_layout(xaxis_rangeslider_visible=True)


fig1.update_layout(
    title='Apple Inc stock price',
    yaxis_title='Stock price',
    shapes = [dict(
        x0='2020-03-22', x1='2020-03-22', y0=0, y1=1, xref='x', yref='paper',
        line_width=3)],
    annotations=[dict(
        x='2020-03-27', y=0.05, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='COVID19')]
)


fig1.show()

plt.waitforbuttonpress()

plt.close('all')



from math import pi
from bokeh.plotting import figure
from bokeh.io import output_notebook, show
from bokeh.resources import INLINE

output_notebook(resources=INLINE)
df_ = df[-100:-1].copy()

inc = df_.Close > df_.Open
dec = df_.Open > df_.Close

w = 12*60*60*1000
p = figure(x_axis_type="datetime", plot_width=800, plot_height=500, title = "Apple Inc stock price - 2020")

p.segment(df_.index, df_.High, df_.index, df_.Low, color="black")
p.vbar(df_.index[inc], w, df_.Open[inc], df_.Close[inc], fill_color="lawngreen", line_color="red")
p.vbar(df_.index[dec], w, df_.Open[dec], df_.Close[dec], fill_color="tomato", line_color="lime")

show(p)
