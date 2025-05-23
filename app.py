from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

trades = []
bot_status = {"active": True}

@app.route("/api/trades", methods=["GET"])
def get_trades():
    return jsonify(trades)

@app.route("/api/trade", methods=["POST"])
def log_trade():
    data = request.json
    trades.append(data)
    return jsonify({"message": "Trade logged"}), 200

@app.route("/api/bot/status", methods=["GET"])
def get_status():
    return jsonify(bot_status)

@app.route("/api/bot/status", methods=["POST"])
def set_status():
    status = request.json.get("active")
    bot_status["active"] = status
    return jsonify({"message": f"Bot {'started' if status else 'paused'}"})

@app.route("/api/dashboard", methods=["GET"])
def get_dashboard():
    stats = {
        "balance": 10000,
        "equity": 10250,
        "profit_today": 250,
        "open_trades": len(trades),
    }
    return jsonify(stats)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
