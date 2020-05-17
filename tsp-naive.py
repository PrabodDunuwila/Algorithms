import numpy as np
import matplotlib.pyplot as plt
import sys
import random
import time


def create_matrix(number_of_cities):
    matrix = np.zeros((number_of_cities, number_of_cities))
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for x in range(0, rows):
        for y in range(0, cols):
            if x == y:
                break
            matrix[x,y] = matrix[y,x] = random.randint(1, 100)
    print("Matrix : ")
    print(matrix)
    return matrix
        

def permutation(lst): 
    if len(lst) == 0: 
        return [] 
    if len(lst) == 1: 
        return [lst] 

    l = []
  
    for i in range(len(lst)):
       m = lst[i] 
       remLst = lst[:i] + lst[i+1:] 
       for p in permutation(remLst): 
           l.append([m] + p)
           
    return l


def algorithm(number_of_cities):
    matrix = create_matrix(number_of_cities)
    city_lst = [*range(1, number_of_cities, 1)]
    
    city_permutations = permutation(city_lst)
    
    for p in city_permutations:
        p.insert(0, 0)
        p.append(0)
        '''if len(p) > 3:
            for p in city_permutations:
                new_lst = p[::-1]
                if new_lst in city_permutations:
                    city_permutations.remove(new_lst)'''
    print(city_permutations)
    min_dist = sys.maxsize
    optimal_perm = []
    
    #Find optimal solution
    for perm in city_permutations:
        dist = 0
        for i in range(0, number_of_cities):
            if i != number_of_cities-1:
                dist += matrix[perm[i],perm[i+1]]
            else:
                dist += matrix[perm[i],perm[0]]
        if dist < min_dist:
            min_dist = dist
            optimal_perm = perm
    print("Minimum distance : {}, Optimal route : {}".format(min_dist, optimal_perm))
    return optimal_perm
    
    
def calculate_time(test_cases):
    exec_time = []
    for i in [*range(2, test_cases+1, 1)]:
        start = time.time()
        algorithm(i)
        execution_time = time.time() - start
        exec_time.append(execution_time)
        print("Execution time : {}".format(execution_time))
        print('-------------------------------------')
    plot_graph(test_cases, exec_time)


def plot_graph(test_cases, exec_time):
    x = [*range(2, test_cases+1, 1)]
    plt.plot(x, exec_time)
    plt.xlabel('number of cities')
    plt.ylabel('execution time(s)')
    plt.title('TSP algorithm execution')
    plt.show()

if __name__ == "__main__":
    calculate_time(10)

