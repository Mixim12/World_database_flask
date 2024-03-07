from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import StringField, SubmitField, IntegerField, SelectField, SelectMultipleField
from ..Cities.models import City

class CountryForm(FlaskForm):
    name = StringField('Name')
    area = IntegerField('Area')
    population = IntegerField('Population')
    
    capital = SelectField('Capital', coerce=int, choices=[], validate_choice=False)
    government = SelectField('Government', choices=[('Monarchy', 'Monarchy'), ('Republic', 'Republic'), ('Dictatorship', 'Dictatorship'), ('Democracy', 'Democracy')], validate_choice=False)
    
    cities = SelectMultipleField('Cities',coerce=int, choices=[],validate_choice=False)
    
    def set_cities_choices(self):
        cities = City.query.all()
        self.cities.choices = [(city.id, city.name) for city in cities]
        self.capital.choices = [(city.id, city.name) for city in cities]
        
    continent_id = SelectField('Continent', choices=[], validate_choice=False)
    
    submit = SubmitField('Submit')
    
    def __init__(self, *args, **kwargs):
        super(CountryForm, self).__init__(*args, **kwargs)
        self.set_cities_choices()