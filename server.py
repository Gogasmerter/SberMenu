from data import db_session
from data.users import User
from flask import Flask, abort, redirect, render_template
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from forms.login import LoginForm
from forms.user import UserForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "very_secret_key"

login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register/user", methods=["GET", "POST"])
def register_user():
    if current_user.is_authenticated:
        abort(404)
    form = UserForm()
    title = "Регистрация"
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            message = {"status": 0, "text": "Пароли не совпадают"}
            return render_template("register_user.html", title=title, form=form, message=message)
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            message = {"status": 0, "text": "Такой пользователь уже есть"}
            return render_template("register_user.html", title=title, form=form, message=message)
        user = User(
            email=form.email.data,
            name=form.name.data,
            surname=form.surname.data,
            role=2,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect("/")
    return render_template("register_user.html", title=title, form=form, message="")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    title = "Вход"
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
        message = {'status': 0, 'text': 'Неверный логин или пароль'}
        return render_template('login.html', title=title, form=form, message=message)
    return render_template('login.html', title=title, form=form, message="")


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == "__main__":
    db_session.global_init("db/GriBD.db")
    app.run(port=8080, host="127.0.0.1", debug=True)
