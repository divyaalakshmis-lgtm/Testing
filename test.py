import os
import sqlite3
import pickle
from flask import Flask, request
import yaml   # vulnerable versions exist
import requests  # old versions have CVEs

app = Flask(__name__)

# 🔐 Hardcoded secret
SECRET_KEY = "sk_live_ABC123SUPERSECRET"
app.secret_key = SECRET_KEY


# ❌ SQL Injection
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    return cursor.fetchall()


# ❌ Command Injection
@app.route("/ping")
def ping():
    host = request.args.get("host")
    os.system(f"ping -c 1 {host}")
    return "Pinged!"


# ❌ Path Traversal
@app.route("/read")
def read_file():
    filename = request.args.get("file")
    with open(filename, "r") as f:
        return f.read()


# ❌ Insecure Deserialization
@app.route("/load", methods=["POST"])
def load_data():
    data = request.data
    obj = pickle.loads(data)
    return str(obj)


# ❌ XSS
@app.route("/")
def home():
    name = request.args.get("name", "")
    return f"<h1>Hello {name}</h1>"


# ❌ YAML unsafe load (known vuln pattern)
@app.route("/yaml", methods=["POST"])
def load_yaml():
    content = request.data.decode()
    data = yaml.load(content, Loader=yaml.Loader)
    return str(data)


if __name__ == "__main__":
    app.run(debug=True)
