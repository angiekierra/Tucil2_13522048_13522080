import matplotlib.pyplot as plt

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
    
def n_bezier_curve(controlpoints, iteration):
    if iteration == 0:
        return controlpoints
    else:
        if len(controlpoints) == 3:
            return bezier_curve(controlpoints, iteration - 1)
        
        middle = len(controlpoints) // 2
        if (len(controlpoints) % 2 == 0):
            mid = mid_point(controlpoints[middle], controlpoints[middle + 1])  
            left_segment = controlpoints[:middle + 1] + [mid]  
            right_segment = [mid] + controlpoints[middle:]  
        else:
            left_segment = controlpoints[:middle + 1]
            right_segment = controlpoints[middle:]
        
        
        left = n_bezier_curve(left_segment, iteration - 1)
        right = n_bezier_curve(right_segment, iteration - 1)


        return left + right

def plot_curve(curve_points):
    x = [p[0] for p in curve_points]
    y = [p[1] for p in curve_points]
    plt.plot(x, y, marker='o')


control_points = [(0, 0), (1, 2), (3, 1), (4, 3), (5, 0),(6,7),(2,7)]
iterations = 10
curve_points = n_bezier_curve(control_points, iterations)

plot_curve(control_points)
plot_curve(curve_points)

plt.title('Bezier Curve')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
