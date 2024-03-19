import matplotlib.pyplot as plt

def mid_point(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def bezier_dnc(control_points, num_of_iterations):
    plt.plot(*zip(*control_points), color = 'grey', marker='o')
    plt.pause(0.5)
    if num_of_iterations == 1:
        subcontrol_points = [(0, 0)] * (len(control_points) * 2 - 3)
        subcontrol_points[0] = control_points[0]
        subcontrol_points[-1] = control_points[-1]
        new_subcontrol_points = get_subcontrol_points(control_points, subcontrol_points, 0)
        points_plotted = []
        for x in new_subcontrol_points:
            if x not in control_points:
                points_plotted.append(x)
        plt.plot(*zip(*points_plotted), color = 'grey', marker='o')
        plt.pause(0.5)
        final_points = [control_points[0]] + [new_subcontrol_points[(len(subcontrol_points)-1)//2]] + [control_points[-1]]
        plt.plot(*zip(*final_points), color = 'red', marker='o')
        plt.pause(0.5)
        return final_points
    else:
        subcontrol_points = [(0, 0)] * (len(control_points) * 2 - 1)
        subcontrol_points[0] = control_points[0]
        subcontrol_points[-1] = control_points[-1]
        subcontrol_points = get_subcontrol_points(control_points, subcontrol_points, 1)
        left = bezier_dnc(subcontrol_points[:len(control_points)], num_of_iterations - 1)
        right = bezier_dnc(subcontrol_points[-len(control_points):], num_of_iterations - 1)
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

num_control_points = int(input("Jumlah Titik: "))
control_points = []
for i in range(num_control_points):
    control_points.append(tuple(map(int, input().split(','))))

num_of_iterations = int(input("Jumlah Iterasi: "))

# plt.figure()
# final_curve = bezier_dnc(control_points, num_of_iterations)
# plt.show()
# for x in final_curve:
#     print(x)

def plot_per_points_ndnc(control_points, num_of_iterations, runtime):
    _, ax = plt.subplots()
    
    def bezier_dnc(control_points, num_of_iterations):
        if num_of_iterations == 1:
            subcontrol_points = [(0, 0)] * (len(control_points) * 2 - 3)
            subcontrol_points[0] = control_points[0]
            subcontrol_points[-1] = control_points[-1]
            new_subcontrol_points = get_subcontrol_points(control_points, subcontrol_points, 0)
            points_plotted = []
            for x in new_subcontrol_points:
                if x not in control_points:
                    points_plotted.append(x)
            ax.plot(*zip(*points_plotted), color='grey', marker='o')
            plt.pause(0.5)
            final_points = [control_points[0]] + [new_subcontrol_points[(len(subcontrol_points)-1)//2]] + [control_points[-1]]
            ax.plot(*zip(*final_points), color='red', marker='o')
            plt.pause(0.5)
            return final_points
        else:
            subcontrol_points = [(0, 0)] * (len(control_points) * 2 - 1)
            subcontrol_points[0] = control_points[0]
            subcontrol_points[-1] = control_points[-1]
            subcontrol_points = get_subcontrol_points(control_points, subcontrol_points, 1)
            ax.plot(*zip(*subcontrol_points), color='grey', marker='o')
            plt.pause(0.5)
            left = bezier_dnc(subcontrol_points[:len(control_points)], num_of_iterations - 1)
            right = bezier_dnc(subcontrol_points[-len(control_points):], num_of_iterations - 1)
            return left + right
        
    custom_legend = [
        plt.Line2D([0], [0], color='grey', marker='o', linestyle='', label='Control Points'),
        plt.Line2D([0], [0], color='red', marker='o', linestyle='', label='Bezier Curve')
    ]
    ax.set_title(f"Iteration: {num_of_iterations} - Runtime (overall): {runtime} ms")
    ax.legend(handles=custom_legend)
    ax.set_aspect('equal', 'box')
    ax.grid(True)
    ax.plot(*zip(*control_points), color='grey', marker='o')
    plt.pause(0.5)
    bezier_dnc(control_points, num_of_iterations)
    plt.show()

plot_per_points_ndnc(control_points, num_of_iterations,500)