import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def mid_point(point1, point2):
    return (point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2


def n_bezier_dnc(control_points, num_of_iterations):
    if num_of_iterations == 1:
        subcontrol_points = [(0, 0)] * (len(control_points) * 2 - 1)
        subcontrol_points[0] = control_points[0]
        subcontrol_points[-1] = control_points[-1]
        new_subcontrol_points = get_subcontrol_points(control_points, subcontrol_points, 0)
        return [control_points[0]] + [new_subcontrol_points[(len(subcontrol_points)-1)//2]] + [control_points[-1]]
    else:
        subcontrol_points = [(0, 0)] * (len(control_points) * 2 - 1)
        subcontrol_points[0] = control_points[0]
        subcontrol_points[-1] = control_points[-1]
        subcontrol_points = get_subcontrol_points(control_points, subcontrol_points, 1)
        # print(subcontrol_points)
        left = n_bezier_dnc(subcontrol_points[:len(control_points)], num_of_iterations - 1)
        right = n_bezier_dnc(subcontrol_points[-len(control_points):], num_of_iterations - 1)
        return left + right

def get_subcontrol_points(control_points, subcontrol_points, counter):
    if len(control_points) == 2:
        new_subcontrol_points = subcontrol_points
        new_subcontrol_points[(len(subcontrol_points)-1)//2] = mid_point(control_points[0], control_points[1])
        return subcontrol_points
    else:
        length = len(control_points) - 1
        mid_points = []
        for i in range(length):
            mid_points.append(mid_point(control_points[i], control_points[i+1]))
        new_subcontrol_points = subcontrol_points
        new_subcontrol_points[counter] = mid_points[0]
        new_subcontrol_points[-(1 + counter)] = mid_points[-1]
        return get_subcontrol_points(mid_points, new_subcontrol_points, counter + 1)
    
# Precompute results for each iteration
def precompute_results_n_bezier(control_points, num_of_iterations):
    results = []
    for i in range(1, num_of_iterations + 1):
        result_points = n_bezier_dnc(control_points, i)
        results.append(result_points)
    return results

def animate_n_bezier(iteration, results, ax, run_time_per_iteration):
    ax.clear()
    result_points = results[iteration]
    curve_x, curve_y = zip(*result_points)
    ax.plot(curve_x, curve_y, marker='o', color='b')
    ax.set_title(f"Iteration {iteration} - Runtime (per iteration): {run_time_per_iteration} ms")
    ax.set_aspect('equal', 'box')
    ax.grid(True)

def animate_bezier_n_bezier(control_points, num_of_iterations, run_time):
    results = precompute_results_n_bezier(control_points, num_of_iterations)
    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, animate_n_bezier, frames=num_of_iterations, fargs=(results, ax, run_time), interval=1000, repeat=False)
    plt.show()

# Example usage:
control_points = [(0, 0), (1, 1), (2, -1), (3, 0)]  # Example control points
num_of_iterations = 5  # Example number of iterations

animate_bezier_n_bezier(control_points, num_of_iterations,122)
