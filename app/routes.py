from flask import Blueprint, jsonify, request, abort, make_response
from app import db
from app.models.planet import Planet
# Test the flask 
hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route("/hello_world", methods=["GET"])
def say_hello_world():
    my_beautiful_response_body = "Hello, World!"
    return my_beautiful_response_body
# --------------------------------------WAVE 1--------------------------------------
# Define planets
# class Planet:
#     def __init__(self, id, name, description):
#         self.id = id
#         self.name = name
#         self.description = description
# planets =[
#     Planet(4, "Earth", "Our Beatiful Family"),
#     Planet(8, "Moon", "The Size of Moon"),
#     Planet(3, "Mars", "Mars on Fire")
# ]

planet_bp= Blueprint("plants", __name__,url_prefix='/planet')
@planet_bp.route("", methods =["GET"])
def show_planets():
    res_body = []
    planets = Planet.query.all()
    for planet in planets:
        res_body.append(
            {
                "id": planet.id,
                "name": planet.name,
                "size": planet.size,
                "description": planet.description
            }
        )
    return jsonify(res_body), 200

# --------------------------------------WAVE 2--------------------------------------
# check one planet in planet list
# check one planet in planet by id
def check_valid_id(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))
    planets = Planet.query.all()    
    for planet in planets:
        if planet.id == planet_id:
            return planet
    abort(make_response({"message":f"planet {planet_id} not found"}, 404))
    
@planet_bp.route("/<planet_id>", methods =["GET"])
def get_one_planet(planet_id):
    planet = check_valid_id(planet_id)
    return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description
            }
# check one planet in planet by name another methodes
@planet_bp.route("/name/<planet_name>", methods =["GET"])  
def check_valid_name(planet_name):
    try:
        planet_name = str(planet_name)
    except:
        response_message = f"Invalid planet name"
        return jsonify({"message":response_message}), 400
    
    planets = Planet.query.all() 
    for planet in planets:
        if planet.name == planet_name:
            return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description
            }   
    return jsonify({"message":f"No this planet in our list"}), 404
    
# --------------------------------------WAVE 3--------------------------------------   
# POST new a planet
@planet_bp.route('/add', methods = ["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"],
        size = request_body['size'],
        description = request_body['description']
    )
    db.session.add(new_planet)
    db.session.commit()
    return make_response(f'Planet {new_planet.name} successfully created',200)
