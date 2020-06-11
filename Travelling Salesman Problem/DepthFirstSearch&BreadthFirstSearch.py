import collections
import random

import numpy as np


def create_matrix():
    """
    Get user input for the number of cities and generate a matrix of random distance/cost to travel from one city to
    another.
    :return: returns a matrix of cost between the cities.
    """
    number_of_cities = int(input("Enter the number of cities: "))
    while number_of_cities < 2:
        print("Enter a number more than 2.")
        number_of_cities = int(input("Enter the number of cities: "))
    matrix = np.zeros((number_of_cities, number_of_cities))
    rows = cols = matrix.shape[0]
    for x in range(0, rows):
        for y in range(0, cols):
            if x == y:
                break
            matrix[x, y] = matrix[y, x] = random.randint(1, 100)
    print("Matrix : ")
    print(matrix)
    return matrix


def get_search_algorithm():
    """
    Get what algorithm is required to solve the problem.
        1. Depth First Search : return True
        2. Breadth First Search : return False
    :return: boolean
    """
    algorithm = input("Enter 'd' for DFS or 'b' for BFS: ")
    while algorithm != 'd' and algorithm != 'b':
        algorithm = input("Enter 'd' for DFS or 'b' for BFS: ")
    return algorithm == 'd'


def traverse(number_of_cities, path):
    """
    Identify next possible child nodes for a parent node.
    If the agent is in the goal state, then return a flag.
    :param number_of_cities: integer value with the number of cities
    :param path: list that contains list of path with nodes.
    :return: list of nodes list for possible paths
    """
    next_possible_nodes = []  # possible nodes to visit next for a parent node
    result = []
    last_nodes_in_path = []  # list of already visited cities

    for node in path:
        last_nodes_in_path.append(node[1])

    all_cities = [*range(0, number_of_cities, 1)]  # list of all possible cities
    not_visited_nodes = [x for x in all_cities if x not in last_nodes_in_path]  # cities not visited yet

    # If the agent have came back to the starting point. This is the goal state of the agent.
    if path[-1][1] == 0 and not not_visited_nodes:
        return 0

    # if there are no any node left to visit return to starting point
    if not not_visited_nodes:
        temp = list(path)
        last_node = [path[-1][1], 0]
        temp.append(last_node)
        result.append(temp)
        return result

    # identify not visited nodes
    for i in not_visited_nodes:
        node = [path[-1][1], i]
        next_possible_nodes.append(node)

    # append next_possible_nodes with the path
    for i in range(0, len(next_possible_nodes)):
        temp = list(path)
        temp.append(next_possible_nodes[i])
        result.append(temp)

    return result


def calculate_cost(matrix, path):
    cost = 0
    for [x, y] in path:
        cost += matrix[x][y]
    return cost


def search(number_of_cities, matrix, is_depth):
    """
    Use DFS or BFS and search the optimal path.
    :param number_of_cities: the number of cities
    :param matrix: matrix with cost/distance between cities
    :param is_depth: whether to use DFS or BFS
    :return: returns optimal path and it's cost as a tuple
    """
    if is_depth:
        print("Using Depth First Search algorithm")
    else:
        print("Using Breadth First algorithm")

    # Agent start from city 0 which has coordinates of [0, 0]
    starting_node = [[0, 0]]
    city_cost_dict = {}
    nodes = collections.deque()
    nodes.appendleft(starting_node)

    while len(nodes) != 0:
        path = nodes.popleft()
        # if all nodes for a particular path have been visited, calculate cost and store in a dictionary.
        if path[-1] != [0, 0] and path[-1][1] == 0:
            tuple_of_path = tuple(tuple(x) for x in path)
            city_cost_dict[tuple_of_path] = calculate_cost(matrix, path)
        # Identify next possible child nodes of the parent
        next_paths = traverse(number_of_cities, path)
        # If a particular path is not in the goal state then do the append operations accordingly based on DFS and BFS.
        if next_paths != 0:
            for i in next_paths:
                if is_depth:
                    nodes.appendleft(i)
                else:
                    nodes.append(i)

    optimal_path = min(city_cost_dict, key=city_cost_dict.get)
    cost_for_optimal_path = city_cost_dict[optimal_path]

    return optimal_path, cost_for_optimal_path


def main():
    """
    Agent get the inputs and perform the actions to identify the path with minimum cost using DFS or BFS.
    :return: optimal path to travel all cities.
    """
    matrix = create_matrix()
    number_of_cities = matrix.shape[0]
    is_depth = get_search_algorithm()
    optimal_path, cost_for_optimal_path = search(number_of_cities, matrix, is_depth)
    print("Optimal path is {} with a cost of {} ".format(optimal_path, cost_for_optimal_path))


if __name__ == "__main__":
    main()
