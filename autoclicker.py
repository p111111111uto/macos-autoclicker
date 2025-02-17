import time
import threading
import tkinter as tk
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

# Default settings
click_delay = 1.0
clicking = False
mouse = Controller()

# Start/Stop key
start_stop_key = KeyCode(char='f6')

def clicker():
    global clicking
    while True:
        if clicking:
            mouse.click(Button.left)
        time.sleep(click_delay)

def on_press(key):
    global clicking
    if key == start_stop_key:
        clicking = not clicking

def set_click_delay():
    global click_delay
    try:
        click_delay = float(delay_entry.get())
    except ValueError:
        delay_entry.delete(0, tk.END)
        delay_entry.insert(0, "Invalid")

def start_gui():
    global delay_entry
    root = tk.Tk()
    root.title("AutoClicker")
    
    tk.Label(root, text="Click Interval (seconds):").pack()
    delay_entry = tk.Entry(root)
    delay_entry.pack()
    delay_entry.insert(0, str(click_delay))
    
    set_button = tk.Button(root, text="Set Interval", command=set_click_delay)
    set_button.pack()
    
    root.mainloop()

t = threading.Thread(target=clicker)
t.daemon = True
t.start()

gui_thread = threading.Thread(target=start_gui)
gui_thread.daemon = True
gui_thread.start()

with Listener(on_press=on_press) as listener:
    listener.join()
