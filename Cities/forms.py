from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField

class CityForm(FlaskForm):
    name = StringField('Name')
    area = IntegerField('Area')
    population = IntegerField('Population')
    
    is_capital = BooleanField('Is Capital')
    
    submit = SubmitField('Submit')
    
    