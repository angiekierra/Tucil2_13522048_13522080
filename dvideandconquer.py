
# blum general


import matplotlib.pyplot as plt

def mid_point(point1,point2):
    return (point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2

def bezier_curve(controlpoints,iteration):
    if iteration == 0:
        return controlpoints
    else:
        
        left_mid = mid_point(controlpoints[0],controlpoints[1])
        right_mid = mid_point(controlpoints[1],controlpoints[2])
        mids = mid_point(left_mid,right_mid)

        left_curve = [controlpoints[0],left_mid,mids]
        right_curve = [mids,right_mid,controlpoints[-1]]

        left = bezier_curve(left_curve,iteration-1)
        right = bezier_curve(right_curve,iteration-1)

        return left + right
    
test = [(6,2),(2,4),(7,15)]
it = 10
res = bezier_curve(test,it)
print(res)
# Generate Bezier curve points
curve_points = bezier_curve(test, it)
curve_x, curve_y = zip(*curve_points)
control_x, control_y = zip(*test)

# Plot Bezier curve and control points
plt.plot(curve_x, curve_y, label='Bezier Curve')
plt.scatter(control_x, control_y, color='red', label='Control Points')
plt.title('Bezier Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()