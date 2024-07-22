from dash import Dash,html,dcc,Input,Output,callback
import data

app = Dash(__name__)

areas = [tup[0] for tup in data.get_areas()]

app.layout = html.Div([
    dcc.Dropdown(
       options = areas,
       value = areas[0],
       id='areas'
    )
])

if __name__ == '__main__':
    app.run(debug=True)
    