from flask import Flask, request, jsonify
import bcrypt

app = Flask(__name__)

users = {}

@app.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']
    
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users[username] = hashed_password
    
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    
    if username in users and bcrypt.checkpw(password.encode('utf-8'), users[username]):
        return jsonify({"message": "Login successful"}), 200
    
    return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode)