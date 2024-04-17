from .services import (
    get_cart,
    create_cart,
    add_item_to_cart,
    remove_item_from_cart,
    update_item_quantity,
)
from flask import request, jsonify


def init_routes(app):
    @app.route("/api/cart/<cart_id>")
    def get(cart_id):
        result = get_cart(cart_id)
        if "error" in result:
            return jsonify(result), 404
        return jsonify(result)

    @app.route("/api/cart", methods=["POST"])
    def create():
        result = create_cart()
        return jsonify(result)

    @app.route("/api/cart/<id>/item", methods=["POST"])
    def add_item(id):
        data = request.get_json()
        result = add_item_to_cart(id, data)
        if "error" in result:
            return jsonify(result), 404
        return jsonify(result)

    @app.route("/api/cart/<cart_id>/item/<item_id>", methods=["DELETE"])
    def remove_item(cart_id, item_id):
        result = remove_item_from_cart(cart_id, item_id)
        if "error" in result:
            return jsonify(result), 404
        return jsonify(result)

    @app.route("/api/cart/<cart_id>/item/<item_id>", methods=["PATCH"])
    def update_item(cart_id, item_id):
        data = request.get_json()
        result = update_item_quantity(cart_id, item_id, data.get("quantity"))
        if "error" in result:
            return jsonify(result), 404
        return jsonify(result)
