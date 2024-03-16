# def bezier_curve(controlpoints,iteration):
#     if iteration == 0:
#         return controlpoints
#     else:
        
#         left_mid = mid_point(controlpoints[0],controlpoints[1])
#         right_mid = mid_point(controlpoints[1],controlpoints[2])
#         mids = mid_point(left_mid,right_mid)

#         left_curve = [controlpoints[0],left_mid,mids]
#         right_curve = [mids,right_mid,controlpoints[-1]]

#         left = bezier_curve(left_curve,iteration-1)
#         right = bezier_curve(right_curve,iteration-1)

#         return left + right

import matplotlib.pyplot as plt
def get_mid_point(point1,point2):
    return (point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2

def general_bezier(control_points,iterations):
    degree = len(control_points) -1

    if (degree == 1 or iterations == 0):
        return [control_points[0], control_points[-1]]
    
    mid_index = degree // 2

    if (degree % 2 != 0): # klo dia control pointnya genap 
        mid_point = get_mid_point(control_points[mid_index] + control_points[mid_index+1])
        left_segment = control_points[:mid_index+1] + [mid_point]
        right_segment = [mid_point] + control_points[mid_index+1:]
    else: # klo dia control poinnya genap
        left_segment = control_points[:mid_index+1]
        right_segment = control_points[mid_index:]

    left_curve = general_bezier(left_segment, iterations-1)
    right_curve = general_bezier(right_segment, iterations -1)

    return left_curve + right_curve



control_points = [(1, 1), (2, 4), (5, 6), (7, 3), (9, 8)]
iterations = 5

curve_points = general_bezier(control_points, iterations)

x_points = [point[0] for point in curve_points]
y_points = [point[1] for point in curve_points]
plt.plot(x_points, y_points, marker='o', linestyle='-')
plt.title('Bezier Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()