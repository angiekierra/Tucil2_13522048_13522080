import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""------------------FUNGSI BRUTE FORCE-------------------- """

def bezier_brute_force(initial_points, num_of_iterations):
    num_created_points = 2 ** num_of_iterations - 1
    length = num_created_points + 2
    final_points = np.zeros(length, dtype=tuple)
    final_points[0] = initial_points[0]
    for i in range(num_created_points):
        t = (i + 1) / (num_created_points + 1)
        x = ((1 - t) ** 2) * initial_points[0][0] + ((1-t) * t) * initial_points[1][0] + (t ** 2) * initial_points[2][0]
        y = ((1 - t) ** 2) * initial_points[0][1] + ((1-t) * t) * initial_points[1][1] + (t ** 2) * initial_points[2][1]
        final_points[i+1] = (x,y)
    final_points[length-1] = initial_points[2]
    return final_points

"""------------------FUNGSI DIVIDE AND CONQUER (KHUSUS 3 TITIK)-------------------- """

def mid_point(point1, point2):
    return (point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2

def bezier_dnc(controlpoints, iteration):
    if iteration == 0:
        return [controlpoints[0], mid_point(controlpoints[0], controlpoints[-1]), controlpoints[-1]]
    else:
        left_mid = mid_point(controlpoints[0], controlpoints[1])
        right_mid = mid_point(controlpoints[1], controlpoints[2])
        mids = mid_point(left_mid, right_mid)

        left_curve = [controlpoints[0], left_mid, mids]
        right_curve = [mids, right_mid, controlpoints[-1]]
        left = bezier_dnc(left_curve, iteration - 1)
        right = bezier_dnc(right_curve, iteration - 1)

        return left + right
    

"""------------------FUNGSI DIVIDE AND CONQUER (UNTUK N TITIK)-------------------- """

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
    


"""------------------FUNGSI VISUALISASI TITIK-------------------- """

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
    curve = bezier_dnc(controlpoints, iteration)
    ax.plot(*zip(*curve), marker='o', color='b')
    ax.plot(*zip(*controlpoints), marker='o', color='r')
    ax.set_title(f"Iteration {iteration}")
    ax.set_aspect('equal', 'box')
    ax.grid(True)

def animate_bezier(controlpoints, iteration):
    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, animate, frames=iteration+1, fargs=(controlpoints, ax), interval=1000, repeat=False)
    plt.show()
