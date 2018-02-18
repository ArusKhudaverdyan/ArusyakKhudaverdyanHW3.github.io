import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd
import quandl
import plotly.figure_factory as ff
quandl.ApiConfig.api_key = "Z2sSmytWEmYixSoCD-yN"
data3 = quandl.get("FRED/GDP")

data_2=[go.Scatter(x=data3.index, y=data3.Value, fill ='tozeroy')
                 ]
layout2=dict(title="<b>US GDP Over Time</b>")
figure2 = dict(data=data_2, layout=layout2)