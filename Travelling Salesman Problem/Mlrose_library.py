import mlrose

if __name__ == "__main__":
    # Create list of city coordinates
    coord_list = [(1, 1), (4, 2), (5, 2), (6, 4), (4, 4), (3, 6), (1, 5), (2, 3)]

    # Initialize fitness function object using coord_list
    fitness_coord = mlrose.TravellingSales(coords=coord_list)

    problem_fit = mlrose.TSPOpt(length=8, fitness_fn=fitness_coord, maximize=False)

    # Solve problem using the genetic algorithm
    best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob=0.2, max_attempts=100, random_state=2)

    print('The best state found is: ', best_state)

    print('The fitness at the best state is: ', best_fitness)
