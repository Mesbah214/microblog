from flask import render_template, flash, redirect, url_for
from app import app
from app.form import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Karim"}
    posts = [
        {
            "author" : {"username" : "John"},
            "body" : "What a beautiful day!"
        },
        {
            "author" : {"username" : "Karim"},
            "body" : "Qatar lost in the opening match to Ecuador"
        },
    ]
    return render_template("index.html", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("login required for user {}, remember_me={}" .format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template("login.html", form=form, title="Sign In")
