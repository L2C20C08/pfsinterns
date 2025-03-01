import sqlite3

# Connect to the database
conn = sqlite3.connect("hotel.db")
cursor = conn.cursor()

# Fetch all reservations
cursor.execute("SELECT * FROM Reservations")
rows = cursor.fetchall()

# Check if there is data
if rows:
    print("Reservations found in the database:")
    for row in rows:
        print(row)
else:
    print("No reservations found! You need to insert sample data.")

# Close connection
conn.close()
