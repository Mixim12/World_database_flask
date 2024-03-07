from flask import request, flash, render_template, redirect, url_for

from ..app import app
from ..db import db
from ..Countries.models import Country
from ..Cities.models import City
from .controllers import list_all_cities, create_city, get_city, update_city, delete_city
from .forms import CityForm

@app.route("/city/delete/<city_id>", methods=['GET', 'POST'])
def delete_city(city_id):
    city = City.query.get(city_id)

    if request.method == 'POST':
        db.session.delete(city)
        db.session.commit()
        
        return redirect(url_for('list_all_cities'))

    return render_template('world_app/delete_city.html', city=city)

@app.route("/city/update/<city_id>", methods=['GET', 'POST'], endpoint='update_city')
def update_city(city_id):
    city = City.query.get(city_id)
    form = CityForm(obj=city)
    
    if form.validate_on_submit():
        city.name = form.name.data
        city.area = form.area.data
        city.population = form.population.data
        city.is_capital = form.is_capital.data
        db.session.commit()
        
        return redirect(url_for('list_all_cities'))
    
    return render_template('world_app/update_city.html', city=city, form=form)

@app.route("/city", endpoint='list_all_cities')
def city():
    cities = City.query.all()
    countries = Country.query.all()
    response = []
    for city in cities:
        city_dict = {
            'id': city.id,
            'name': city.name,
            'area': city.area,
            'population': city.population,
            'is_capital': city.is_capital,
        }
        response.append(city_dict)
    return render_template('world_app/cities.html', cities=response)
    
@app.route("/city/add", methods=['GET', 'POST'], endpoint='add_city')
def add_country():
    submitted = False
    form = CityForm()

    if request.method == "POST":
        form = CityForm(request.form)
        if form.validate_on_submit(): 
            
            city = City(
                name=form.name.data,
                area=form.area.data,    
                population=form.population.data,
                is_capital=form.is_capital.data,
            )
            
            db.session.add(city)
            db.session.commit()
            
            submitted = True

    return render_template('world_app/add_city.html', form=form, submitted=submitted)