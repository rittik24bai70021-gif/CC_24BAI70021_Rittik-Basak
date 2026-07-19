# Exp 1.1.2 - Product of Array Except Self

## Problem Statement
Given an integer array nums, return an array answer such that:

- answer[i] is equal to the product of all elements in nums except nums[i]
- The solution must work without using division

## Objective
This experiment demonstrates different ways to solve the problem efficiently while understanding the trade-off between simplicity and performance.


## 📊 Complexity Comparison
| File                         | Time Complexity |                Space Complexity                |
| ---------------------------- | :-------------: | :--------------------------------------------: |
| `brute_force.py`             |    **O(n²)**    |             **O(1)** (Extra Space)             |
| `optimized_prefix_suffix.py` |     **O(n)**    | **O(1)** (Extra Space, excluding output array) |
| `advanced_prefix_suffix.py`  |     **O(n)**    |                    **O(n)**                    |



## 📂 Project Structure

```
EXP-1.1.2-Product-of-Array-Except-Self/
│
├── brute_force.py
├── optimized_prefix_suffix.py
├── advanced_prefix_suffix.py
├── README.md
└── screenshots/

```

---


### 1. Brute Force
File: brute_force.py

- Computes the product of all elements except the current index by iterating through the array for each position.
- Simple and easy to understand.
- Time complexity: O(n^2)

### 2. Optimized Prefix and Suffix Method
File: optimized_prefix_suffix.py

- Uses one left-to-right pass and one right-to-left pass.
- Builds the result in O(n) time and O(n) extra space.
- This is the standard efficient approach.

### 3. Advanced Prefix and Suffix Method
File: advanced_prefix_suffix.py

- Uses separate prefix and suffix arrays before combining them into the final answer.
- Helps in understanding the step-by-step logic behind the optimized solution.
- Time complexity: O(n)

## Example
Input:
```python
[1, 2, 3, 4]
```

Output:
```python
[24, 12, 8, 6]
```

## How to Run
Run any Python file using:

```bash
python brute_force.py
python optimized_prefix_suffix.py
python advanced_prefix_suffix.py
```

When prompted, enter the array elements separated by spaces.

## Learning Outcome
By completing this experiment, you will learn:

- How to solve array problems without division
- The difference between brute force and optimized approaches
- How prefix and suffix products work in algorithm design

**Author:** Rittik Basak
