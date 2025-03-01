import tkinter as tk
import random
import string
import pyperclip


def generate_password(phrase):
    user_password_portion = phrase[:3]
    random_password_portion = ''.join(random.choices(string.ascii_lowercase + string.digits, k=int(entry_length.get()) - len(user_password_portion)))
    password = random_password_portion + user_password_portion.upper()
    
    return password

def get_input():
    user_phrase = entry.get()
    password = generate_password(user_phrase)
    result_label.config(text=f"Your new password is: {password}")

def get_password_length():
    password_length = int(entry_length.get())

def copy_to_clipboard():
    text_to_copy = result_label.cget("text").replace("Your new password is: ", "")
    pyperclip.copy(text_to_copy)
    result_label.config(text="Text copied to clipboard!")
    
window = tk.Tk()
window.title("Password Generator")

label = tk.Label(window, text="Welcome to the Password Generator!", font=("Open Sans", 20))
label.pack()
label = tk.Label(window, text=" ")
label.pack()
label = tk.Label(window, text="Enter a phrase:")
label.pack()

entry = tk.Entry(window)
entry.pack()

label = tk.Label(window, text="How long do you want your password to be? ")
label.pack()

entry_length = tk.Entry(window)
entry_length.pack()



result_label = tk.Label(window, text="Your new password is: ", font=("Open Sans", 14))
result_label.pack()

button = tk.Button(window, text="Submit", command=get_input)
button.pack()

button_two = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
button_two.pack()

window.mainloop()
