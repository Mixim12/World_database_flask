from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectMultipleField
from ..Countries.models import Country

class ContinentForm(FlaskForm):
    name = StringField('Name')
    area = IntegerField('Area')
    population = IntegerField('Population')

    countries = SelectMultipleField('Countries', coerce=int, choices=[], validate_choice=False)

    def set_country_choices(self):
        countries = Country.query.all()
        self.countries.choices = [(country.id, country.name) for country in countries]
        
    submit = SubmitField('Submit')
    
    def __init__(self, *args, **kwargs):
        super(ContinentForm, self).__init__(*args, **kwargs)
        self.set_country_choices()
