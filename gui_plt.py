import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import simpledialog

def mid_point(point1, point2):
    return (point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2

def bezier_curve(controlpoints, iteration):
    if iteration == 0:
        return [controlpoints[0], mid_point(controlpoints[0], controlpoints[-1]), controlpoints[-1]]
    else:
        left_mid = mid_point(controlpoints[0], controlpoints[1])
        right_mid = mid_point(controlpoints[1], controlpoints[2])
        mids = mid_point(left_mid, right_mid)

        left_curve = [controlpoints[0], left_mid, mids]
        right_curve = [mids, right_mid, controlpoints[-1]]
        left = bezier_curve(left_curve, iteration - 1)
        right = bezier_curve(right_curve, iteration - 1)

        return left + right

def animate(iteration, controlpoints):
    ax.clear()
    curve = bezier_curve(controlpoints, iteration)
    ax.plot(*zip(*curve), marker='o', color='b')
    ax.plot(*zip(*controlpoints), marker='o', color='r')
    ax.set_title(f"Iteration {iteration}")
    ax.set_aspect('equal', 'box')
    ax.grid(True)

def get_control_points_and_iteration():
    root = tk.Tk()
    root.withdraw()
    num_points = simpledialog.askinteger("Number of Control Points", "Enter the number of control points:")
    controlpoints = []
    for i in range(num_points):
        x = simpledialog.askfloat("Control Point", f"Enter x-coordinate for point {i+1}:")
        y = simpledialog.askfloat("Control Point", f"Enter y-coordinate for point {i+1}:")
        controlpoints.append((x, y))
    iteration = simpledialog.askinteger("Iteration", "Enter the number of iterations:")
    return controlpoints, iteration

controlpoints = [(0, 0), (1, 1), (2, 0)]
iteration = 10

fig, ax = plt.subplots()
ani = FuncAnimation(fig, animate, frames=iteration+1, fargs=(controlpoints,), interval=1000, repeat=False)
plt.show()
