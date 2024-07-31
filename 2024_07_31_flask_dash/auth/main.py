from flask import Blueprint,render_template,request,session,redirect
from flask_wtf import FlaskForm
from wtforms import EmailField,PasswordField
from wtforms.validators import DataRequired,Length
from .datasource import validateUser
auth_blueprint = Blueprint('auth',__name__)

@auth_blueprint.route('/auth/register')
def register():
    return render_template('/auth/register.html.jinja')

class LoginForm(FlaskForm):
    email = EmailField('郵件信箱',validators=[DataRequired()])
    password = PasswordField('密碼',validators=[DataRequired(),Length(min=4, max=20)])


@auth_blueprint.route("/auth/",methods=['GET', 'POST'])
@auth_blueprint.route("/auth/login",methods=['GET', 'POST'])
def index(email:str | None = None):
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            print("表單傳送過來")
            print("驗証了token")
            email = form.email.data
            password = form.password.data
            print(f'email:{email}')
            print(f'password:{password}')
            is_ok, username = validateUser(email,password)
            if is_ok:
                session['username'] = username
                return redirect('/')
            else:
                form.email.errors.append("帳號或密碼錯誤")
                form.email.data = ""

    else:
        print("這是第一次進入")
        #if email is not None:
        #    form.email.data = email
    
    return render_template('/auth/login.html.jinja',form=form)

@auth_blueprint.route("/auth/logout")
def logout():
    session.pop('username')
    return redirect('/')