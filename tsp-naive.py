#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random

number_of_cities = 4

matrix = np.zeros((number_of_cities, number_of_cities))

print(matrix)

rows = matrix.shape[0]
cols = matrix.shape[1]

for x in range(0, rows):
    for y in range(0, cols):
        if x == y:
            break
        num = random.randint(1, 100)
        matrix[x,y] = num
        matrix[y,x] = num

print(matrix)

def permutation(lst): 
    if len(lst) == 0: 
        return [] 
    if len(lst) == 1: 
        return [lst] 

    l = [] # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(lst)): 
       m = lst[i] 
  
       # Extract lst[i] or m from the list.  remLst is 
       # remaining list 
       remLst = lst[:i] + lst[i+1:] 
  
       # Generating all permutations where m is first 
       # element 
       for p in permutation(remLst): 
           l.append([m] + p)
    return l

city_lst =  [*range(0, number_of_cities, 1)]

city_permutations = permutation(city_lst)

print(city_permutations)

print(len(city_permutations))

min_dist = 100 * number_of_cities
optimal_perm = []

for perm in city_permutations:
    dist = 0
    print(perm)
    for i in range(0, number_of_cities):
        if i != number_of_cities-1:
            print("{}-{}:{}".format(perm[i], perm[i+1], matrix[perm[i],perm[i+1]]))
            dist += matrix[perm[i],perm[i+1]]
        else:
            print("{}-{}:{}".format(perm[i], perm[0], matrix[perm[i],perm[0]]))
            dist += matrix[perm[i],perm[0]]
    print(dist)
    if dist < min_dist:
        min_dist = dist
        optimal_perm = perm
        
print(min_dist)
optimal_perm.append(optimal_perm[0])
print(optimal_perm)
        
        