from flask_wtf import Form
from wtforms import (BooleanField, TextField, HiddenField, PasswordField, 
   DateTimeField, validators, IntegerField)
from wtforms.validators import DataRequired

class LoginForm(Form):
   next = HiddenField()
   login = TextField('user_name', [validators.Required()])
   password  = TextField('password',  [validators.Required()])
   remember_me = BooleanField('remember_me', default = False)
    
class SignupForm(Form):
   next = HiddenField()
   user_name   = TextField('user_name',    [validators.Length(min=4, max=30)])
   first_name  = TextField('first_name',   [validators.Required()])
   last_name   = TextField('last_name',    [validators.Required()])
   email       = TextField('email',        [validators.Required()])
   password    = PasswordField('New Password', [
      validators.Required(),
      validators.EqualTo('confirm', message='Passwords must match')
   ])
   confirm     = PasswordField('Repeat Password', [validators.Required()])