#AI Generated for testing purposes
#Aug14-PR Comment

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
