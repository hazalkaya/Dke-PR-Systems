from flask import Blueprint, jsonify

from ..modelsDatabase import (
    Bahnhof,
    bahnhöfeSchema,
)

# API = communication layer, method dump = stores python Objects in a file, from flask library jsonify

api = Blueprint("api", __name__)

@api.route("/api/")
def api_index():
    return jsonify(
        {
            "api": [
                "/trainstations",
                "/trainstations/<int:trainstations_id>",
                "/users",
                "/users/<int:users_id>",
            ]
        }
    )

@api.route("/api/trainstations/", methods=["GET"])
def api_getBahnhöfe():
    trainstations = Bahnhof.query.all()
    res = bahnhöfeSchema.dump(trainstations)
    return jsonify({"trainstations": res})
