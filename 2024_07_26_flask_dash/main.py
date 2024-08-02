from flask import Flask,render_template,request
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from dashboard.board1 import app1
from dashboard.board2 import app2
import data
import dashboard

app = Flask(__name__)
application = DispatcherMiddleware(app,{
    "/dashboard/app1":app1.server,
    "/dashboard/app2":app2.server
})

@app.route("/")
def index():
    return render_template("index.html.jinja")

@app.route("/index1")
def index1():
    #print(list(map(lambda value:value[0],data.get_areas())))
    selected_area = request.args.get('area')
    areas = [tup[0] for tup in data.get_areas()]
    selected_area = '士林區' if selected_area is None else selected_area
    detail_snaes = data.get_snaOfArea(area=selected_area)
    
    #areas->所有行政區 
    #show_area -> 要顯示的行政區
    #detail_snaes -> 該行政區所有站點資訊   
    return render_template('index1.html.jinja',areas=areas,show_area=selected_area,detail_snaes=detail_snaes)    
    
    


if __name__ == "__main__":
    run_simple("localhost", 8080, application,use_debugger=True,use_reloader=True)