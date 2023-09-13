from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():
    return "API homepage"
@app.route('/api', methods=["GET"])
def get_api():
    data = {
        "name": "James",
        "age": 27,
        "location": "Texas"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)