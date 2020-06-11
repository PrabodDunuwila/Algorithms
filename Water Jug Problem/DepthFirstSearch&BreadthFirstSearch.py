import collections


def get_jugs():
    """
    Get volume of jugs as a input from the user.
    :return: tuple
    """
    print("Enter the volumes of jugs")
    jug1 = int(input("Enter volume of jug 1: "))
    while jug1 < 1:
        jug1 = int(input("Enter volume of jug 1: "))
    jug2 = int(input("Enter volume of jug 2: "))
    while jug2 < 1:
        jug2 = int(input("Enter volume of jug 2: "))
    return jug1, jug2


def get_target():
    """
    Get the target amount of water to fill the jar.
    :return: int
    """
    return int(input("Enter the desired amount of water: "))


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


def operation_performed(old_status, new_status, jugs):
    """
    Return a string for the operation of the current state change
    :param old_status: node with previous status of jugs
    :param new_status: node with current status of jugs
    :param jugs: volume of jugs
    :return: String
    """
    old_status_jug1 = old_status[0]
    old_status_jug2 = old_status[1]
    new_status_jug1 = new_status[0]
    new_status_jug2 = new_status[1]
    max_of_jug1 = jugs[0]
    max_of_jug2 = jugs[1]
    if old_status_jug1 > new_status_jug1 and old_status_jug2 == new_status_jug2:
        return "Select leaf node: Empty {} litre jug".format(max_of_jug1)
    if old_status_jug1 > new_status_jug1:
        return "Select leaf node: Pour {} litre jug into {} litre jug".format(max_of_jug1, max_of_jug2)
    if old_status_jug1 == new_status_jug1 and old_status_jug2 > new_status_jug2:
        return "Select leaf node: Empty {} litre jug".format(max_of_jug2)
    if old_status_jug2 > new_status_jug2:
        return "Select leaf node: Pour {} litre jug into {} litre jug".format(max_of_jug2, max_of_jug1)
    if old_status_jug1 < new_status_jug1:
        return "Select leaf node: Fill {} litre jug".format(max_of_jug1)
    if old_status_jug2 < new_status_jug2:
        return "Select leaf node: Fill {} litre jug".format(max_of_jug2)


def next_operation(path, check_dict, jugs):
    """
    Return a list of all possible operations if they are not already visited before. There are 6 different operations
    identified.
    :param path: list of nodes for the current path
    :param check_dict: dictionary with visited nodes
    :param jugs: volume of jugs
    :return:
    """
    print("Identifying next possible operations")

    result = []
    next_nodes = []
    max_first_jug = jugs[0]
    max_second_jug = jugs[1]
    current_jug1 = path[-1][0]
    current_jug2 = path[-1][1]

    # Operation 1: Fill first jug
    node = [max_first_jug, current_jug2]
    if not check_dict.get(tuple(node)):
        next_nodes.append(node)
        print("\tFill first jug: {}".format(node))

    # Operation 2: Fill second jug
    node = [current_jug1, max_second_jug]
    if not check_dict.get(tuple(node)):
        next_nodes.append(node)
        print("\tFill second jug: {}".format(node))

    # Operation 3: Fill first jug using second jug
    node = [min(max_first_jug, current_jug1 + current_jug2)]
    node = [min(max_first_jug, current_jug1 + current_jug2), current_jug2 - (node[0] - current_jug1)]
    if not check_dict.get(tuple(node)):
        next_nodes.append(node)
        print("\tFill first jug using second jug: {}".format(node))

    # Operation 4: Fill second jug using first jug
    node = [min(max_second_jug, current_jug1 + current_jug2)]
    node.insert(0, current_jug1 - (node[0] - current_jug2))     # check why
    if not check_dict.get(tuple(node)):
        next_nodes.append(node)
        print("\tFill second jug using first jug: {}".format(node))

    # Operation 5: Empty first jug
    node = [0, current_jug2]
    if not check_dict.get(tuple(node)):
        next_nodes.append(node)
        print("\tEmpty first jug: {}".format(node))

    # Operation 6: Empty second jug
    node = [current_jug1, 0]
    if not check_dict.get(tuple(node)):
        next_nodes.append(node)
        print("\tEmpty second jug: {}".format(node))

    # create a list of next paths
    for i in range(0, len(next_nodes)):
        temp = list(path)                   # check why
        temp.append(next_nodes[i])
        result.append(temp)

    if len(next_nodes) <= 0:
        print("All nodes are visited")

    return result


def search(jugs, goal_amount, check_dict, is_depth_first_search):
    """
    Search for a path from the starting node [0, 0] to desired state of the jugs
    :param jugs: List of 2 integer values of volumes of jugs
    :param goal_amount: integer value for desired amount of water
    :param check_dict: dictionary to store visited nodes
    :param is_depth_first_search: boolean value for whether to use DFS(True) or BFS(False)
    """
    if is_depth_first_search:
        print("Using Depth First Search algorithm")
    else:
        print("Using Breadth First algorithm")

    starting_node = [[0, 0]]
    goal = []  # Store operations to achieve the desired state
    accomplished = False  # Whether desired state is achieved

    nodes = collections.deque()
    nodes.appendleft(starting_node)

    while len(nodes) != 0:
        path = nodes.popleft()
        check_dict[tuple(path[-1])] = True
        if len(path) >= 2:
            print(operation_performed(path[-2], path[-1], jugs), path[-1])
        if (path[-1][0] == goal_amount and path[-1][1] == 0) or (path[-1][1] == goal_amount and path[-1][0] == 0):
            accomplished = True
            goal = path
            break
        next_op = next_operation(path, check_dict, jugs)
        for i in next_op:
            if is_depth_first_search:
                nodes.appendleft(i)
            else:
                nodes.append(i)
        print("\t{}".format(nodes))

    if accomplished:
        print("\nThe goal is achieved\nPrinting the sequence of the moves...")
        print("Starting from:\t", goal[0])
        for i in range(0, len(goal) - 1):
            print(i + 1, ":", operation_performed(goal[i], goal[i + 1], jugs), goal[i + 1])
    else:
        print("Problem cannot be solved.")


def main():
    jugs = get_jugs()
    goal_amount = get_target()
    check_dict = {}
    is_depth = get_search_algorithm()
    search(jugs, goal_amount, check_dict, is_depth)


if __name__ == '__main__':
    main()
