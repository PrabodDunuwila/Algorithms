# TSP

Implementations for Travelling Salesman Problem using,
	1. mlrose library
	2. implement algorithm from scratch using naive method.
	3. using depth first search
	4. using breadth first search
	5. using uniform cost search

Implement algorithm from scratch using naive method

The algorithm used to solve the TSP has the following steps.
	1. Create a matrix with the distances for each city using random values.
	2. Generate all the permutations of the routes between the cities to start travelling from ‘city zero’ and visit all other cities exactly once before returning to the ‘city zero’ back. The permutations include only unique routes.
	3. Then find the total distance for each route.
	4. Find the minimum distance and its route.

Console output produces a log  for the following values (Figure 1)
	1. Matrix of distance
	2. Minimum distance / Optimal route
	3. Execution time

The execution time against the number of cities was plotted for the algorithm used for the calculation of TSP.


