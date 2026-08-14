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
