from flask import request, flash, render_template, redirect, url_for

from ..app import app
from ..db import db
from .models import Country
from ..Cities.models import City
from .controllers import list_all_countries, create_country, get_country, update_country, delete_country
from .forms import CountryForm

@app.route("/country/delete/<country_id>", methods=['GET', 'POST'])
def delete_country(country_id):
    country = Country.query.get(country_id)

    if request.method == 'POST':
        db.session.delete(country)
        db.session.commit()
        flash('Country deleted successfully', 'success')
        return redirect(url_for('list_all_countries'))

    return render_template('world_app/delete_country.html', country=country)

@app.route("/country/update/<country_id>", methods=['GET', 'POST'], endpoint='update_country')
def update_country(country_id):
    country = Country.query.get(country_id)
    form = CountryForm(obj=country)
    form.set_cities_choices()
    
    if form.validate_on_submit():
        country.name = form.name.data
        country.area = form.area.data
        country.population = form.population.data
        country.government = form.government.data
        country.cities = City.query.filter(City.id.in_(form.cities.data)).all()
        db.session.commit()
        flash('Country updated successfully', 'success')
        return redirect(url_for('list_all_countries'))
    
    return render_template('world_app/update_country.html', country=country, form=form)

@app.route("/country", endpoint='list_all_countries')
def country():
    countries = Country.query.all()
    cities = City.query.all()
    response = []
    for country in countries:
        country_cities = City.query.filter(City.country_id == country.id).all()
        country_dict = {
            'id': country.id,
            'name': country.name,
            'area': country.area,
            'population': country.population,
            'government': country.government,
            'cities': [city.name for city in country_cities]
        }
        response.append(country_dict)
    return render_template('world_app/countries.html', countries=response, cities=cities)
    
from flask import render_template

@app.route("/country/add", methods=['GET', 'POST'], endpoint='add_country')
def add_country():
    form = CountryForm()
    submitted = False

    if request.method == "POST":
        form = CountryForm(request.form)
        if form.validate_on_submit(): 
            cities = City.query.filter(City.id.in_(form.cities.data)).all()
            
            country = Country(
                name=form.name.data,
                area=form.area.data,    
                population=form.population.data,
                government=form.government.data,
                cities=cities,
            )
            
            db.session.add(country)
            db.session.commit()
            
            submitted = True  

    return render_template('world_app/add_country.html', form=form, submitted=submitted)
