from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    diameter = db.Column(db.Integer)
    description = db.Column(db.String)

    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["diameter"] = self.diameter
        planet_as_dict["description"] = self.description
        return planet_as_dict
