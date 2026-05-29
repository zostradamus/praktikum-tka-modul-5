from flask import Flask, jsonify
import socket

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 12000000},
    {"id": 2, "name": "Mouse", "price": 150000},
    {"id": 3, "name": "Keyboard", "price": 350000},
    {"id": 4, "name": "Monitor", "price": 3500000},
    {"id": 5, "name": "Headset", "price": 750000},
]

@app.route("/")
def index():
    hostname = socket.gethostname()
    return jsonify({
        "server": "Server 2 - TokoKita",
        "hostname": hostname,
        "message": "Selamat datang di TokoKita Backend 2!"
    })

@app.route("/products")
def products():
    hostname = socket.gethostname()
    return jsonify({
        "server": "Server 2 - TokoKita",
        "hostname": hostname,
        "products": PRODUCTS
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
