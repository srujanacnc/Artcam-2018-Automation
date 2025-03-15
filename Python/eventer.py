import tkinter as tk
from tkinter import ttk
import os
import sys

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

root = tk.Tk()
root.title("Event Panel")
root.geometry("240x120")
root.resizable(False, False)
root.attributes('-topmost', True)

style = ttk.Style()
style.theme_use('clam')

# Set dark background
root.configure(bg='#1E1E1E')
style.configure('TFrame', background='#1E1E1E')

# Define different button styles with different colors
colors = [
     ('#90A4AE', '#78909C', '#607D8B'),  # Soft Gray-Blue
    ('#A5D6A7', '#81C784', '#66BB6A'),  # Pastel Green
    ('#FFCC80', '#FFB74D', '#FFA726'),  # Muted Orange
    ('#B0BEC5', '#90A4AE', '#78909C'),  # Light Gray
    ('#80CBC4', '#4DB6AC', '#26A69A'),  # Soft Teal
    ('#9FA8DA', '#7986CB', '#5C6BC0'),  # Gentle Blue
    ('#C5CAE9', '#9FA8DA', '#7986CB'),  # Light Lavender
    ('#BCAAA4', '#A1887F', '#8D6E63'),  # Warm Gray
    ('#FFE0B2', '#FFCC80', '#FFB74D'),  # Light Orange
    ('#B39DDB', '#9575CD', '#7E57C2'),  # Soft Purple
    
]

for i, (main_color, active_color, pressed_color) in enumerate(colors):
    style.configure(
        f'Color{i}.TButton',
        font=('Arial', 8),
        padding=1,
        background=main_color,
        foreground='white',
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

events = ["2D toolpath", "3D toolpath", "2D&3D", "mm", "Inch", "Cutting toolpath","V Layer","Messure","Save","<",">","Load"]

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