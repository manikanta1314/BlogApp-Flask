from flask_wtf import FlaskForm
# auto converting python classes into html forms.
from wtforms import StringField
from wtforms.validators import DataRequired,Length,Email,EqualTo,Password

class RegistrationForm(FlaskForm):
    username = StringField("Username",
                           validators=[DataRequired(), Length(min = 2,max = 20)])
    email = StringField("Email",
                        validators=[DataRequired(),Email()]) 
    
    password = Pa