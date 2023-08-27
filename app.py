from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send-locations', methods=['POST'])
def receive_locations():
    data = request.get_json()
    start_location = data.get('startLocation')
    end_location = data.get('endLocation')

    # You can save the locations to a JSON file, process them, or perform any other action
    # For example, you can save them to a file named 'locations.json'
    with open('locations.json', 'w') as file:
        json.dump(data, file)

    return jsonify({'message': 'Locations received by Flask'})

if __name__ == '__main__':
    app.run()
