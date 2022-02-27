import random2
import time

from solver import Solver


class RouteFinder:
    def __init__(self, distance_matrix, cities_names, iterations=5, writer_flag=False, method='py2opt'):
        self.distance_matrix = distance_matrix
        self.iterations = iterations
        self.writer_flag = writer_flag
        self.cities_names = cities_names

    def solve(self):
        start_time = round(time.time() * 1000)
        elapsed_time = 0
        iteration = 0
        best_distance = 0
        best_route = []
        best_distances = []
        iterate_dis = []
        best_time = 0

        while iteration < self.iterations:
            num_cities = len(self.distance_matrix)
            print(round(elapsed_time), 'msec')
            initial_route = [0] + random2.sample(range(1, num_cities), num_cities - 1)
            tsp = Solver(self.distance_matrix, initial_route)
            new_route, new_distance, distances = tsp.two_opt()
            # iterate_dis.append(new_distance)

            if iteration == 0:
                best_distance = new_distance
                best_route = new_route
            else:
                pass
            if new_distance < best_distance:
                best_distance = new_distance
                best_route = new_route
                best_distances = distances
                best_time = round(time.time() * 1000) - start_time
                iterate_dis.append(new_distance)
            else:
                iterate_dis.append(best_distance)
            elapsed_time = round(time.time() * 1000) - start_time
            iteration += 1
        if self.cities_names:
            best_route = [self.cities_names[i] for i in best_route]
            return best_distance, best_route, iterate_dis, best_time
        else:
            return best_distance, best_route, iterate_dis, best_time
