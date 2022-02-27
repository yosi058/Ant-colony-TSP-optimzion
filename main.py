import random
import numpy as np
from two_opt import RouteFinder
from Antcolony import AntColony
import matplotlib.pyplot as plt
def init_matrix(num):
    names = []
    for j in range(num):
        names.append(chr(ord('A') + j))
    dis_matrix = np.random.randint(1, 150, size=(num, num))
    dis_matrix = list(dis_matrix)

    for index, i in enumerate(dis_matrix):
        i = list(i)
        i[index] = np.inf
    return names, dis_matrix

cities_names, dist_mat = init_matrix(100)
num_of_iterations = 100
route_finder = RouteFinder(dist_mat, cities_names, iterations=num_of_iterations)
best_distance, best_route, y_dis_hill, hill_time = route_finder.solve()

print(best_distance)
print(best_route)
print(y_dis_hill)

distances = np.array(dist_mat)
ant_colony = AntColony(distances,5, 5, num_of_iterations, 0.95, alpha=1, beta=1)
shortest_path, y_dis_ant, ant_time = ant_colony.run()
print("shorted_path: {}".format(shortest_path))
print(y_dis_ant)
x_iterate_hill = list(range(1, num_of_iterations + 1))
x_iterate_ant = x_iterate_hill.copy()
plt.plot(x_iterate_hill, y_dis_hill, label='Hill claiming')
plt.plot(0, y_dis_hill[0], label=f'Hill time:{hill_time} msec', color='white')
plt.plot(x_iterate_ant, y_dis_ant, label='Ant colony')
plt.plot(0, y_dis_ant[0], label=f'Ant time:{ant_time} msec', color='white')
plt.xlabel("iterations")
plt.ylabel("distance")
plt.title(f"num of iterations={num_of_iterations}, num of cities={len(cities_names)}")
plt.legend()
plt.show()
