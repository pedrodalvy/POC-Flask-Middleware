from http import HTTPMethod, HTTPStatus
from typing import Any, Dict

from flask import Blueprint, jsonify, request, Response

storage: Dict[int, Any] = {}
bp = Blueprint("routes", __name__)


@bp.route("/create", methods=[HTTPMethod.POST])
def create() -> Response:
    """
    Create a sample resource
    """
    payload = request.get_json()

    storage[payload["id"]] = payload

    return jsonify(payload)


@bp.route("/", methods=[HTTPMethod.GET])
def read() -> Response:
    """
    Read a sample resource
    """
    response_data = []

    for key, value in storage.items():
        response_data.append(value)

    return jsonify(response_data)


@bp.route("/<int:item_id>", methods=[HTTPMethod.GET])
def read_by_id(item_id: int) -> [Response]:
    """
    Read a sample resource
    """
    data = storage.get(item_id)

    if data is None:
        return jsonify({}), HTTPStatus.NOT_FOUND

    return jsonify(storage[item_id])


@bp.route("/<int:item_id>", methods=[HTTPMethod.PUT])
def update(item_id: int) -> Response:
    """
    Update a sample resource
    """
    payload = request.get_json()

    storage[item_id] = payload

    return jsonify(payload)


@bp.route("/<int:item_id>", methods=[HTTPMethod.DELETE])
def delete(item_id: int) -> Response:
    """
    Delete a sample resource
    """
    deleted_data = storage.pop(item_id)

    return jsonify(deleted_data)
