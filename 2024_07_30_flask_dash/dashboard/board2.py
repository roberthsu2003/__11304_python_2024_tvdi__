from dash import Dash,html,dcc,Input,Output,callback,dash_table
import data
import pandas as pd

app2 = Dash(__name__,requests_pathname_prefix='/dashboard/app2/')

areas = [tup[0] for tup in data.get_areas()]
print(areas[0])

app2.layout = html.Div([
    dcc.Dropdown(
       options = areas,
       value = areas[0],
       id='areas'
    ),
    html.Hr(),
    dash_table.DataTable(id='sites_table')
])
#如果要連結2個dash,必需要加上app1
@app2.callback(
    Output('sites_table','data'),
    Input('areas','value')
)
def selected_area(areas_value):
    content = data.get_snaOfArea(area=areas_value)
    df = pd.DataFrame(content)
    df.columns = ['站點名稱','總數','可借','可還','日期','狀態']
    return df.to_dict('records')

    