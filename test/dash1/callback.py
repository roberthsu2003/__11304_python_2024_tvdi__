from dash import Dash,html,dcc,Input,Output,callback
import pandas as pd
import plotly.express as px

app1 = Dash(__name__,requests_pathname_prefix="/dash1/callback/")

df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')

app1.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                df['Indicator Name'].unique(),
                'Fertility rate, total (births per woman)',
                id='xaxis-column'
            ),
            dcc.RadioItems(
                ['Linear','Log'],
                'Linear',
                id = 'xaxis-type',
                inline=True
            )
        ],style={'width':'48%','display':'inline-block'}),
        html.Div([
            dcc.Dropdown(
                df['Indicator Name'].unique(),
                'Life expectancy at birth, total (years)',
                id='yaxis-column'
            ),
            dcc.RadioItems(
                ['Linear','Log'],
                'Linear',
                id = 'yaxis-type',
                inline=True
            )
        ],style={'width':'48%','float':'right','display':'inline-block'})
    ]),
    dcc.Graph(id='indicator-graphic'),
    dcc.Slider(
        min=df['Year'].min(),
        max=df['Year'].max(),
        step=None,
        id='year--slider',
        value=df['Year'].max(),
        marks = {str(year):str(year) for year in df['Year'].unique()}
    )

])

@callback(
    Output('indicator-graphic','figure'),
    Input('xaxis-column','value'),
    Input('yaxis-column','value'),
    Input('xaxis-type','value'),
    Input('yaxis-type','value'),
    Input('year--slider','value')   
)
def update_graph(xaxis_column_name,
                 yaxis_column_name,
                 xaxis_type,
                 yaxis_type,
                 year_value
                 ):
    dff = df[df['Year'] == year_value]
    xValue = dff[dff['Indicator Name'] == xaxis_column_name]['Value']
    yValue = dff[dff['Indicator Name'] == yaxis_column_name]['Value']
    hoverValue = dff[dff['Indicator Name'] == yaxis_column_name]['Country Name']
    fig = px.scatter(
                x=xValue,
                y=yValue,
                hover_name=hoverValue)
    
    fig.update_layout(margin={'l':40, 'b':40, 't':10, 'r':0},
                      hovermode='closest')
    
    fig.update_xaxes(title=xaxis_column_name,
                     type='linear' if xaxis_type == 'Linear' else 'log')
    
    fig.update_yaxes(title=yaxis_column_name,
                     type='linear' if yaxis_type == 'Linear' else 'log')
    return fig

    

