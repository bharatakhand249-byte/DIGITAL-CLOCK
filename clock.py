import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x120")
root.config(bg="black")

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)   # updates every 1 second

label = tk.Label(root, font=("Arial", 40, "bold"), bg="black", fg="cyan")
label.pack(pady=20)

update_time()

root.mainloop()
