from flask import Flask, jsonify

app = Flask(__name__)

# Sample list data
list_data = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

@app.route("/")
def index():
    return "Welcome to the Flask List Data Server!"

@app.route("/data")
def get_data():
    return jsonify(list_data)

if __name__ == "__main__":
    # Run on all interfaces for container/Codespace access
    app.run(host="0.0.0.0", port=3000, debug=True)
