from wtforms import form 
from wtforms import StringField,IntegerField
from wtforms import EmailField


class UserForm(form):
    id=IntegerField('id')
    nombre=StringField('nombre')
    apellidos=StringField('apellidos')
    email = EmailField('correo')

