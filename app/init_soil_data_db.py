import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('soil_data.db')
cursor = conn.cursor()

# Drop the table if it already exists to avoid duplication
cursor.execute("DROP TABLE IF EXISTS soil_info")

# Create the soil_info table
cursor.execute('''
    CREATE TABLE soil_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        land_number TEXT,
        country TEXT,
        land_type TEXT,
        crop TEXT,
        season TEXT,
        water_capacity TEXT
    )
''')

# Insert sample data into the soil_info table
sample_data = [
    (None, '1234', 'India', 'red soil', 'groundnut', 'kharif', 'high'),
    (None, '2380', 'India', 'black soil', 'sugar cane', 'rabi', 'high'),
    (None, '9100', 'India', 'clay soil', 'rice', 'rabi', 'high'),
    (None, '2000', 'India', 'red soil', 'red gram', 'rabi', 'low'),
    (None, '1990', 'India', 'clay soil', 'cotton', 'rabi', 'high')
]

cursor.executemany('''
    INSERT INTO soil_info VALUES (?, ?, ?, ?, ?, ?, ?)
''', sample_data)

# Commit changes and close the connection
conn.commit()
conn.close()

print("soil_data.db has been created and populated successfully.")
