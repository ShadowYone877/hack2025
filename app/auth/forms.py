  

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField

from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    lastname = StringField('Apellido Paterno', validators=[DataRequired(), Length(max=64)])
    lastname2 = StringField('Apellido Materno', validators=[DataRequired(), Length(max=64)])
    local_phone = StringField('Telefono local', validators=[DataRequired(), Length(max=10)])
    mobile_phone = StringField('Celular', validators=[DataRequired(), Length(max=10)])
    key_elector = StringField('Clave Elector', validators=[DataRequired(), Length(max=28)])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    rol = SelectField("rol" , choices=[])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Registrar')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Iniciar Sesión')
