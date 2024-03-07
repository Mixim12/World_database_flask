from flask import request, jsonify
import uuid

from .. import db
from .models import Country

def list_all_countries():
    countries = Country.query.all()
    response = []
    for country in countries:
        response.append(country.toDict())
    return jsonify(response)

def create_country():
    request_form = request.form.to_dict()
    
    id = str(uuid.uuid4())
    new_country = Country(id=id, name=request_form['name'], area=request_form['area'], population=request_form['population'], continent_id=request_form['continent_id'])
    
    db.session.add(new_country)
    db.session.commit()
    
    response = Country.query.get(id).toDict()
    
    return jsonify(response)

def get_country(country_id):
    country = Country.query.get(country_id).toDict()
    
    if country is None:
        return jsonify({'error': 'Country not found!'})
    return jsonify(country.toDict())

def update_country(country_id):
    country = Country.query.get(country_id)
    
    if country is None:
        return jsonify({'error': 'Country not found!'})
    
    request_form = request.form.to_dict()
    
    country.name = request_form['name']
    country.area = request_form['area']
    country.population = request_form['population']
    country.continent_id = request_form['continent_id']
    
    db.session.commit()
    
    return jsonify(country.toDict())

def delete_country(country_id):
    country = Country.query.get(country_id)
    
    if country is None:
        return jsonify({'error': 'Country not found!'})
    
    db.session.delete(country)
    db.session.commit()
    
    return jsonify({'message': 'Country deleted!'})