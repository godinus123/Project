# pip install mplfinance
# pip install boken

import datetime
import yfinance as yf
import mplfinance as mpl
from   matplotlib import pyplot as plt
import plotly.graph_objects as go

start_Oq = "1999-03-10"
start_Tq = "2010-02-11"
end      = "2021-10-29"

qqq  = yf.download( 'QQQ', start_Oq,end)
tqqq = yf.download('TQQQ', start_Tq,end)
df = tqqq

candlestick = go.Candlestick (
    x=df.index,
    open  = df['Open'],
    high  = df['High'],
    low   = df['Low'],
    close = df['Close']
)

def zoom(layout, xrange):
    in_view = df.loc[fig.layout.xaxis.range[0]:fig.layout.xaxis.range[1]]
    fig.layout.yaxis.range = [in_view.High.min() - 10, in_view.High.max() + 10]


fig1 = go.Figure  (data=[candlestick])
fig1.update_layout(xaxis_rangeslider_visible=True)


fig1.update_layout(
    title          = 'TQQQ stock price',
    yaxis_title    = 'Stock Price',
    yaxis_type     = 'log',
    
    shapes         = [dict(
        x0         = start_Tq, x1=end, y0=0, y1=1, 
        xref       ='x', 
        yref       ='paper',
        line_width = 3 )],
    
    annotations = ([dict(
        x          = '2020-03-27', 
        y          = 0.05, 
        xref       = 'x',
        yref       = 'paper',
        showarrow  = False, 
        xanchor    = 'left', 
        text       = 'COVID19' )])
)
fig1.update_xaxes(showgrid=True, linewidth=2, 
                  linecolor="black",gridcolor="blue")
fig1.update_yaxes(showgrid=True, linewidth=2,
                  linecolor="black",gridcolor="Green")

fig1.show()

# df = tqqq
# def zoom(layout, xrange):
#     in_view = df.loc[fig.layout.xaxis.range[0]:fig.layout.xaxis.range[1]]
#     fig.layout.yaxis.range = [in_view.High.min() - 10, in_view.High.max() + 10]


# fig2 = go.Figure(data=[candlestick])
# fig2.update_layout(xaxis_rangeslider_visible=True)


# fig2.update_layout(
#     title          = 'TQQQ stock price',
#     yaxis_title    = 'Stock Price',
#     yaxis_type     = 'log',
    
#     shapes         = [dict(
#         x0         = start_Tq, x1=end, y0=0, y1=1, 
#         xref       ='x', 
#         yref       ='paper',
#         line_width = 3 )],
    
#     annotations = ([dict(
#         x          = '2020-03-27', 
#         y          = 0.05, 
#         xref       = 'x',
#         yref       = 'paper',
#         showarrow  = False, 
#         xanchor    = 'left', 
#         text       = 'COVID19' )])
# )
# fig2.update_xaxes(showgrid=True, linewidth=2, 
#                   linecolor="black",gridcolor="blue")
# fig2.update_yaxes(showgrid=True, linewidth=2,
#                   linecolor="black",gridcolor="Green")

# fig2.show()


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



