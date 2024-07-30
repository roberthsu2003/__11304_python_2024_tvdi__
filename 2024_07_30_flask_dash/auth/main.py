from flask import Blueprint,render_template

auth_blueprint = Blueprint('auth',__name__)
@auth_blueprint.route("/auth/",methods=['GET', 'POST'])
@auth_blueprint.route("/auth/login",methods=['GET', 'POST'])
def index():
    return render_template('/auth/login.html.jinja')