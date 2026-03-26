from flask import Flask, jsonify, request, render_template
from models import HotelModel
from services import BookingService
import random

app = Flask(__name__)

hotel = HotelModel()
service = BookingService(hotel)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/state", methods=["GET"])
def get_state():
    return jsonify(hotel.get_state())


@app.route("/api/book", methods=["POST"])
def book():
    data = request.get_json()
    n = int(data.get("count", 1))

    if n < 1 or n > 5:
        return jsonify({"error": "You can book between 1 and 5 rooms only."}), 400

    available = hotel.get_available_rooms()
    if len(available) < n:
        return jsonify({"error": f"Only {len(available)} room(s) available."}), 400

    result = service.book_rooms(n)
    if not result:
        return jsonify({"error": "No suitable rooms found."}), 400

    selected_rooms, travel = result
    for r in selected_rooms:
        hotel.mark_booked(r["number"])

    return jsonify({
        "booked": [r["number"] for r in selected_rooms],
        "travel": travel,
        "state": hotel.get_state()
    })


@app.route("/api/random", methods=["POST"])
def random_occupancy():
    data = request.get_json()
    count = int(data.get("count", 1))

    # Random occupancy: random number between count and count*10 (capped at 92)
    available = hotel.get_available_rooms()
    
    if not available:
        return jsonify({"error": "No rooms available to randomly occupy."}), 400
    
    max_rand = min(count * 10, len(available))
    max_rand = max(max_rand, count)
    occupy_count = random.randint(count, max_rand)
    
    # Only mark currently available rooms, don't reset previously booked rooms
    rooms_to_mark = random.sample(available, min(occupy_count, len(available)))
    for r in rooms_to_mark:
        hotel.mark_booked(r["number"])

    return jsonify({
        "occupied": occupy_count,
        "state": hotel.get_state()
    })


@app.route("/api/reset", methods=["POST"])
def reset():
    hotel.reset()
    return jsonify({"state": hotel.get_state()})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
