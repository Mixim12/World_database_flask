from flask import request, render_template, redirect, url_for, flash, jsonify

from ..app import app
from ..db import db
from .models import Continent
from ..Countries.models import Country
from .controllers import  get_continent, update_continent, delete_continent
from .forms import ContinentForm

@app.route("/continent/delete/<continent_id>", methods=['GET', 'POST'])
def delete_continent(continent_id):
    continent = Continent.query.get(continent_id)

    if request.method == 'POST':
        db.session.delete(continent)
        db.session.commit()
        
        return redirect(url_for('list_all_continents'))

    return render_template('world_app/delete_continent.html', continent=continent)

@app.route("/continent/update/<continent_id>", methods=['GET', 'POST'], endpoint='update_continent')
def update_continent(continent_id):
    continent = Continent.query.get(continent_id)
    form = ContinentForm(obj=continent)
    form.set_country_choices()
    
    if form.validate_on_submit():
        continent.name = form.name.data
        continent.area = form.area.data
        continent.population = form.population.data
        continent.countries = Country.query.filter(Country.id.in_(form.countries.data)).all()
        db.session.commit()
        
        return redirect(url_for('list_all_continents'))
    
    return render_template('world_app/update_continent.html', continent=continent, form=form)


@app.route("/continent", endpoint='list_all_continents')
def continent():
    continents = Continent.query.all()
    countries = Country.query.all()
    response = []
    for continent in continents:
        continent_countries = Country.query.filter(Country.continent_id == continent.id).all()
        continent_dict = {
            'id': continent.id,
            'name': continent.name,
            'area': continent.area,
            'population': continent.population,
            'countries': [country.name for country in continent_countries]
        }
        response.append(continent_dict)
    return render_template('world_app/continents.html', continents=response, countries=countries)

    

@app.route("/continent/add", methods=['GET', 'POST'], endpoint='add_continent')
def add_continent():
    submitted = False
    form = ContinentForm()

    if request.method == "POST":
        form = ContinentForm(request.form)
        if form.validate_on_submit(): 
            
            countries = Country.query.filter(Country.id.in_(form.countries.data)).all()
            
            continent = Continent(
                name=form.name.data,
                area=form.area.data,    
                population=form.population.data,
                countries=countries
            )
            db.session.add(continent)
            db.session.commit()
            
            submitted = True
            

    return render_template('world_app/add_continent.html', form=form, submitted=submitted)
