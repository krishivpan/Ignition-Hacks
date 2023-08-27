from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json
from bson import json_util
import requests
import googlemaps
from datetime import datetime

app = Flask(__name__)
CORS(app, origins="*", supports_credentials=True, methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])

@app.route('/send-locations', methods=['POST', 'GET'])
@cross_origin(origin='*')
def send_locations():
    print("hello")
    if(request.method == "POST"):
        print("hey")

        data = request.get_data
        print(data)
        start_location = data(['startLocation'])
        end_location = data(['endLocation'])

        # Print the received locations
        print("Received start location:", start_location)
        print("Received end location:", end_location)

        # Google Maps API key
        apikey = 'AIzaSyCbHMXlojYEJn94poaxLRKAXhk79ln4H7A'

        # Connect to the Google Maps API client
        gmaps_client = googlemaps.Client(key=apikey)

        # Origin and destination addresses
        originaddress = start_location
        destinationaddress = end_location

        # Get origin and destination coordinates
        origin_result = gmaps_client.geocode(originaddress)
        destination_result = gmaps_client.geocode(destinationaddress)

        if origin_result and destination_result:
            origin = origin_result[0]['geometry']['location']
            destination = destination_result[0]['geometry']['location']

            # Get directions and details
            biking_result = gmaps_client.directions(origin, destination, mode="bicycling", avoid='ferries', departure_time="now")[0]['legs'][0]
            transit_result = gmaps_client.directions(origin, destination, mode="transit", avoid='ferries', departure_time="now")[0]['legs'][0]
            driving_result = gmaps_client.directions(origin, destination, mode="driving", avoid='ferries', departure_time="now")[0]['legs'][0]

            # Print distance and duration details
            print("Biking:")
            print("Distance:", biking_result['distance']['text'])
            print("Duration:", biking_result['duration']['text'])

            print("Transit:")
            print("Distance:", transit_result['distance']['text'])
            print("Duration:", transit_result['duration']['text'])

            print("Driving:")
            print("Distance:", driving_result['distance']['text'])
            print("Duration:", driving_result['duration']['text'])
        else:
            print("Invalid addresses.")

        response = {'message': 'Data received successfully'}
        print("hi")
        return json.loads(json_util.dumps(response))
    
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}                            

if __name__ == '__main__':
    app.run(debug=True)
