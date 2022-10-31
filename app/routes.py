# from urllib import response
# from ast import literal_eval


from flask import Blueprint, jsonify, request, make_response
from app.models.planet import Planet
from app.models import planet
from app import db


# --------------------------------------WAVE 1--------------------------------------

planet_bp = Blueprint("planet", __name__, url_prefix="/planet")


@planet_bp.route("", methods=["GET"])
def show_planets():
    planets = Planet.query.all()
    res_body = []
    for planet in planets:
        res_body.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                " diameter": planet.diameter
            }
        )
    return jsonify(res_body), 200

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
