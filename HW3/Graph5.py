import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd
import quandl
import plotly.figure_factory as ff
df = [dict(Task="Task 1", Start='2018-01-01', Finish='2018-01-31', Resource='Idea Validation'),
      dict(Task="Task 2", Start='2018-03-05', Finish='2018-04-15', Resource='Prototyping'),
      dict(Task="Task 3", Start='2018-04-20', Finish='2018-09-30', Resource='Team Formation')]

colors = ['#0033cc', '#009933', '#e68a00']

fig = ff.create_gantt(df, colors=colors, index_col='Resource', reverse_colors=True, show_colorbar=True, title="Startup Roadmap")
