
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
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
    

def plot_points(result,control):
    curve_x, curve_y = zip(*result)
    control_x, control_y = zip(*control)

    plt.plot(curve_x, curve_y, label='Bezier Curve')
    plt.scatter(control_x, control_y, color='red', label='Control Points')
    plt.title('Bezier Curve')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

def animate(iteration, controlpoints, ax):
    ax.clear()
    curve = bezier_curve(controlpoints, iteration)
    ax.plot(*zip(*curve), marker='o', color='b')
    ax.plot(*zip(*controlpoints), marker='o', color='r')
    ax.set_title(f"Iteration {iteration}")
    ax.set_aspect('equal', 'box')
    ax.grid(True)

def animate_bezier(controlpoints, iteration):
    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, animate, frames=iteration+1, fargs=(controlpoints, ax), interval=1000, repeat=False)
    plt.show()

test = [(1,2),(5,4),(7,2)]
it = 10
res = bezier_curve(test,it)
# print(res)
curve_points = bezier_curve(test, it)
plot_points(curve_points,test)
animate_bezier(test, it)






















