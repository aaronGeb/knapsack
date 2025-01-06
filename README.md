# Knapsack Problem Solver Using Genetic Algorithms

This project implements a **Genetic Algorithm (GA)** to solve the **Knapsack Problem**. The goal is to maximize the total value of items in a knapsack without exceeding its weight capacity. This solution uses Python and encapsulates the algorithm in a reusable class structure.

---

## **Features**
- Solves the 0/1 Knapsack Problem.
- Encapsulates functionality in a Python class for modularity and reusability.
- Includes:
  - **Fitness Evaluation**
  - **Selection (Roulette Wheel)**
  - **Crossover (Single-point)**
  - **Mutation**
  - **Iteration until Convergence**

---

## **How It Works**
1. **Initialization**:
   - Randomly generate a population of solutions (binary vectors).

2. **Fitness Function**:
   - Calculates the total value of items in a solution. Penalizes solutions exceeding the weight capacity.

3. **Selection**:
   - Uses **roulette wheel selection** to pick parents based on their fitness.

4. **Crossover**:
   - Combines two parents to create new offspring using a single crossover point.

5. **Mutation**:
   - Flips a random bit in the solution with a given probability to introduce diversity.

6. **Iteration**:
   - Repeats selection, crossover, mutation, and replacement for a specified number of generations.

7. **Output**:
   - Returns the best solution and its value after all generations.

---

## **Requirements**
- Python 3.7+
- No additional libraries required (uses Python's standard `random` module).

---

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/aaronGeb/knapsack.git
   cd knapsack