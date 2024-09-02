from flask import Flask, request, jsonify
import bcrypt
import jwt
import pyotp
import datetime
from cryptography.fernet import Fernet

app = Flask(__name__)

# A key for encrypting sensitive data
encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

# Secret key for JWT
SECRET_KEY = 'your_jwt_secret_key'

# In-memory storage for simplicity (use a database in production)
users = {}

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users[username] = {'password': hashed_password}

    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    totp_code = request.json.get('totp_code')

    user = users.get(username)

    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        # Verify TOTP code
        totp = pyotp.TOTP(user.get('totp_secret', ''))
        if not totp.verify(totp_code):
            return jsonify({'message': 'Invalid TOTP code'}), 401
        
        # Create JWT token
        token = jwt.encode({
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, SECRET_KEY, algorithm='HS256')

        return jsonify({'token': token})

    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/setup-mfa', methods=['POST'])
def setup_mfa():
    username = request.json.get('username')
    
    # Generate a TOTP secret
    totp_secret = pyotp.random_base32()
    users[username]['totp_secret'] = totp_secret
    
    return jsonify({'totp_secret': totp_secret})

@app.route('/store-data', methods=['POST'])
def store_data():
    sensitive_data = request.json.get('data')
    encrypted_data = cipher_suite.encrypt(sensitive_data.encode('utf-8'))

    # Here we just store it in memory, but you should store it in a database
    users[request.json.get('username')]['data'] = encrypted_data

    return jsonify({"message": "Data stored securely"})

@app.route('/retrieve-data', methods=['GET'])
def retrieve_data():
    username = request.args.get('username')
    encrypted_data = users[username].get('data', None)

    if encrypted_data:
        decrypted_data = cipher_suite.decrypt(encrypted_data).decode('utf-8')
        return jsonify({"data": decrypted_data})

    return jsonify({"message": "No data found"}), 404

if __name__ == '__main__':
    # Control debug mode via environment variables
    import os
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode)