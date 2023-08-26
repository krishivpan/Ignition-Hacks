from flask import Flask, request, jsonify
import googlemaps

app = Flask(__name__)https://github.com/krishivpan/Ignition-Hacks

# Initialize the Google Maps API client
gmaps = googlemaps.Client(key='YOUR_GOOGLE_MAPS_API_KEY')

# ... (Previous code for user and points management)

# Endpoint to get optimal route using Google Maps API
@app.route('/route', methods=['POST'])
def get_optimal_route():
    start_location = request.json.get('start_location')
    end_location = request.json.get('end_location')
    mode = request.json.get('mode', 'driving')  # Default to driving mode

    directions_result = gmaps.directions(start_location, end_location, mode=mode)

    if directions_result:
        # Extract relevant route information from the API response
        route_info = {
            "duration": directions_result[0]['legs'][0]['duration']['text'],
            "distance": directions_result[0]['legs'][0]['distance']['text'],
            "steps": [step['html_instructions'] for step in directions_result[0]['legs'][0]['steps']]
        }
        return jsonify(route_info)
    return jsonify({"error": "No route found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
