import random

grid_side_length = 100

num_points = 100

points = []
sum_x = 0
sum_y = 0
center = [0, 0]

for cur_iteration in range(num_points):
    new_point = (random.random() % grid_side_length, random.random() % grid_side_length)
    sum_x += new_point[0]
    sum_y += new_point[1]
    center = [sum_x / (cur_iteration + 1), sum_y / (cur_iteration + 1)]
    points.append(new_point)
    print(f'new_point #{str(cur_iteration).ljust(2)}: {str(new_point).ljust(44)}, center: {str(center).ljust(50)}')
