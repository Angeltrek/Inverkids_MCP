from flask import Blueprint, request, jsonify
import os

from src.backend.client import BackendClient
from src.app.executor import execute_agent

agent_bp = Blueprint("agent", __name__)

BACKEND_BASE_URL = os.environ["BACKEND_BASE_URL"]

@agent_bp.post("/ask")
def ask_agent():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Authorization header required"}), 401

    body = request.get_json(force=True)
    question = body.get("question")

    if not question:
        return jsonify({"error": "Question required"}), 400

    backend_client = BackendClient(
        base_url=BACKEND_BASE_URL,
        token=token,
    )

    answer = execute_agent(
        question,
        backend_client=backend_client,
    )

    return jsonify({
        "question": question,
        "answer": answer,
    }), 200
