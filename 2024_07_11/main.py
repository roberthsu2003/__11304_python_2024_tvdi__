from flask import Flask,render_template,request
import data

app = Flask(__name__)
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
    
    
    