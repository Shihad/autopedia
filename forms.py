from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    login = StringField("Введите логин", validators=[DataRequired()])
    password = PasswordField("Введите пароль", validators=[DataRequired()])
    submit = SubmitField()

class SignUpForm(FlaskForm):
    login = StringField("Придумайте логин", validators=[DataRequired()])
    password = PasswordField("Придумайте пароль", validators=[DataRequired()])
    password2 = PasswordField("Повторите пароль", validators=[DataRequired()])
    email = StringField("Электронная почта", validators=[DataRequired(), Email()])
    submit = SubmitField()