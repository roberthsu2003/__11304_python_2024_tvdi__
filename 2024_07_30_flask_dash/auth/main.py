from flask import Blueprint

auth_blueprint = Blueprint('auth',__name__)
@auth_blueprint.route("/auth/")
@auth_blueprint.route("/auth/login")
def index():
    return "<h1>我是auth的首頁</h1>"