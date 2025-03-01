import sqlite3

# Connect to the database
conn = sqlite3.connect("hotel.db")
cursor = conn.cursor()




# Insert Sample Rooms
cursor.executemany(
    "INSERT OR IGNORE INTO Rooms (room_number, room_type, price, status) VALUES (?, ?, ?, ?)",
    [
        ("101", "Single", 50.0, "Available"),
        ("102", "Double", 75.0, "Booked"),
        ("103", "Suite", 120.0, "Available")
    ]
)

# Insert Sample Reservations (only if no reservations exist)
cursor.execute("SELECT COUNT(*) FROM Reservations")
if cursor.fetchone()[0] == 0:
    cursor.executemany(
        "INSERT INTO Reservations (guest_id, room_id, check_in, check_out, guest_name, phone_number, email_address) VALUES (?, ?, ?, ?)",
        [
            (1, 1, "2025-03-01", "2025-03-05"),
            (2, 2, "2025-03-02", "2025-03-06"),
            (3, 3, "2025-03-03", "2025-03-07"),
        ]
    )

# Commit and close the connection
conn.commit()
conn.close()

print("Sample data inserted successfully!")
