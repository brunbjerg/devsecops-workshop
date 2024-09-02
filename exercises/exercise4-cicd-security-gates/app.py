from flask import Flask, request, jsonify
import bcrypt
import jwt
import datetime

app = Flask(__name__)

SECRET_KEY = 'your_jwt_secret_key'
users = {}  # In-memory storage (for simplicity)

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    
    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users[username] = hashed_password

    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Fetch the hashed password from storage
    hashed_password = users.get(username)

    if hashed_password and bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        # Generate a JWT token
        token = jwt.encode({
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, SECRET_KEY, algorithm='HS256')

        return jsonify({'token': token}), 200

    return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=False)
