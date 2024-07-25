from flask import Flask,render_template,request
from dash1 import youbike
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from dash1.callback import app1
from login.main import bp
import data

app = Flask(__name__)
app.register_blueprint(youbike.dashbp)
app.register_blueprint(bp)
application = DispatcherMiddleware(app,{
    "/dash1/callback":app1.server
})

@app.route("/")
def index():
    #print(list(map(lambda value:value[0],data.get_areas())))
    selected_area = request.args.get('area')
    areas = [tup[0] for tup in data.get_areas()]
    selected_area = '士林區' if selected_area is None else selected_area
    detail_snaes = data.get_snaOfArea(area=selected_area)
    
    #areas->所有行政區 
    #show_area -> 要顯示的行政區
    #detail_snaes -> 該行政區所有站點資訊   
    return render_template('index.html.jinja',areas=areas,show_area=selected_area,detail_snaes=detail_snaes)    


@app.errorhandler(404)
def page_error(e):
    return '<p>this page not found</p>'

if __name__ == '__main__':
   run_simple("localhost",8080, application, use_debugger=True, use_reloader=True) 