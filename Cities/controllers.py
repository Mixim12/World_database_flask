from flask import request, jsonify
import uuid

from .. import db
from .models import City

def list_all_cities():
    cities = City.query.all()
    response = []
    for city in cities:
        response.append(city.toDict())
    return jsonify(response)

def create_city():
    request_form = request.form.to_dict()
    
    id = str(uuid.uuid4())
    new_city = City(id=id, name=request_form['name'], area=request_form['area'], population=request_form['population'], country_id=request_form['country_id'])
    
    db.session.add(new_city)
    db.session.commit()
    
    response = City.query.get(id).toDict()
    
    return jsonify(response)

def get_city(city_id):
    city = City.query.get(city_id).toDict()
    
    if city is None:
        return jsonify({'error': 'City not found!'})
    return jsonify(city.toDict())

def update_city(city_id):
    city = City.query.get(city_id)
    
    if city is None:
        return jsonify({'error': 'City not found!'})
    
    request_form = request.form.to_dict()
    
    city.name = request_form['name']
    city.area = request_form['area']
    city.population = request_form['population']
    city.country_id = request_form['country_id']
    
    db.session.commit()
    
    return jsonify(city.toDict())

def delete_city(city_id):
    city = City.query.get(city_id)
    
    if city is None:
        return jsonify({'error': 'City not found!'})
    
    db.session.delete(city)
    db.session.commit()
    
    return jsonify({'message': 'City deleted!'})