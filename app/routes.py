from flask import Blueprint, jsonify, request

# Test the flask 
hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route("/hello_world", methods=["GET"])
def say_hello_world():
    my_beautiful_response_body = "Hello, World!"
    return my_beautiful_response_body
# --------------------------------------WAVE 1--------------------------------------
# Define planets
class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
planets = [
    Planet(1, 'Earth', "family earth"),
    Planet(2, 'Saturn', "rings of saturn"),
    Planet(3, 'Mars', "Red Planet")
]
planets_bp = Blueprint("planets", __name__)
@planets_bp.route('/planets', methods = ["Get"])
        
def show_planets():
    response_planet = []
    for planet in planets:
        response_planet.append(
            {
                "id": planet.id,
                "name":planet.name,
                "description":planet.description
            }
        )
    return jsonify(response_planet)
# POST new a planet
@planets_bp.route('/planets/add', methods = ["POST"])
def add_planet():
    request_newplanet = request.get_json()
    planets.append(request_newplanet)
    return "success add new planet"

# --------------------------------------WAVE 2--------------------------------------

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
