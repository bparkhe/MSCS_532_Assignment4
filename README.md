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
  
