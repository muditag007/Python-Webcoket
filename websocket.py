from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
import random,time

app: Flask = Flask(__name__)

app.config["SECRET_KEY"] = "secret"
app.config["SESSION_TYPE"] = "filesystem"

socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/", methods=["GET", "POST"])
def index():
    return jsonify({"data": "Web Socket Example"})


@socketio.on("connect")
def connect():
    print("client connected")


@socketio.on("update")
def join():
    print("updated")
    random_speed = random.randint(1, 100)
    random_dist = random.randint(1, 100)
    random_lat = random.randint(1, 100)
    random_long = random.randint(1, 100)

    emit(
        "newValues",
        {
            "speed": random_speed,
            "dist": random_dist,
            "lat": random_lat,
            "long": random_long,
        },
    )


if __name__ == "__main__":
    socketio.run(app, debug=True)
