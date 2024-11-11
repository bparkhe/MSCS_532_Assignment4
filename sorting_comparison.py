import random
import time

def heapify_down(arr, heap_size, root_idx):
    max_idx = root_idx  
    left_idx = 2 * root_idx + 1  
    right_idx = 2 * root_idx + 2  

    if left_idx < heap_size and arr[left_idx] > arr[max_idx]:
        max_idx = left_idx

    if right_idx < heap_size and arr[right_idx] > arr[max_idx]:
        max_idx = right_idx

    if max_idx != root_idx:
        arr[root_idx], arr[max_idx] = arr[max_idx], arr[root_idx]  
        heapify_down(arr, heap_size, max_idx)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify_down(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify_down(arr, i, 0)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Testing with various input sizes and distributions
for arr_size in [1000, 5000, 10000]:
    test_arr = random.sample(range(arr_size), arr_size)
    
    start = time.time()
    heap_sort(test_arr.copy())
    print("Heap Sort Time:", time.time() - start)
    
    start = time.time()
    quick_sort(test_arr.copy())
    print("Quick Sort Time:", time.time() - start)
    
    start = time.time()
    merge_sort(test_arr.copy())
    print("Merge Sort Time:", time.time() - start)
