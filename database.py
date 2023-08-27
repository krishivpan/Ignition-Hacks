import sqlite3

connection = sqlite3.connect('locations.db')
cursor = connection.cursor()

create_table_query = '''
    CREATE TABLE IF NOT EXISTS locations (
        id INTEGER PRIMARY KEY,
        start_location TEXT,
        end_location TEXT
    )
'''

cursor.execute(create_table_query)

connection.commit()
connection.close()
