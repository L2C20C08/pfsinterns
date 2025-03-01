import sqlite3

# Connect to the database
conn = sqlite3.connect("hotel.db")
cursor = conn.cursor()

# Create the Rooms table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS Rooms (
    room_id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_number TEXT NOT NULL UNIQUE,
    room_type TEXT NOT NULL,
    price REAL NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('Available', 'Booked'))
)
''')

# Create the Reservations table with the necessary columns for guest details
cursor.execute('''
CREATE TABLE IF NOT EXISTS Reservations (
    reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    guest_id INTEGER,
    room_id INTEGER,
    check_in TEXT,
    check_out TEXT,
    FOREIGN KEY (guest_id) REFERENCES Guests(guest_id),
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
)
''')

# Create the Guests table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS Guests (
    guest_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT
)
''')

# Insert Sample Rooms (if not already inserted)
cursor.executemany(
    "INSERT OR IGNORE INTO Rooms (room_number, room_type, price, status) VALUES (?, ?, ?, ?)",
    [
        ("101", "Single", 50.0, "Available"),
        ("102", "Double", 75.0, "Booked"),
        ("103", "Suite", 120.0, "Available")
    ]
)

# Insert Sample Guests (if not already inserted)
cursor.executemany(
    "INSERT OR IGNORE INTO Guests (name, phone, email) VALUES (?, ?, ?)",
    [
        ("Alice Johnson", "1234567890", "alice@example.com"),
        ("Bob Smith", "0987654321", "bob@example.com"),
        ("Charlie Brown", "1122334455", "charlie@example.com")
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

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Sample data inserted successfully!")
