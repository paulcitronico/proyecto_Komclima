from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_required, login_user, logout_user
from models.Forms.SignUpForm import SignUpForm
from models.Forms.LoginForm import LoginForm
from models.user import User
from routes.decorator import admin_required

auth = Blueprint("auth",__name__)

@auth.route("/register", methods=["GET","POST"])
@login_required
@admin_required
def register_user():
    form = SignUpForm()
    if request.method=="POST":
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            password = form.password.data
            type_user = form.type_user.data
            rut = form.rut.data

            user_by_rut = User.get_by_rut(rut)
            user_by_email = User.get_by_email(email)

            if user_by_rut or user_by_email or (user_by_rut and user_by_email):
                flash("Email y/o rut ya se encuentra vinculado a un usuario.")
                return redirect("register")
            else:
                user = User(name,password,rut,email,type=type_user)
                user.save()
                return redirect(url_for("root.index"))
    return render_template("register.html",css="css/register.css",form=form)

@auth.route("/login",methods=["GET","POST"])
def _login_user():
    if request.method == "POST":
        form = LoginForm()
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data

            user = User.get_by_rut(username)

            if not user or not user.check_password(password):
                flash("Usuario y/o contraseña no válida(o).")
                return redirect("login")

            login_user(user=user)
            return redirect("profile")

    return redirect(url_for("root.index"))

@auth.route("/logout")
@login_required
def _logout_user():
    logout_user()
    return redirect("/")