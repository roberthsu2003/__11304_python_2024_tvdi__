from dash import Dash, dcc, html, Input, Output, callback

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
print(external_stylesheets)

app = Dash(__name__,external_stylesheets=external_stylesheets)

if __name__ == '__main__':
    app.run(debug=True)