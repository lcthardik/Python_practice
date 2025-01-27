import tkinter as tk
import math
import argparse

# Define the lengths of the robotic arm links
link1_length = 100
link2_length = 100

# Define the initial joint angles (in radians)
theta1 = math.radians(0)
theta2 = math.radians(0)

def inverse_kinematics(x, y):
    try:
        q2 = math.acos((x**2 + y**2 - link1_length**2 - link2_length**2) / (2 * link1_length * link2_length))
        q1 = math.atan2(y, x) - math.atan2(link2_length * math.sin(q2), link1_length + link2_length * math.cos(q2))
        return q1, q2
    except ValueError:
        print("Target position is unreachable")
        return None, None

def draw_dot(canvas, x, y, radius=4):
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="black")

def draw_arm(canvas, theta1, theta2):
    x1 = 200 + link1_length * math.cos(theta1)
    y1 = 200 - link1_length * math.sin(theta1)
    x2 = x1 + link2_length * math.cos(theta1 + theta2)
    y2 = y1 - link2_length * math.sin(theta1 + theta2)

    canvas.delete("all")
    canvas.create_oval(195, 195, 205, 205, fill="black")
    canvas.create_line(200, 200, x1, y1, width=5, fill="blue")
    canvas.create_line(x1, y1, x2, y2, width=5, fill="red")
    draw_dot(canvas, x1, y1)
    draw_dot(canvas, x2, y2)

def update_angles(canvas, target_x, target_y):
    global theta1, theta2

    in_theta1, in_theta2 = inverse_kinematics(target_x, target_y)

    if in_theta1 is not None and in_theta2 is not None:
        if abs(math.degrees(theta1) - math.degrees(in_theta1)) > 1:
            theta1 += math.radians(1) if in_theta1 > theta1 else -math.radians(1)
        if abs(math.degrees(theta2) - math.degrees(in_theta2)) > 1:
            theta2 += math.radians(1) if in_theta2 > theta2 else -math.radians(1)
    
    draw_arm(canvas, theta1, theta2)
    draw_dot(canvas, 200+target_x, 200-target_y,6)
    canvas.after(10, update_angles, canvas, target_x, target_y)

def main():
    parser = argparse.ArgumentParser(description="2-DOF Robotic Arm Animation")
    parser.add_argument("target_x", type=float, help="Target X position for the end-effector")
    parser.add_argument("target_y", type=float, help="Target Y position for the end-effector")
    args = parser.parse_args()

    root = tk.Tk()
    root.title("2-DOF Robotic Arm Animation")

    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    update_angles(canvas, args.target_x, args.target_y)
    root.mainloop()

if __name__ == "__main__":
    main()