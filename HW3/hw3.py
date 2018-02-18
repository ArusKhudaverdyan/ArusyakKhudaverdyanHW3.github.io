import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd
import quandl
import plotly.figure_factory as ff


import Graph1
import Graph2 
import Graph3 
import Graph4 
import Graph5   
  
graph1=dcc.Graph(id='Graph1', figure=Graph1.figure1)
graph2=dcc.Graph(id='Graph2', figure=Graph2.figure2)
graph3=dcc.Graph(id='Graph3', figure=Graph3.figure3)
graph4=dcc.Graph(id='Graph4', figure=Graph4.figure4)
graph5=dcc.Graph(id='Graph5', figure=Graph5.fig)


app=dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
app.layout =html.Div([html.H1(children="Homework3"),
	html.Div([

    html.Div([html.H4(children="Graph1"), html.P(children='The graph on the right hand side is showing correlations of different variables (call them from x1 to x8) with employee churn. Data is artificial, manually inputted by the developer. Recreate the graph. Small coloring or corelation value differences will be neglected.')], className='three columns'),
    html.Div([graph1], className='six columns')

    ], className='row'),
html.Div([
    html.Div([html.H4(children="Graph2"),html.P('One the right hand side we have US GDP graphed over time. The data is sourced from QUANDL API (FRED/GDP). Your task is to recreate exactly the same graph.')], className='three columns'),
    html.Div([graph2], className='six columns')

    ], className='row'),
html.Div([
    html.Div([html.H4(children="Graph3 and 4"),html.P('The two graphs on this row are based on Googles stock (WIKI/GOOGL) and Bitcoins (BCHARTS/ABUCOINSUSD) prices sourced from Quandl. First, percentage changes are calculated. Then the latter is plotted using Box plot to find the distribution and outliers. In the end the first 4 percentage changes (apart from the very first one, which is N/A) are plotted in a table. Recreate similar graphs with the same values (minor styling is neglected).')], className='three columns'),
    html.Div([graph3,graph4], className='eight columns')

    ], className='row'),
html.Div([
    html.Div([html.H4(children="Graph5"),html.P('Last graph is based on manually inputted data. It shows the Roadmap developed by an artificial startup. Task 1 is assumed to take the whole Janduary, while Task 2 is starting from March and ending in mid April. Afterwards, Task 3 begins and ends in the end of September. Recreate a similar Roadmap.')], className='three columns'),
    html.Div([graph5], className='six columns')

    ], className='row') 
])







if __name__== '__main__':
    app.run_server(debug=True)
