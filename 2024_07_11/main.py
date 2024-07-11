from flask import Flask,render_template,request
import data

app = Flask(__name__)
@app.route("/")
def index():
    #print(list(map(lambda value:value[0],data.get_areas())))
    selected_area = request.args.get('area')
    areas = [tup[0] for tup in data.get_areas()]
    if  selected_area is None:
        print("第一次進入")      
        return render_template('index.html.jinja',areas=areas)
    else:
        print(selected_area)
        return render_template('index.html.jinja',areas=areas)
    
    
    