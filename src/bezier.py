import numpy as np

initial_points = np.zeros(3, dtype=tuple)
for i in range(3):
    initial_points[i] = tuple(map(int, input().split(',')))

num_of_iterations =  int(input("Jumlah iterasi: "))

def bezier_brute_force(initial_points, num_of_iterations):
    num_created_points = 2 ** num_of_iterations - 1
    # print(num_of_points)
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

final_points = bezier_brute_force(initial_points, num_of_iterations)

for x in final_points:
    print(x)