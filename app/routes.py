# from sys import prefix
# from urllib import response
# from ast import literal_eval
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

planet_bp= Blueprint("planet", __name__, url_prefix= "/planet")
@planet_bp.route("", methods =["GET"])
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

# Wave 2
@planet_bp.route("/<planet_id>", methods =["GET"])
def check_invalid_id(planet_id):
    
    try:
        planet_id = int(planet_id)
    except:
        response_messege = f"It is invalid input"
        return jsonify({
            "messege": response_messege
        }), 400
    for planet in planets:
        if planet_id == planet.id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
        }
    return jsonify({
        "message": f"We can't found this planet"}), 404

@planet_bp.route("/<planet_name>", methods =["GET"])
def check_invalid_name(planet_name):
    
    try:
        planet_name = str(planet_name)
    except:
        response_messege = f"It is invalid input"
        return jsonify({
            "messege": response_messege
        }), 400
    for planet in planets:
        if planet_name == planet.name:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
        }
    return jsonify({
        "message": f"We can't found this planet"}), 404

