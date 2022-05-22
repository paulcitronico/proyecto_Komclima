from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, SelectField
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    rut = StringField("Rut", validators=[DataRequired()])
    email = EmailField("email", validators=[DataRequired()])
    type_user = SelectField("Tipo de usuario", validators=[DataRequired()], choices=["User","admin","Superadmin"])
    submit = SubmitField("Registrar")