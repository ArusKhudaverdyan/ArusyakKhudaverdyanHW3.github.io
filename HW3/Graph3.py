import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd
import quandl
import plotly.figure_factory as ff
quandl.ApiConfig.api_key = "Z2sSmytWEmYixSoCD-yN"
data1=quandl.get("WIKI/AAPL")
data2=quandl.get("BCHARTS/ABUCOINSUSD")

BitCoin = go.Box(x=data1.Open.pct_change(), name='BitCoin')
Google = go.Box(x=data2.Open.pct_change(),name='Google')
layout3=dict(title="Distribution of Price Change")
data_3 = [BitCoin,Google]
figure3 = dict(data=data_3, layout=layout3)