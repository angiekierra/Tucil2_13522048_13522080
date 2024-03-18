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

final_points = bezier_brute_force(initial_points, num_of_iterations)

length = len(final_points)
for i in range(length):
    plt.plot(*zip(final_points[i]), color='red', marker='o')
    plt.pause(0.1)
plt.show()

for x in final_points:
    print(x)