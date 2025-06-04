#!/usr/bin/python3
"""Flask API with basic routing, JSON data, and POST support"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user store
users = {}

@app.route('/')
def home():
    """Root route returns a welcome message"""
    return "Welcome to the Flask API!"

@app.route('/status')
def status():
    """Status check route"""
    return "OK"

@app.route('/data')
def data():
    """Return list of all usernames"""
    return jsonify(list(users.keys()))

@app.route('/users/<username>')
def get_user(username):
    """Return full user data for a given username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Add new user via POST request"""
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201

if __name__ == "__main__":
    app.run()
