
from flask import Blueprint, jsonify, request, make_response, abort
from app.models.planet import Planet
from app import db

# --------------------------------------WAVE 1--------------------------------------

planet_bp = Blueprint("planet", __name__, url_prefix="/planet")


@planet_bp.route("", methods=["GET"])
def show_planets():
    planet_name = request.args.get("name")
    if planet_name:
        planets = Planet.query.filter_by(name=planet_name)
    else:
        planets = Planet.query.all()

    response = []
    for planet in planets:
        response.append(planet.to_dict())
    return jsonify(response)

# # Wave 2
# @planet_bp.route("/<planet_id>", methods =["GET"])
# def check_invalid_id(planet_id):

#     try:
#         planet_id = int(planet_id)
#     except:
#         response_messege = f"It is invalid input"
#         return jsonify({
#             "messege": response_messege
#         }), 400
#     for planet in planets:
#         if planet_id == planet.id:
#             return {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description
#         }
#     return jsonify({
#         "message": f"We can't found this planet"}), 404

# @planet_bp.route("/<planet_name>", methods =["GET"])
# def check_invalid_name(planet_name):

#     try:
#         planet_name = str(planet_name)
#     except:
#         response_messege = f"It is invalid input"
#         return jsonify({
#             "messege": response_messege
#         }), 400
#     for planet in planets:
#         if planet_name == planet.name:
#             return {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description
#         }
#     return jsonify({
#         "message": f"We can't found this planet"}), 404

# --------------------------------------WAVE 3--------------------------------------


@planet_bp.route("/add", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"],
        diameter=request_body["diameter"])
    db.session.add(new_planet)
    db.session.commit()
    return make_response(f" Id: {new_planet.id} successfully created", 201)

# --------------------------------------WAVE 4--------------------------------------


def checking_valid_id(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        response_message = f"Invalid id {planet_id}."
        # abort(make_response({"message":f"Invalid id {planet_id}."},400))
        abort(make_response(response_message, 400))
    get_planet_id = Planet.query.get(planet_id)
    if get_planet_id is None:
        response_message = f"Planet with id {planet_id} was not found in the database"
        # abort(make_response({"message":f"lanet with id {planet_id} was not found in the database"}, 404))
        abort(make_response(response_message, 404))
    return get_planet_id


@planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = checking_valid_id(planet_id)
    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "diameter": planet.diameter
    }, 200


@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_one_planet(planet_id):
    planet = checking_valid_id(planet_id)
    request_body = request.get_json()
    if "name" not in request_body or\
        "description" not in request_body or\
            "diameter" not in request_body:
        return jsonify({"message": "Request must include name, description, diameter"}), 400
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.diameter = request_body["diameter"]

    db.session.commit()
    return jsonify({"message": f"Successfuly replaced planet with id {planet_id}"}), 200


@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_one_planet(planet_id):
    planet = checking_valid_id(planet_id)
    db.session.delete(planet)
    db.session.commit()
    return jsonify({"message": f"Successfuly delete planet with id {planet_id}"}), 200
