from flask import Blueprint, request, jsonify
import os

from src.auth.client import AuthClient

auth_bp = Blueprint("auth", __name__)

BASE_URL = os.environ["BACKEND_BASE_URL"]


@auth_bp.post("/login")
def login():
    body = request.get_json(force=True)

    enrollment_id = body.get("enrollment_id")
    password = body.get("password")

    if not enrollment_id or not password:
        return jsonify({
            "error": "enrollment_id and password are required"
        }), 400

    auth = AuthClient(base_url=BASE_URL)

    session = auth.login_with_enrollment(
        enrollment_id=enrollment_id,
        password=password,
    )

    return jsonify({
        "user": session.user,
        "token": session.token,
    }), 200
