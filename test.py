import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
def bezier_brute_force(initial_points, num_of_iterations):
    num_created_points = 2 ** num_of_iterations - 1
    length = num_created_points + 2
    final_points = [(0, 0)] * length
    final_points[0] = initial_points[0]
    for i in range(num_created_points):
        t = (i + 1) / (num_created_points + 1)
        x = ((1 - t) ** 2) * initial_points[0][0] + ((1-t) * t) * initial_points[1][0] + (t ** 2) * initial_points[2][0]
        y = ((1 - t) ** 2) * initial_points[0][1] + ((1-t) * t) * initial_points[1][1] + (t ** 2) * initial_points[2][1]
        final_points[i+1] = (x,y)
    final_points[length-1] = initial_points[2]
    return final_points

def plot_points(result,control,runtime):
    curve_x, curve_y = zip(*result)
    control_x, control_y = zip(*control)

    plt.plot(curve_x, curve_y, label='Bezier Curve')
    plt.plot(control_x, control_y, color='red', label='Control Points')
    plt.title(f"Bezier Curve - Runtime (overall): {runtime} ms")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

def animate(iteration, controlpoints, ax, runtime,n):
    ax.clear()
    if (n ==1):
        curve = bezier_brute_force(controlpoints,iteration)
    elif (n==2):
        curve = bezier_dnc(controlpoints, iteration)

    
    ax.plot(*zip(*curve), marker='o', color='b')
    ax.plot(*zip(*controlpoints), marker='o', color='r')
    ax.set_title(f"Iteration {iteration} - Runtime (overall): {runtime} ms")
    ax.set_aspect('equal', 'box')
    ax.grid(True)


def animate_bezier(controlpoints, iteration, runtime_ms,n):
    fig, ax = plt.subplots()
    
    def animate_wrapper(iteration):
        animate(iteration, controlpoints, ax, runtime_ms,n)
    
    ani = FuncAnimation(fig, animate_wrapper, frames=iteration+1, interval=1000, repeat=False)
    plt.show()

# Example usage:
control_points = [(0, 0), (5, 1), (2, -1)]  # Example control points
num_of_iterations = 5  # Example number of iterations
start_time = time.time()
curve = bezier_brute_force(control_points,num_of_iterations)
end_time = time.time()
runtime_ms = (end_time-start_time) * 1000
print(runtime_ms)
# plot_points(curve,control_points,1000)
animate_bezier(control_points,num_of_iterations,1000,1)
