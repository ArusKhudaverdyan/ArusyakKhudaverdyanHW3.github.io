import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd
import quandl
import plotly.figure_factory as ff
header = dict(values=['Google','BitCoin'],
              align = ['left','center'],
              font = dict(color = '#ffb3e6', size = 12),
              fill = dict(color='#119DFF')
             )
cells = dict(values=[round(data1.Open.pct_change().head()[1:],3), round(data2.Open.pct_change().head()[1:],3)], 
             align = ['left','center'], fill = dict(color=["yellow","white"]) 
             )
            
trace = go.Table(header=header, cells=cells)

data_4 = [trace]
layout4 = dict(width=500, height=300)
figure4 = dict(data=data_4, layout=layout4)