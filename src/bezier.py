import matplotlib.pyplot as plt

initial_points = []
for i in range(3):
    initial_points.append(tuple(map(int, input().split(','))))

num_of_iterations =  int(input("Jumlah iterasi: "))

def bezier_brute_force(initial_points, num_of_iterations):
    num_created_points = pow(2, num_of_iterations) - 1
    length = num_created_points + 2
    final_points = [(0, 0)] * length
    final_points[0] = initial_points[0]
    for i in range(num_created_points):
        t = (i + 1) / (num_created_points + 1)
        x = pow((1 - t),2) * initial_points[0][0] + (2 * (1-t) * t) * initial_points[1][0] + pow(t,2) * initial_points[2][0]
        y = pow((1 - t),2) * initial_points[0][1] + (2 * (1-t) * t) * initial_points[1][1] + pow(t,2) * initial_points[2][1]
        final_points[i+1] = (x,y)
    final_points[length-1] = initial_points[2]
    return final_points

# final_points = bezier_brute_force(initial_points, num_of_iterations)
# # print(final_points)
# length = len(final_points)
# # print(length)
# for i in range(length):
#     plt.plot(*zip(final_points[i]), color='red', marker='o')
#     plt.pause(0.1)
# plt.show()

# for x in final_points:
#     print(x)

final_points = bezier_brute_force(initial_points, num_of_iterations)
length = len(final_points)


def plot_by_point(controlpoint,result):
    for i in range(len(result)):
        plt.plot(*zip(result[i]), color='red', marker='o')
        if i < length - 1:
            plt.plot([result[i][0], result[i+1][0]], [result[i][1], result[i+1][1]], color='r')
        plt.pause(0.1)
    plt.plot(*zip(controlpoint), color='b', marker='o')


def plot_per_points(result, control, runtime):
    curve_x, curve_y = [], []
    control_x, control_y = zip(*control)

    plt.plot(control_x, control_y, color='red', label='Control Points')

    plt.title(f"Bezier Curve - Runtime (overall): {runtime} ms")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)

    for i in range(len(result)):
        curve_x.append(result[i][0])
        curve_y.append(result[i][1])
        plt.plot(curve_x, curve_y, marker='o', color='b')
        if i > 0:
            plt.plot([result[i-1][0], result[i][0]], [result[i-1][1], result[i][1]], color='b')
        plt.pause(0.3)  
    plt.show()


plt.show()