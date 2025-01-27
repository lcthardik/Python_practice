import tkinter as tk
import math

# Create the main window
root = tk.Tk()
root.title("Fourier Series Animation")

# Create a canvas widget
canvas = tk.Canvas(root, width=800, height=400, bg='white')
canvas.pack()

# Parameters for the Fourier series
width = 800
height = 400
center_y = height // 2
amplitude = 100
num_terms = 10  # Number of terms in the Fourier series

# Function to draw the Fourier series
def draw_fourier_series(shift):
    canvas.delete("all")
    for x in range(width):
        y = center_y
        for n in range(1, num_terms * 2, 2):
            y += (4 / (math.pi * n)) * amplitude * math.sin(n * (x + shift) * math.pi / width)
        canvas.create_line(x, y, x + 1, y, fill='blue')

# Function to update the Fourier series
def update(frame):
    draw_fourier_series(frame)
    root.after(50, update, frame + 1)

# Start the animation
update(0)

# Start the Tkinter main loop
root.mainloop()