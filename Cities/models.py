from sqlalchemy import inspect


from .. import db

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable = False)
    name = db.Column(db.String(50), nullable = False)
    area = db.Column(db.Integer, nullable = False)
    population = db.Column(db.Integer, nullable = False)
    is_capital = db.Column(db.Boolean, nullable = True)
    
    country = db.relationship('Country', back_populates='cities')
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=True)

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return "<%r>" % self.name