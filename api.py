
import requests
import googlemaps
from datetime import datetime

# Google Maps API key
apikey = 'AIzaSyCbHMXlojYEJn94poaxLRKAXhk79ln4H7A'

# Connect to the Google Maps API client
gmaps_client = googlemaps.Client(key=apikey)

# Origin and destination addresses
originaddress = input("Enter your starting destination: ")
destinationaddress = input('Enter your ending destination: ')

# Get origin and destination coordinates
origin_result = gmaps_client.geocode(originaddress)
destination_result = gmaps_client.geocode(destinationaddress)

if origin_result and destination_result:
    origin = origin_result[0]['geometry']['location']
    destination = destination_result[0]['geometry']['location']
else:
    print("Invalid addresses.")

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
