# TSP

<pre>
Implementations for Travelling Salesman Problem using,
    1. using mlrose library
    2. using naive method
    3. using Depth First Search and Breadth First Search
    4. using Uniform Cost Search
</pre>

<pre>
1. Using mlrose library
    - Provide a list of coordinates and get a best state.
</pre>

<pre>
2. Naive method
    - Create a matrix with the distances for each city using random values.
    - Generate all the permutations of the routes between the cities to start travelling from ‘city zero’ and visit all other cities exactly once before returning to the ‘city zero’ back. The permutations include only unique routes.
    - Then find the total distance for each route.
    - Find the minimum distance and its route.
</pre>

<pre>
3. Depth First Search and Breadth First Search
    - Request user to input the matrix size
    - Generate a matrix with random cost values.
    - Request user to whether to use DFS or BFS to solve the problem
    - Output the optimal path
</pre>

<pre>
4. Uniform Cost Search algorithm
    - Request user to input the matrix size
    - Generate a matrix with random cost values.
    - Run the algorithm and print out the UCS path with the cost.
</pre>
