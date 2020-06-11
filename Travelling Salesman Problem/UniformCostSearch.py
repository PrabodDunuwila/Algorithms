import random
from queue import PriorityQueue

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


def traverse(number_of_cities, path, matrix):
    """
    Identify next possible child nodes for a parent node.
    If the agent is in the goal state, then return a flag.
    :param matrix:
    :param number_of_cities: integer value with the number of cities
    :param path: list that contains list of path with nodes.
    :return: list of nodes list for possible paths
    """
    next_possible_nodes = []  # possible nodes to visit next for a parent node
    result = []
    result_with_cost = []
    last_nodes_in_path = []  # list of already visited cities
    starting_cost = path[0]
    path = path[1]  # since path is the second element of the tuple
    last_city_visited = path[-1][1]

    for nodes in path:
        last_nodes_in_path.append(nodes[1])

    all_cities = [*range(0, number_of_cities, 1)]  # list of all possible cities
    not_visited_nodes = [x for x in all_cities if x not in last_nodes_in_path]  # cities not visited yet

    # If the agent have came back to the starting point. This is the goal state of the agent.
    if last_city_visited == 0 and not not_visited_nodes:
        return 0

    # if there are no any node left to visit return to starting point
    if not not_visited_nodes:
        temp = list(path)
        last_node = [last_city_visited, 0]
        temp.append(last_node)
        result.append(temp)

        # calculate cost for each path and make a list of tuples
        cost = starting_cost + matrix[result[0][-1][0]][result[0][-1][1]]
        t = (cost, result[0])
        result_with_cost.append(t)

        return result_with_cost

    # identify not visited nodes
    for i in not_visited_nodes:
        node = [last_city_visited, i]
        next_possible_nodes.append(node)

    # append next_possible_nodes with the path
    for i in range(0, len(next_possible_nodes)):
        temp = list(path)
        temp.append(next_possible_nodes[i])
        result.append(temp)

    # calculate cost for each path and make a list of tuples
    for path in result:
        temp_cost = starting_cost
        cost = temp_cost + matrix[path[-1][0]][path[-1][1]]
        t = (cost, path)
        result_with_cost.append(t)

    return result_with_cost


def search(number_of_cities, matrix):
    """
    Use DFS or BFS and search the optimal path.
    :param number_of_cities: the number of cities
    :param matrix: matrix with cost/distance between cities
    :return: returns optimal path and it's cost as a tuple
    """
    # Agent start from city 0 which has coordinates of [0, 0]
    starting_node = (0, [[0, 0]])
    # Keep paths with their costs to return to initial node.
    city_cost_dict = {}
    # Use a priority queue
    nodes = PriorityQueue()
    nodes.put(starting_node)

    while not nodes.empty():
        path = nodes.get()
        # if all nodes for a particular path have been visited, store path and cost in a dictionary.
        if path[1] != [[0, 0]] and path[1][-1][1] == 0:
            tuple_of_path = tuple(tuple(x) for x in path[1])
            city_cost_dict[tuple_of_path] = path[0]
            break
        # Identify next possible child nodes of the parent
        next_paths = traverse(number_of_cities, path, matrix)
        # If a particular path is not in the goal state then put to the priority queue.
        if next_paths != 0:
            for i in next_paths:
                nodes.put(i)

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
    optimal_path, cost_for_optimal_path = search(number_of_cities, matrix)
    print("Optimal path is {} with a cost of {} ".format(optimal_path, cost_for_optimal_path))


if __name__ == "__main__":
    main()
