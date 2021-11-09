#!pip install yfinance
#!pip install mplfinance
from datetime import datetime
import yfinance as yf
import mplfinance as mpf
from matplotlib import pyplot as plt
import plotly.graph_objects as go


start_date = datetime(2010, 2, 11)
end_date   = datetime(2021,10, 27)

data = yf.download('TQQQ', start=start_date, end=end_date)
mpf.plot(data,type='candle',mav=(3,6,9),volume=True,show_nontrading=True)


# Data reading and processing steps omitted

# fig, axlist = mpf.plot(data, type='line', returnfig=True)
fig, axlist = mpf.plot(data, type='candle', returnfig=True)
ax = axlist[0]
ax.set_yscale('log')
plt.grid()
plt.show(block=False)

plt.waitforbuttonpress()
plt.close('all')

# plt.waitforbuttonpress()
 #mpf.plot.close('all')
 
# import plotly.graph_objects as go
# df = yf.download('TQQQ', start=start_date, end=end_date)

# candle = go.Candlestick(
# 	x=df.index,
# 	open=df['Open'],
# 	high=df['High'],
# 	low=df['Low'],
# 	close=df['Close'],
# 	increasing_line_color='red', # 상승봉
# 	decreasing_line_color='blue' # 하락봉
# )
# ch = go.Figure(data=candle)
# ch.update_layout(xaxis_rangeslider_visible=False)
# ch.show()


