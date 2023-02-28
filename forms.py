from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    login = StringField("Введите логин", validators=[DataRequired()])
    password = PasswordField("Введите пароль", validators=[DataRequired()])
    submit = SubmitField()


class RegisterForm(FlaskForm):
    login = StringField("Логин",validators=[DataRequired()])
    email = StringField("Почта", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    password2 = PasswordField("Повтор пароля", validators=[DataRequired()])
    submit = SubmitField()
