import tkinter as tk
import random

def draw_snake():
    canvas.delete("snake")
    for segment in snake:
        canvas.create_rectangle(segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill="green", tag="snake")

def draw_food():
    canvas.delete("food")
    canvas.create_rectangle(food[0], food[1], food[0] + 10, food[1] + 10, fill="red", tag="food")

def move_snake():
    global snake, food

    head_x, head_y = snake[0]
    if direction == "Up":
        new_head = (head_x, head_y - 10)
    elif direction == "Down":
        new_head = (head_x, head_y + 10)
    elif direction == "Left":
        new_head = (head_x - 10, head_y)
    elif direction == "Right":
        new_head = (head_x + 10, head_y)

    if new_head[0] < 0 or new_head[0] >= 600 or new_head[1] < 0 or new_head[1] >= 400 or new_head in snake:
        game_over()
        return

    if new_head == food:
        snake = [new_head] + snake
        food = (random.randint(0, 59) * 10, random.randint(0, 39) * 10)
        draw_food()
    else:
        snake = [new_head] + snake[:-1]

    draw_snake()
    root.after(100, move_snake)

def change_direction(new_direction):
    global direction
    if new_direction == "Up" and direction != "Down":
        direction = new_direction
    elif new_direction == "Down" and direction != "Up":
        direction = new_direction
    elif new_direction == "Left" and direction != "Right":
        direction = new_direction
    elif new_direction == "Right" and direction != "Left":
        direction = new_direction

def game_over():
    canvas.create_text(300, 200, text="Game Over", fill="white", font=("Arial", 24))

root = tk.Tk()
root.title("Simple Snake Game")

canvas = tk.Canvas(root, width=600, height=400, bg="black")
canvas.pack()

snake = [(20, 20), (20, 30), (20, 40)]
food = (100, 100)
direction = "Right"

draw_snake()
draw_food()
move_snake()

root.bind("<Up>", lambda event: change_direction("Up"))
root.bind("<Down>", lambda event: change_direction("Down"))
root.bind("<Left>", lambda event: change_direction("Left"))
root.bind("<Right>", lambda event: change_direction("Right"))

root.mainloop()
