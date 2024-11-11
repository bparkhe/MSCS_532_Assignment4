# MSCS_532_Assignment4

# Sorting Algorithm Implementation

## Overview

This repository provides Python implementations for three classic sorting algorithms: **Heapsort**, **Quicksort**, and **Merge Sort**. These algorithms are tested on different input sizes and distributions (random, sorted, and reverse-sorted arrays) to observe and compare their performance.

## Files

- `heap_sort`: Contains the `heapify_down` and `heap_sort` functions to sort an array using the Heapsort algorithm.
- `quick_sort`: Implements the Quicksort algorithm using recursive partitioning around a pivot.
- `merge_sort`: Implements the Merge Sort algorithm using recursive division and merging of array halves.
- `test_script`: A script to run each sorting algorithm on arrays of different sizes and distributions, recording and displaying the runtime of each.

## Implementation Details

### Heapsort
- **Description**: Builds a max-heap from the input array and extracts the maximum element repeatedly.
- **Helper Function**: `heapify_down` maintains the max-heap property after each extraction.
- **Time Complexity**: `O(n log n)` for all cases.
- **Space Complexity**: `O(1)` (in-place sorting).

### Quicksort
- **Description**: Selects a pivot and partitions the array into elements less than, equal to, and greater than the pivot, then recursively sorts the left and right partitions.
- **Time Complexity**: Average `O(n log n)`, Worst `O(n^2)`.
- **Space Complexity**: `O(log n)` due to recursion.

### Merge Sort
- **Description**: Divides the array into halves, recursively sorts each half, and merges them.
- **Time Complexity**: `O(n log n)` for all cases.
- **Space Complexity**: `O(n)` due to temporary arrays for merging.

## Running Tests

The script measures the execution time for each algorithm on arrays of varying sizes and distributions. To run the tests:
1. Install Python 3.x.
2. Run the script in a terminal or Python environment:
   ```sh
   python sorting_comparison.py
## Expected Output
   ```sh
   Testing with array size: 1000
   Heap Sort Time: 0.0053 seconds
   Quick Sort Time: 0.0037 seconds
   Merge Sort Time: 0.0042 seconds
   
   Testing with array size: 5000
   Heap Sort Time: 0.0254 seconds
   Quick Sort Time: 0.0201 seconds
   Merge Sort Time: 0.0228 seconds
   
   Testing with array size: 10000
   Heap Sort Time: 0.0556 seconds
   Quick Sort Time: 0.0459 seconds
   Merge Sort Time: 0.0498 seconds


# Priority Queue for Task Scheduling

This repository contains an implementation of a Priority Queue using a binary heap to manage and schedule tasks efficiently. The implementation supports both max-heap and min-heap configurations, allowing for either highest-priority-first or lowest-priority-first scheduling. The project includes a `Task` class to represent individual tasks, with attributes such as task ID, priority, arrival time, and deadline.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Class and Method Descriptions](#class-and-method-descriptions)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Overview

This implementation provides an efficient way to manage and retrieve tasks based on priority, using a binary heap data structure. The binary heap allows efficient insertion, extraction, and priority modification operations, making it ideal for task scheduling applications.

## Features

- Efficient insertion and extraction of tasks based on priority.
- Supports both max-heap (highest-priority-first) and min-heap (lowest-priority-first) configurations.
- Provides functionality to adjust the priority of tasks and maintain the heap property.
- Simple and efficient checks for heap status (e.g., empty or not).

## Getting Started

### Prerequisites

- Python 3.x

### Running the script

Run the script in a terminal or Python environment:

```bash
   python priority_queue_implementation.py
## Expected Output
```bash
Extracted task: Task(id=2, priority=20, arrival=09:30, deadline=13:00)
Is the queue empty? False
Heap: [Task(id=3, priority=25, arrival=10:00, deadline=11:30), Task(id=1, priority=10, arrival=09:00, deadline=12:00)]

