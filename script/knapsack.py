import random
import numpy as np


class KnapsackEDA:
    def __init__(
        self,
        values,
        weights,
        capacity,
        population_size=20,
        generations=100,
        elite_ratio=0.5,
    ):
        if not (0 < elite_ratio <= 1):
            raise ValueError("Elite ratio must be between 0 and 1.")
        self.values = values
        self.weights = weights
        self.capacity = capacity
        self.population_size = population_size
        self.generations = generations
        self.elite_ratio = elite_ratio
        self.n_items = len(values)

    def fitness(self, individual):
        """Calculate fitness of an individual."""
        total_value = sum(v * i for v, i in zip(self.values, individual))
        total_weight = sum(w * i for w, i in zip(self.weights, individual))
        return total_value if total_weight <= self.capacity else 0

    def generate_population(self):
        """Generate the initial population."""
        return [
            random.choices([0, 1], k=self.n_items) for _ in range(self.population_size)
        ]

    def select_elite(self, population, fitness_scores):
        """Select the elite subset based on fitness."""
        elite_size = int(self.elite_ratio * self.population_size)
        sorted_indices = np.argsort(fitness_scores)[::-1]  # Descending order
        return [population[i] for i in sorted_indices[:elite_size]]

    def estimate_distribution(self, elite_population):
        """Estimate the marginal probabilities for each item."""
        elite_array = np.array(elite_population)
        return np.mean(elite_array, axis=0)  # Probability of selecting each item

    def sample_population(self, probabilities):
        """Generate a new population by sampling from the estimated probabilities."""
        return [
            [1 if random.random() < p else 0 for p in probabilities]
            for _ in range(self.population_size)
        ]

    def run(self):
        """Run the Estimation of Distribution Algorithm."""
        population = self.generate_population()

        for generation in range(self.generations):
            # Evaluate fitness of the population
            fitness_scores = [self.fitness(ind) for ind in population]

            # Select elite solutions
            elite_population = self.select_elite(population, fitness_scores)

            # Estimate the probability distribution
            probabilities = self.estimate_distribution(elite_population)

            # Generate a new population
            population = self.sample_population(probabilities)

        # Return the best solution
        fitness_scores = [self.fitness(ind) for ind in population]
        best_index = np.argmax(fitness_scores)
        return population[best_index], fitness_scores[best_index]
