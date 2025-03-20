import tkinter as tk
from tkinter import ttk
import os
import sys
import ctypes

def update_event(event_text):
    # Get the directory where the exe/script is located
    if getattr(sys, 'frozen', False):
        # If running as exe (PyInstaller)
        application_path = os.path.dirname(sys.executable)
    else:
        # If running as script
        application_path = os.path.dirname(os.path.abspath(__file__))

    # Create the full path for Event.txt
    event_file_path = os.path.join(application_path, "Event.txt")

    with open(event_file_path, "w") as file:
        file.write(event_text)

def set_dark_title_bar(window):
    """Set the title bar to dark mode on Windows."""
    try:
        # Get the handle of the window
        hwnd = ctypes.windll.user32.GetParent(window.winfo_id())
        # Set the dark mode attribute
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, ctypes.byref(ctypes.c_int(1)), ctypes.sizeof(ctypes.c_int))
    except Exception as e:
        print(f"Failed to set dark title bar: {e}")

root = tk.Tk()
root.title("Event Panel - Dark Theme")
root.geometry("240x120")
root.resizable(False, False)
root.attributes('-topmost', True)

# Set dark title bar (Windows only)
set_dark_title_bar(root)

style = ttk.Style()
style.theme_use('clam')

# Set dark background
root.configure(bg='#1E1E1E')
style.configure('TFrame', background='#1E1E1E')

# Define different button styles with different colors
colors = [
    ('#1a237e', '#283593', '#3949ab'),  # Deep Blue
    ('#311b92', '#4527a0', '#512da8'),  # Deep Purple
    ('#004d40', '#00695c', '#00796b'),  # Teal
    ('#b71c1c', '#c62828', '#d32f2f'),  # Red
    ('#1b5e20', '#2e7d32', '#388e3c'),  # Green
    ('#e65100', '#ef6c00', '#f57c00'),  # Orange
    ('#4a148c', '#6a1b9a', '#7b1fa2'),  # Purple
    ('#01579b', '#0277bd', '#0288d1'),  # Light Blue
    ('#827717', '#9e9d24', '#afb42b'),  # Lime
    ('#3e2723', '#4e342e', '#5d4037'),  # Brown
    ('#880e4f', '#ad1457', '#c2185b'),  # Pink
    ('#1a237e', '#283593', '#3949ab'),  # Deep Blue
]

for i, (main_color, active_color, pressed_color) in enumerate(colors):
    style.configure(
        f'Color{i}.TButton',
        font=('Arial', 10, 'bold'),
        padding=1,
        background=main_color,
        foreground='#FFFFFF',
        borderwidth=1,
        relief='raised'
    )
    style.map(
        f'Color{i}.TButton',
        background=[('active', active_color), ('pressed', pressed_color)]
    )

# Create a main container with grid layout
main_frame = ttk.Frame(root, padding="3", style='TFrame')
main_frame.grid(row=0, column=0, sticky="nsew")

# Configure grid weights
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

events = ["2D", "3D", "2D&3D", "mm", "Inch", "Cutting","V Layer","Messure","Save","<",">","Load",]

# Arrange buttons in a 2x3 grid
for i, event in enumerate(events):
    row = i // 3
    col = i % 3
    color_index = i if i >= 3 else col  # Use different indices for bottom row
    btn = ttk.Button(main_frame, text=event, style=f'Color{color_index}.TButton', command=lambda e=event: update_event(e))
    btn.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
    main_frame.grid_columnconfigure(col, weight=1)
    main_frame.grid_rowconfigure(row, weight=1)

root.mainloop()