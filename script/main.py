#!/usr/bin/env python
from knapsack import KnapsackEDA

if __name__ == "__main__":
    # Define problem
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    # Create KnapsackEDA instance
    knapsack = KnapsackEDA(
        values, weights, capacity, population_size=100, generations=500, elite_ratio=0.4
    )

    # Run the algorithm
    best_solution, best_value = knapsack.run()
    print("Best solution:", best_solution)
    print("Best value:", best_value)
