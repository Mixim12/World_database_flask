from flask import request, jsonify, redirect, url_for
import uuid

from .. import db
from .models import Continent
from ..Countries import models as Countries



def get_countries_names(countries_ids):
    countries_names = []
    for country_id in countries_ids:
        country = Countries.Country.query.get(country_id)
        countries_names.append(country.name)
    return countries_names

        
def get_continent(continent_id):
    continent = Continent.query.get(continent_id).toDict()
    
    if continent is None:
        return jsonify({'error': 'Continent not found!'})
    return jsonify(continent.toDict())

def update_continent(continent_id):
    continent = Continent.query.get(continent_id)
    
    if continent is None:
        return jsonify({'error': 'Continent not found!'})
    
    request_form = request.form.to_dict()
    
    continent.name = request_form['name']
    continent.area = request_form['area']
    continent.population = request_form['population']
    
    db.session.commit()
    
    return jsonify(continent.toDict())

def delete_continent(continent_id):
    continent = Continent.query.get(continent_id)
    
    if continent is None:
        return jsonify({'error': 'Continent not found!'})
    
    db.session.delete(continent)
    db.session.commit()
    
    return jsonify({'message': 'Continent deleted!'})