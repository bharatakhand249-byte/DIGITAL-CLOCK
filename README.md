# DIGITAL-CLOCK
A simple and clean Digital Clock built using Python and Tkinter. This project displays the current time in hours, minutes, and seconds, updating every second. Perfect for beginners learning GUI development in Python.
⏰ Digital Clock (Python)

A simple and elegant Digital Clock built using Python and Tkinter.
This project displays the current time in hours, minutes, and seconds, updating every second.
Perfect for beginners learning GUI programming in Python.


🚀 Features

🕒 Real-time digital clock

⏳ Updates every second

🎨 Clean GUI (black theme + cyan digits)

💻 Beginner-friendly and easy to understand

⚡ Lightweight and fast

---import tkinter as tk
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

root.mainloop().

📦 Requirements

Make sure Python is installed.
No extra modules are needed.

Python 3.x

Tkinter (comes built-in with Python)
---
python clock.py
digital-clock/
│
├── clock.py       # main program file
├── README.md      # project documentation
└── LICENSE        # MIT license
🧠 What You Learn

Tkinter GUI basics

Label widget usage

Using after() for real-time updates

Time formatting with strftime()
---

📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute the code.
