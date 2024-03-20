import flask
from flask import request, jsonify
from flask_cors import CORS
import sys
from geo_distance.utils.distance import calc_distance_list, calc_distance, filter_points

app = flask.Flask(__name__)
cors = CORS(app)


@app.route("/distance", methods=["GET"])
def distance():
    try:
        lat1 = request.args.get("lat1")
        lon1 = request.args.get("lon1")
        lat2 = request.args.get("lat2")
        lon2 = request.args.get("lon2")
    except:
        print("Invalid parameters")
        return jsonify({"error": "Invalid parameters"}), 400


    point1 = {
        "lat": lat1,
        "lon": lon1
    }
    point2={
        "lat": lat2,
        "lon": lon2
    }
    distance = calc_distance(point1, point2)
    response = {
        "distance_meters": distance,
        "distance_kilometres": distance / 1000,
        "distance_miles": distance / 1609.34,
    }
    print(response)
    return jsonify(response), 200

@app.route("/distance_list", methods=["POST"])
def distance_list():
    try:
        data = request.get_json()
        points_list = data["points"]
    except:
        print("Invalid JSON")
        return jsonify({"error": "Invalid JSON"}), 400

    if len(points_list) < 2:
        print("Not enough points. Need at least 2 points to calculate distance")
        return (
            jsonify(
                {
                    "error": "Not enough points. Need at least 2 points to calculate distance"
                }
            ),
            400,
        )

    try:
        # fitered_points_list = filter_points(points_list, 8, 350)
        fitered_points_list = points_list
        total_distance = calc_distance_list(fitered_points_list)
        response_dict = {
            "distance_metres": total_distance,
            "distance_kilometres": total_distance / 1000,
            "distance_miles": total_distance / 1609.34,
        }
        print (response_dict)
        return jsonify(response_dict), 200

    except:
        print("Invalid JSON Format. Ensure parameters lat and lon are floats")
        return (
            jsonify(
                {
                    "error": "Invalid JSON Format. Ensure parameters lat and lon are floats"
                }
            ),
            400,
        )

if __name__ == "__main__":
    default_port = 8501
    try:
        port = int(sys.argv[1])
    except:
        port = default_port

    debug = False
    if len(sys.argv) > 2:
        debug = sys.argv[2] == "debug"
    # print(f'{debug=}')
    app.run(host="0.0.0.0", port=port, debug=debug)
