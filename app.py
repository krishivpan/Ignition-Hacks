from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/send-locations', methods=['POST'])
def send_locations():
    data = request.json

    start_location = data['startLocation']
    end_location = data['endLocation']

    # Connect to the SQLite database
    connection = sqlite3.connect('locations.db')
    cursor = connection.cursor()

    # Insert the locations into the database
    cursor.execute("INSERT INTO locations (start_location, end_location) VALUES (?, ?)",
                   (start_location, end_location))
    
    connection.commit()
    connection.close()

    return jsonify({'message': 'Locations saved successfully'})

if __name__ == '__main__':
    app.run()
