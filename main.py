import tkinter as tk
from tkinter import messagebox
import random
import os
import tempfile

a = "Hello. Think Before Running it."
b = "Are you sure?"
c = "You made a mistake."

def handle_response(response):
    if response == "yes":
        messagebox.showinfo("Response", "Congratulations.")
        simulate_deletion()
    else:
        messagebox.showinfo("Response", c)

def simulate_deletion():
    if random.randint(0, 1) == 1:
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.close()
        try:
            os.remove(temp_file.name)
            messagebox.showinfo("Result", "Simulated file deletion successful.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete the file: {e}")
    else:
        messagebox.showinfo("Result", "Random condition not met. No file deletion.")

def ask_confirmation():
    if messagebox.askyesno("Confirmation", b):
        handle_response("yes")
    else:
        handle_response("no")

root = tk.Tk()
root.title("Chat Box")
root.geometry("300x150")

message_label = tk.Label(root, text=a, wraplength=250)
message_label.pack(pady=20)

run_button = tk.Button(root, text="Run", command=ask_confirmation)
run_button.pack(pady=10)

root.mainloop()
