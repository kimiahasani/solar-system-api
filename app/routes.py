from urllib import response
from ast import literal_eval
from flask import Blueprint, jsonify
class Planet:
    def __init__(self, id, name, descrption) -> None:
        self.id = id
        self.name = name
        self.description = descrption

planets =[
    Planet(4, "Earth", "Our Beatiful Family"),
    Planet(8, "Moon", "The Size of Moon"),
    Planet(3, "Mars", "Mars on Fire")
]

planet_bp= Blueprint("planet", __name__)
@planet_bp.route("/planet", methods =["GET"])
def show_planets():
    res_body = []
    for planet in planets:
        res_body.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
            }
        )
    return jsonify(res_body), 200
