import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd
import quandl
import plotly.figure_factory as ff
x_values_1 = ['X8','X7','X6','X5'] 
x_values_2 = ['X4','X3','X2','X1'] 
y_values_1 = [20,15,45,15]
y_values_2 = [-30,-5,-40,-15]
trace_1 = go.Bar(y=x_values_1, x=y_values_1, name="Negative", orientation = 'h', 
	marker=dict(color="rgb(153, 235, 255)",line=dict(color='blue', width=1.5)))
trace_2 = go.Bar(y=x_values_2, x=y_values_2, name="Positive", orientation = 'h', 
	marker=dict(color="rgb(255, 153, 255)",line=dict(color='pink', width=1.5)))

layout1 = dict(    
    title='<b>Correlation with employees probability of churn</b>', 
    yaxis=dict(title='Variable'))
    
data_1 = [trace_1,trace_2]
figure1 = dict(data=data_1,layout=layout1)