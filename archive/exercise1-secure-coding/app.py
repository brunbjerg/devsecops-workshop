
### **2. `exercise1-secure-coding/app.py`**

This is the Python application file with initial basic implementation. You will enhance this file by following the instructions in the `README.md`.

```python
from flask import Flask, request, jsonify
import jwt
import bcrypt
import datetime
import sqlite3

app = Flask(__name__)

# Secret key for JWT
SECRET_KEY = 'your_secret_key'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Fetch user from database
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    conn.close()

    if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        # Create JWT token
        token = jwt.encode({
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, SECRET_KEY, algorithm='HS256')
        
        return jsonify({'token': token})

    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/users', methods=['GET'])
def users():
    token = request.headers.get('Authorization')
    try:
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except:
        return jsonify({'message': 'Token is invalid or expired'}), 403

    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    
    return jsonify([dict(user) for user in users])

if __name__ == '__main__':
    app.run(host='0.0.0.0')