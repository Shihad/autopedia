from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    login = StringField("Введите логин", validators=[DataRequired()])
    password = PasswordField("Введите пароль", validators=[DataRequired()])
    submit = SubmitField()



class RegisterForm(FlaskForm):
    username = StringField("Логин",validators=[DataRequired()])
    mail = StringField("Почта")
    password1 = PasswordField("Пароль",validators=[DataRequired()])
    password2 = PasswordField("Повтор пароля", validators=[DataRequired()])
    submit = SubmitField()