# Step 1: Implement Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(test_arr.copy())
print("Bubble Sort Result:", sorted_arr)


# Step 2: Implement Merge Sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(test_arr)
print("Merge Sort Result:", sorted_arr)


# Step 3: Implement Quick Sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(test_arr)
print("Quick Sort Result:", sorted_arr)


# Step 4: Compare Performance

import time
import random

def compare_sorting_algorithms(arr):
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort)
    ]
    
    for name, func in algorithms:
        arr_copy = arr.copy()
        start_time = time.time()
        func(arr_copy)
        end_time = time.time()
        print(f"{name} took {end_time - start_time:.6f} seconds")

# Generate a large random array
large_arr = [random.randint(1, 1000) for _ in range(1000)]

# Compare the algorithms
compare_sorting_algorithms(large_arr)




# Exercises

# 1.Implementing an In-Place Version of Quick Sort.

def in_place_quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        in_place_quick_sort(arr, low, pivot_index - 1)
        in_place_quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Using the last element as pivot
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Test the in-place Quick Sort function
test_arr = [64, 34, 25, 12, 22, 11, 90]
in_place_quick_sort(test_arr, 0, len(test_arr) - 1)
print("In-Place Quick Sort Result:", test_arr)


# 2.Modifying Bubble Sort to Stop Early if the List Becomes Sorted.

def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # No swaps means the array is sorted
            break
    return arr

# Test the optimized Bubble Sort function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = optimized_bubble_sort(test_arr.copy())
print("Optimized Bubble Sort Result:", sorted_arr)


# 3.Implementing a Hybrid Sorting Algorithm.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def hybrid_merge_sort(arr):
    if len(arr) <= 10:  # Threshold for using Insertion Sort
        insertion_sort(arr)
        return arr
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = hybrid_merge_sort(arr[:mid])
    right = hybrid_merge_sort(arr[mid:])
    
    return merge(left, right)  # Reuse the existing merge function

# Test the hybrid Merge Sort function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = hybrid_merge_sort(test_arr.copy())
print("Hybrid Merge Sort Result:", sorted_arr)


# 4.Creating a Visualization of Sorting Algorithms.

import matplotlib.pyplot as plt
import numpy as np
import time

def bubble_sort(arr, draw, pause):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            
            # Draw the current state of the array
            draw(arr)
            time.sleep(pause)
        if not swapped:
            break

def draw(arr):
    plt.clf()  # Clear the current figure
    plt.bar(range(len(arr)), arr, color='blue')
    plt.ylim(0, max(arr) + 1)  # Set y-axis limit
    plt.title("Bubble Sort Visualization")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.pause(0.1)  # Pause to allow the plot to update

def main():
    # Example array to sort
    arr = np.random.randint(1, 100, size=20)  # Generate a random array
    print("Original array:", arr)

    plt.ion()  # Turn on interactive mode
    draw(arr)  # Initial drawing
    bubble_sort(arr, draw, pause=0.1)  # Sort the array with visualization
    plt.ioff()  # Turn off interactive mode
    plt.show()  # Keep the final plot displayed

if __name__ == "__main__":
    main()