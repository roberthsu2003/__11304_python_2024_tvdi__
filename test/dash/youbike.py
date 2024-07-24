from flask import Blueprint,render_template
dashbp = Blueprint('dash',__name__,url_prefix='/dash')

@dashbp.route('/register',methods=('GET','POST'))
def register():
    return render_template('dash/youbike.html.jinja')