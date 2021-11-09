# pip install mplfinance

import datetime
from bokeh.models import annotations
import yfinance as yf
import mplfinance as mpf
from   matplotlib import pyplot as plt

start_Oq = "1999-03-10"
start_Tq = "1999-03-10"
end      = "2021-10-28"

qqq  = yf.download( 'QQQ',start_Oq,end)
tqqq = yf.download('TQQQ',start_Tq,end)

df1 = tqqq
df2 =  qqq

import plotly.graph_objects as go

df = tqqq
candlestick = go.Candlestick(
    x=df.index,
    open  = df['Open'],
    high  = df['High'],
    low   = df['Low'],
    close = df['Close']
)

fig = go.Figure(data=[candlestick])
fig.update_yaxes(title_text='Number of cases')
fig.update_layout(
    xaxis_rangeslider_visible=True,
    # xaxis_type="log", 
    yaxis_type="log",
    title = 'TQQQ Price',
    yaxis_title = 'Stock price',
    
    shapes = [dict(
        x0= '2020-03-22', x1='2020-03-22', y0=0, y1=1, xref='x',yref='paper',
        line_width=3)],
    annotations=[dict(
        x='2020-03-27', y=0.05, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='COVID19')]
)

# plt.show(block=False)
fig.show(block=False)
plt.waitforbuttonpress()
plt.close('all')






