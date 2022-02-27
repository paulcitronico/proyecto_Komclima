from email import message
from flask import Blueprint, render_template, url_for, redirect, request
from models.Forms.SignUpForm import SignUpForm
from models.user import User

auth = Blueprint("auth",__name__)

@auth.route("/register", methods=["GET","POST"])
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
                return redirect("register")
            else:
                user = User(name,password,rut,email,type=type_user)
                user.save()
                return redirect(url_for("root.index"))
    return render_template("register.html",css="register.css",form=form)