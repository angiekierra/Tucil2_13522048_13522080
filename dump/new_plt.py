import matplotlib.pyplot as plt

def mid_point(point1, point2):
    return (point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2

def dnc(controlpoints, iteration):
    if iteration == 0:
        return [controlpoints[0], mid_point(controlpoints[0], controlpoints[-1]), controlpoints[-1]]
    else:
        left_mid = mid_point(controlpoints[0], controlpoints[1])
        right_mid = mid_point(controlpoints[1], controlpoints[2])
        mids = mid_point(left_mid, right_mid)

        left_curve = [controlpoints[0], left_mid, mids]
        right_curve = [mids, right_mid, controlpoints[-1]]
        left = dnc(left_curve, iteration - 1)
        right = dnc(right_curve, iteration - 1)

        return left + right

# Define control points
controlpoints = [(1, 2), (5, 4), (7, 2)]

# Number of iterations
iterations = 4


# Plot control points
plt.scatter(*zip(*controlpoints), color='red', label='Control Points')

# Plot each iteration of the Bezier curve
for i in range(1,iterations):
    curve_points = dnc(controlpoints, i)
    if i == iterations - 1:
        plt.plot(*zip(*curve_points), label=f'Iteration {i}', linewidth=2)  # Make last iteration bolder
    else:
        plt.plot(*zip(*curve_points), label=f'Iteration {i}')

# Add legend and show plot
plt.legend()
plt.title('Bezier Curve Iterations')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
