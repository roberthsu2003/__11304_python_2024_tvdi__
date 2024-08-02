from dash import Dash, dash_table, html
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

print(df.to_dict('records'))

app = Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(data=df.to_dict('records'),
                         columns=[{'name':i, "id":i} for i in df.columns]
                        )
])

if __name__ == '__main__':
    app.run(debug=True)