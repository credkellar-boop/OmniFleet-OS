from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/fleet/status')
def get_fleet_status():
    return jsonify({"fleet_size": 1, "active_units": 1, "revenue_daily": 250})
  
