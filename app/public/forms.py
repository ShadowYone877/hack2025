  

from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    content = TextAreaField('Contenido', validators=[DataRequired(), ])
    submit = SubmitField('Comentar')

class institucion(FlaskForm):
    escuela = TextAreaField('Escuela', validators=[DataRequired(), ])
    localidad = TextAreaField('Localidad', validators=[DataRequired(), ])
    requerimiento = TextAreaField('Requerimiento', validators=[DataRequired(), ])
    submit = SubmitField('Enviar')
    