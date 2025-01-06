#!/usr/bin/env python
import unittest
import numpy as np
import os, sys

sys.path.append(os.path.join(os.path.join("../script")))
root_path = os.path.abspath("..")
if root_path not in sys.path:
    sys.path.insert(0, root_path)
from knapsack import KnapsackEDA


class TestKnapsackEDA(unittest.TestCase):
    def setUp(self):
        """Set up test cases with predefined problem instances."""
        # Problem instance 1
        self.values1 = [60, 100, 120]
        self.weights1 = [10, 20, 30]
        self.capacity1 = 50

        # Problem instance 2
        self.values2 = [10, 40, 30, 50]
        self.weights2 = [5, 10, 15, 20]
        self.capacity2 = 30

    def test_best_solution_instance1(self):
        """Test best solution for problem instance 1."""
        knapsack = KnapsackEDA(
            values=self.values1,
            weights=self.weights1,
            capacity=self.capacity1,
            population_size=50,
            generations=200,
            elite_ratio=0.4,
        )
        best_solution, best_value = knapsack.run()
        self.assertEqual(sum(best_solution), 2)  # Expecting 2 items selected
        self.assertEqual(best_value, 220)  # Expected total value for the best solution

    def test_best_solution_instance2(self):
        """Test best solution for problem instance 2."""
        knapsack = KnapsackEDA(
            values=self.values2,
            weights=self.weights2,
            capacity=self.capacity2,
            population_size=50,
            generations=200,
            elite_ratio=0.4,
        )
        best_solution, best_value = knapsack.run()
        self.assertTrue(
            best_value <= 90
        )  # Best value should not exceed the total value of all items
        self.assertLessEqual(
            sum(np.array(best_solution) * np.array(self.weights2)), self.capacity2
        )  # Total weight must not exceed capacity

    def test_invalid_capacity(self):
        """Test behavior when the capacity is set to 0."""
        knapsack = KnapsackEDA(
            values=self.values1,
            weights=self.weights1,
            capacity=0,
            population_size=50,
            generations=200,
            elite_ratio=0.4,
        )
        best_solution, best_value = knapsack.run()
        self.assertEqual(sum(best_solution), 0)  # No items can be selected
        self.assertEqual(best_value, 0)  # Total value must be 0

    def test_empty_items(self):
        """Test behavior when no items are provided."""
        knapsack = KnapsackEDA(
            values=[],
            weights=[],
            capacity=50,
            population_size=50,
            generations=200,
            elite_ratio=0.4,
        )
        best_solution, best_value = knapsack.run()
        self.assertEqual(len(best_solution), 0)  # No solution since no items exist
        self.assertEqual(best_value, 0)  # Total value must be 0

    def test_invalid_elite_ratio(self):
        """Test behavior with an invalid elite ratio."""
        with self.assertRaises(ValueError):
            knapsack = KnapsackEDA(
                values=self.values1,
                weights=self.weights1,
                capacity=self.capacity1,
                population_size=50,
                generations=200,
                elite_ratio=1.5,  # Invalid elite ratio
            )

    def test_edge_case_single_item(self):
        """Test edge case with a single item."""
        knapsack = KnapsackEDA(
            values=[100],
            weights=[20],
            capacity=50,
            population_size=50,
            generations=200,
            elite_ratio=0.4,
        )
        best_solution, best_value = knapsack.run()
        self.assertEqual(sum(best_solution), 1)  # Only one item is selected
        self.assertEqual(best_value, 100)  # Total value is the value of the single item


if __name__ == "__main__":
    unittest.main()
