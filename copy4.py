#AI Generated for testing purposes
#July23 - Test PR
#July23- Test Merge

import os
import subprocess
import pickle
from flask import Flask, request

app = Flask(__name__)

# 1. Hardcoded credentials (Sensitive Data Exposure)
USERNAME = "admin"
PASSWORD = "P@ssw0rd123"  # Hardcoded password

# 2. Command injection vulnerability
@app.route("/ping")
def ping():
    ip = request.args.get("ip", "")
    # UNSAFE: Directly concatenating user input into shell command
    command = "ping -c 1 " + ip
    try:
        output = subprocess.check_output(command, shell=True)  # Vulnerable
        return f"<pre>{output.decode()}</pre>"
    except subprocess.CalledProcessError:
        return "Ping failed", 400

# 3. Insecure deserialization
@app.route("/load")
def load_data():
    data = request.args.get("data", "")
    try:
        # UNSAFE: Loading pickled data from untrusted input
        obj = pickle.loads(bytes.fromhex(data))  # Vulnerable
        return f"Loaded object: {obj}"
    except Exception as e:
        return f"Error: {e}", 400

# 4. SQL Injection (if using raw queries)
import sqlite3
@app.route("/user")
def get_user():
    username = request.args.get("username", "")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # UNSAFE: Direct string formatting in SQL query
    query = f"SELECT * FROM users WHERE username = '{username}'"  # Vulnerable
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return {"users": result}

# 5. Weak cryptography
import hashlib
def weak_hash(password):
    # UNSAFE: MD5 is cryptographically broken
    return hashlib.md5(password.encode()).hexdigest()

if __name__ == "__main__":
    app.run(debug=True)
