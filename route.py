from flask import jsonify, request

batteries = [
    {"id": "BAT001", "voltage": 3.7, "status": "OK"},
    {"id": "BAT002", "voltage": 3.5, "status": "Charging"},
    {"id": "BAT003", "voltage": 3.6, "status": "Discharging"}
]

def register_routes(app):
    @app.route("/")
    def home():
        return "Welcome to the Battery Telemetry API weekend special!"
    
    @app.route("/hello")
    def hello():
        return jsonify({"message": "Hello, Flask Telemetry Weekend!"})
    @app.route("/batteries", methods=["GET"])
    def get_batteries():
        return jsonify(batteries)
 
    @app.route("/add_battery", methods=["POST"])
    def add_battery():
        data = request.get_json()
        if not data or "id" not in data or "voltage" not in data or "status" not in data:
            return jsonify({"error": "Invalid battery data"}), 400
        batteries.append(data)
        return jsonify({"message": "Battery added successfully"}), 201
    @app.route("/battery-stats", methods=["GET"])
    def battery_stats():
        voltages = [b["voltage"] for b in batteries]

        if not voltages:
            return jsonify({"error": "No battery data available"}), 404

        max_v = max(voltages)
        min_v = min(voltages)
        avg_v = sum(voltages) / len(voltages)

        return jsonify({
            "max_voltage": max_v,
            "min_voltage": min_v,
            "average_voltage": avg_v
        })