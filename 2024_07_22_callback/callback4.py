from dash import Dash, dcc, html, Input, Output, callback

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__,external_stylesheets=external_stylesheets)

all_options = {
    '美國':['New York City', 'San Francisco', 'Cincinnati'],
    '加拿大':['Montreal', 'Toronto', 'Ottawa']
}

app.layout = html.Div([
    dcc.RadioItems(
        list(all_options.keys()),
        '美國',
        id='countries-radio'
    ),
    html.Hr(),
    dcc.RadioItems(id='cities-radio'),
    html.Div(id='display-selected-values')
])

@callback(
    Output('cities-radio','options'),
    Input('countries-radio','value')
)
def set_cities_options(selected_country:str):
    return [{'label':i, 'value':i} for i in all_options[selected_country]]

@callback(
        Output('cities-radio','value'),
        Input('cities-radio','options')
)
def set_cities_value(available_options):
    return available_options[0]['value']

@callback(
    Output('display-selected-values','children'),
    Input('countries-radio','value'),
    Input('cities-radio','value')
)
def set_display_children(selected_country, selected_city):
    return f'{selected_city}城市位於{selected_country}'


if __name__ == '__main__':
    app.run(debug=True)