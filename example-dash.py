import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
df = pd.read_csv(
   'https://gist.githubusercontent.com/chriddyp/'
   'c78bf172206ce24f77d6363a2d754b59/raw/'
   'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
   'usa-agricultural-exports-2011.csv')
def generate_table(dataframe, max_rows=10):
   return html.Table(
      # Header
      [html.Tr([html.Th(col) for col in dataframe.columns])] +
      # Body
      [html.Tr([
         html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
      ]) for i in range(min(len(dataframe), max_rows))]
   )
app = dash.Dash()
colors = {
   'background': '#87D653',
   'text': '#ff0033'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
   html.H1(
      children='Hello Dash',
      style={
         'textAlign': 'center',
         'color': colors['text']
      }
   ),
	
   html.Div(children='Dash: A web application framework for Python.', style={
      'textAlign': 'center',
      'color': colors['text']
   }),
	
   dcc.Graph(
      id='example-graph-2',

      figure={
         'data': [
            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Delhi'},
            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Mumbai'},
         ],
         'layout': {
            'plot_bgcolor': colors['background'],
            'paper_bgcolor': colors['background'],
            'font': {
               'color': colors['text']
            }
         }
      }
   )
]
                      html.Div(children=[
   html.H4(children='US Agriculture Exports (2011)'),
   generate_table(df)
])
if __name__ == '__main__':
   app.run_server()
