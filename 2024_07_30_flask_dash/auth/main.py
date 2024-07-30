from flask import Blueprint,render_template

auth_blueprint = Blueprint('auth',__name__)
@auth_blueprint.route("/auth/")
@auth_blueprint.route("/auth/login")
def index():
    return render_template('/auth/login.html.jinja')