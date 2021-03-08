from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class ComentarioForm(FlaskForm):
  nome = StringField('Seu Nome', validators=[DataRequired()])
  nota = IntegerField('Nota', validators=[DataRequired()])
  corpo = StringField('Descrição', widget=TextArea(), validators=[DataRequired()])
  
  submit = SubmitField('Enviar')
