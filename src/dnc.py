def mid_point(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def bezier_dnc(control_points, num_of_iterations):
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

num_control_points = int(input("Jumlah titik: "))
control_points = []
for i in range(num_control_points):
    control_points.append(tuple(map(int, input().split(','))))

num_of_iterations = int(input("Jumlah iterasi: "))
final_curve = bezier_dnc(control_points, num_of_iterations)
for x in final_curve:
    print(x)
