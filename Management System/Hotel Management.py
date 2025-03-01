
import tkinter as tk
from tkinter import ttk, messagebox 

import sqlite3

from datetime import datetime

def manage_reservations():
    global tree
    reservation_label.config(text="Opening Reservations Menu...")
    
    reservation_window = tk.Toplevel(window)
    reservation_window.title("Reservation Information")
    reservation_window.geometry("520x400")
    
    frame = tk.Frame(reservation_window)
    frame.pack()
    
    label = tk.Label(reservation_window, text="Manage Reservations", font=("Open Sans", 16)) 
    label.pack()
    
    add_button = tk.Button(reservation_window, text="Add Reservations", command=add_reservations)
    add_button.pack()
    
    remove_button = tk.Button(reservation_window, text="Remove Reservations", command=delete_reservations)
    remove_button.pack()
    
    tree = ttk.Treeview(reservation_window, columns=("ID", "Guest ID", "Room ID", "Check-in", "Check-out", "Name", "Phone", "Email"), show="headings")
    tree.heading("ID", text="Reservation ID")
    tree.heading("Guest ID", text="Guest ID")
    tree.heading("Room ID", text="Room ID")
    tree.heading("Check-in", text="Check-in Date")
    tree.heading("Check-out", text="Check-out Date")
    
    tree.column("ID", width=80)
    tree.column("Guest ID", width=100)
    tree.column("Room ID", width=100)
    tree.column("Check-in", width=120)
    tree.column("Check-out", width=120)
    
    tree.pack(pady=20, fill="both", expand=True)
    
    fetch_reservations()
    
def fetch_reservations():
    conn = sqlite3.connect("hotel.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Reservations")
    rows = cursor.fetchall()
    conn.close()
        
    print("Fetched reservations:", rows)
        
    tree.delete(*tree.get_children())
        
    for row in rows:
        tree.insert("", tk.END, values=row)
    

def delete_reservations():
    selected_item = tree.selection()
    
    if not selected_item:
        messagebox.showerror("Error, Please select a valid reservation to remove.")
        return
    
    reservation_id = tree.item(selected_item)["values"][0]
    
    
    if reservation_id is None:
        messagebox.showerror("Error", "Invalid reservation ID.")
        return
    
    if messagebox.askyesno("Delete Reservation", f"Are you sure you want to delete reservation {reservation_id}?"):
        try:
            conn = sqlite3.connect("hotel.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Reservations WHERE reservation_id = ?", (reservation_id,))
            conn.commit()
            conn.close()
            
            fetch_reservations()
            messagebox.showinfo("Success", f"Reservation {reservation_id} delete successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting reservation: {e}")
            

def add_reservations():
    add_window = tk.Toplevel(window)
    
    label_guest_id = tk.Label(add_window, text="Guest ID:")
    label_guest_id.pack(pady=5)
    entry_guest_id = tk.Entry(add_window)
    entry_guest_id.pack(pady=5)
    
    label_room_id = tk.Label(add_window, text="Room ID:")
    label_room_id.pack(pady=5)
    entry_room_id = tk.Entry(add_window)
    entry_room_id.pack(pady=5)
    
    label_check_in = tk.Label(add_window, text="Check-in Date (YYYY-MM-DD):")
    label_check_in.pack(pady=5)
    entry_check_in = tk.Entry(add_window)
    entry_check_in.pack(pady=5)
    
    label_check_out = tk.Label(add_window, text="Check-out Date (YYYY-MM-DD):")
    label_check_out.pack(pady=5)
    entry_check_out = tk.Entry(add_window)
    entry_check_out.pack(pady=5)
    
    
    
    
    
    
    def submit_reservation():
        guest_id = entry_guest_id.get()
        room_id = entry_room_id.get()
        check_in = entry_check_in.get()
        check_out = entry_check_out.get()

        if not guest_id or not room_id or not check_in or not check_out:
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return
        
        try:
            # Ensure guest_id and room_id are integers
            guest_id = int(guest_id)
            room_id = int(room_id)
            
            # Ensure the date format is correct
            try:
                datetime.strptime(check_in, "%Y-%m-%d")
                datetime.strptime(check_out, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Date Error", "Please enter valid dates in the format YYYY-MM-DD.")
                return

            # Insert the reservation into the database
            conn = sqlite3.connect("hotel.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Reservations (guest_id, room_id, check_in, check_out) VALUES (?, ?, ?, ?)",
                           (guest_id, room_id, check_in, check_out))
            conn.commit()
            conn.close()

            # Close the add window and show success message
            messagebox.showinfo("Success", "Reservation added successfully!")
            add_window.destroy()

            # Refresh the reservations list
            manage_reservations()
        
        except ValueError:
            messagebox.showerror("Invalid Input", "Guest ID and Room ID must be integers.")
        

    # Submit button for adding reservation
    submit_button = tk.Button(add_window, text="Submit", command=submit_reservation)
    submit_button.pack(pady=10)

def guest_information():
    guest_label.config(text="Opening Guest Information...")

def billing_information():
    billing_label.config(text="Opening Billing Information...")


window = tk.Tk()
window.title("Hotel Management System")

label = tk.Label(window, text="Management System", font=("Open Sans", 25))
label.pack()

label = tk.Label(window, text=" ")
label.pack(pady=10)

button = tk.Button(window, text="Manage Reservations", command=manage_reservations)
button.pack()

reservation_label = tk.Label(window, text=" ")
reservation_label.pack()


window.mainloop()


