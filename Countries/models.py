from sqlalchemy import inspect

from .. import db

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable = False)
    name = db.Column(db.String(50), nullable = False)
    area = db.Column(db.Integer, nullable = False)
    population = db.Column(db.Integer, nullable = False)
    
    cities = db.relationship('City', back_populates='country')
    
    government = db.Column(db.String(50), nullable = True)
    
    continent_id = db.Column(db.Integer, db.ForeignKey('continent.id'), nullable=True)
    continent = db.relationship('Continent', back_populates='countries')
    
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return "<%r>" % self.name