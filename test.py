import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

import matplotlib.pyplot as plt

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
    

def plot_bezier_dnc_iterations(controlpoints, num_iterations,runtime):
    fig, ax = plt.subplots()
    
    for i in range(num_iterations):
        curve_points = bezier_dnc(controlpoints, i)
        for j in range(len(curve_points)):
            x, y = curve_points[j]
            ax.plot(x, y, marker='o', color='gray') 
            if j > 0:
                prev_x, prev_y = curve_points[j - 1]
                ax.plot([prev_x, x], [prev_y, y], color='gray')  
                
            plt.pause(0.3)  
        
    final_points = bezier_dnc(controlpoints, num_iterations)
    final_x, final_y = zip(*final_points)
    ax.plot(final_x, final_y, marker='o', color='red', label='Final Points', linestyle='-', linewidth=2)

    plt.title(f'Runtime (overall): {runtime} ms')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage:
controlpoints = [(0, 0), (2, 3), (5, 1)]
num_iterations = 3

plot_bezier_dnc_iterations(controlpoints, num_iterations,100)
