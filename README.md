# Knapsack Problem Solver Using Estimation of Distribution Algorithms

This project implements an **Estimation of Distribution Algorithm (EDA)** to solve the **Knapsack Problem**. The goal is to maximize the total value of items in a knapsack without exceeding its weight capacity. This solution uses Python and encapsulates the algorithm in a reusable class structure.

---

## **Key Features**
- Solves the **0/1 Knapsack Problem** efficiently using EDA principles.
- Provides a clean and reusable Python class structure.
- Core functionalities include:
  - **Fitness Calculation**: Evaluates the total value of selected items.
  - **Elite Selection**: Focuses on the top-performing solutions.
  - **Distribution Estimation**: Learns the probabilities of selecting each item.
  - **Population Sampling**: Generates new solutions based on learned probabilities.
---

## Installation

### Prerequisites
- **Python 3.9+**
- Required packages:
  - `numpy`
  - `black`
  - `pytest`
---

## **Installation**
### **Setup Instructions**
1. Clone the repository:
```
git clone https://github.com/aaronGeb/knapsack.git
cd knapsack
```

2.	Install the dependencies
```
pip install -r requirements.txt
```
## Testing
This project includes unit tests using pytest. To run the tests:
```
python -m unittest test_knapsack.py
```

## Code Formatting
```
black .
```
### Contributing

Contributions are welcome! If you’d like to contribute:
1.	Fork the repository.
2.	Create a new branch for your feature or bug fix.
3.	Submit a pull request for review.

## License
This project is licensed under the MIT License. See the [LICENSE]() file for details.