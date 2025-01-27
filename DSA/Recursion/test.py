import tkinter as tk
import math

# Function to generate Fibonacci sequence
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Function to draw Fibonacci spiral
def draw_fibonacci_spiral(canvas, fib_sequence):
    canvas.delete("all")
    x, y = 400, 400  # Starting point
    angle = 0
    for i in range(2, len(fib_sequence)):
        length = fib_sequence[i] * 10  # Scale the length
        x1 = x + length * math.cos(math.radians(angle))
        y1 = y - length * math.sin(math.radians(angle))
        canvas.create_arc(x - length, y - length, x + length, y + length, start=angle, extent=90, style=tk.ARC)
        x, y = x1, y1
        angle -= 90

# Create the main window
root = tk.Tk()
root.title("Fibonacci Spiral")

# Create a canvas for drawing
canvas = tk.Canvas(root, width=800, height=800, bg="white")
canvas.pack()

# Generate Fibonacci sequence and draw the spiral
n_terms = 10
fib_sequence = fibonacci(n_terms)
draw_fibonacci_spiral(canvas, fib_sequence)

# Run the tkinter main loop
root.mainloop()