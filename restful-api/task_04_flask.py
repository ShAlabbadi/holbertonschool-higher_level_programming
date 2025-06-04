#!/usr/bin/env python3
"""
Flask API implementation for user management
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user database
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route('/')
def home():
    """Root endpoint returning welcome message"""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Endpoint returning list of usernames"""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Status endpoint"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Endpoint returning user details by username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Endpoint for adding new users"""
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == '__main__':
    app.run(debug=True)
