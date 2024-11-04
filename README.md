# LAB2

# Text Analysis Tool

This Python script analyzes text files to provide insights such as the number of lines, words, the most common word, average word length, and more.

## Features

- Read a text file and return its content.
- Count lines in the text.
- Count total words in the text.
- Identify the most common word and its frequency.
- Calculate the average word length.
- Count unique words in the text.
- Find the longest word in the text.
- Count occurrences of a specific word (case-insensitive).
- Calculate the percentage of words longer than the average word length.

## Functions

- read_file(filename): Reads the content of a file.
- count_lines(content): Counts the number of lines in the content.
- count_words(content): Counts the total number of words.
- most_common_word(content): Finds the most common word and its count.
- average_word_length(content): Calculates the average length of words.
- analyze_text(filename): Runs the complete analysis on the specified file.
- count_unique_words(content): Counts the number of unique words.
- find_longest_word(content): Finds the longest word in the text.
- count_word_occurrences(content, target_word): Counts occurrences of a specified word.
- percentage_longer_than_average(content): Calculates the percentage of words longer than the average length.


# LAB3

# Fibonacci Number Analysis Tool

This Python script provides various functions to work with Fibonacci numbers, including generating sequences, finding specific Fibonacci numbers, and calculating ratios that approach the golden ratio.

## Features

- Generate Fibonacci Sequence: Returns a list of Fibonacci numbers up to a specified index.
- Find Index of Exceeding Fibonacci Number: Determines the index of the first Fibonacci number that exceeds a given value.
- Check if a Number is Fibonacci: Checks if a specified number is a Fibonacci number.
- Calculate Ratios: Computes the ratios between consecutive Fibonacci numbers to observe their convergence to the golden ratio.

## Functions

- fibonacci_list(n): Returns a list of Fibonacci numbers up to the nth index.
- find_fibonacci_exceeding(value): Finds the index of the first Fibonacci number greater than the specified value.
- is_fibonacci_number(num): Determines if the provided number is a Fibonacci number.
- fibonacci_ratios(limit): Calculates the ratios between consecutive Fibonacci numbers up to the specified limit.


# LAB4

This code contains implementations of various search algorithms in Python, including Linear Search, Binary Search, Jump Search, and their performance analysis. Each algorithm is designed to showcase different methods of searching through lists and includes features to count the number of comparisons made during the search process.

## Features

- Linear Search: Searches for a target value in an unsorted list, returning all indices where the target appears.
- Binary Search: Efficiently finds a target value in a sorted list and provides the insertion point for the target if not found.
- Comparison Counting: Each search algorithm counts the number of comparisons made during its execution.
- Jump Search: Combines linear search with a block-based approach to optimize search performance in sorted lists.
- Performance Comparison: A tool to compare the efficiency of different search algorithms based on the number of
comparisons.

## Functions

- linear_search_all_indices(arr, target): Returns a list of indices where the target is found, or -1 if not found.
- binary_search_insertion_point(arr, target): Finds the insertion point for the target in a sorted list.
- linear_search_with_count(arr, target): Performs linear search and counts the number of comparisons.
- binary_search_with_count(arr, target): Performs binary search and counts the number of comparisons.
- jump_search(arr, target): Performs a jump search in a sorted list.
- compare_search_algorithms(arr, target): Compares the performance of linear and binary search on a given array for
a target value.


# LAB5

This code includes implementations of various data structures and algorithms using stacks and queues. It covers the
evaluation of postfix expressions, queue implementation using stacks, a basic task scheduler, and the conversion of
infix expressions to postfix notation.

## Features

- Postfix Expression Evaluation: Evaluates postfix expressions using a stack to compute the result.
- Queue Implementation Using Stacks: Implements a queue structure utilizing two stacks for enqueueing and dequeueing elements.
- Task Scheduler: A simple task scheduler that processes tasks in the order they were added using a queue.
- Infix to Postfix Conversion: Converts infix expressions to postfix notation using a stack to manage operator precedence.

## Functions

- evaluate_postfix(expression): Evaluates a given postfix expression and returns the result.
- QueueUsingStacks: A class that implements a queue using two stacks.
- TaskScheduler:  A class that manages and processes tasks in a first-in-first-out (FIFO) order.
- infix_to_postfix(expression): Converts an infix expression to postfix notation.


# LAB6

This code implements a singly linked list with various operations such as finding the middle element, detecting
cycles, removing duplicates, and merging two sorted linked lists. The linked list is a fundamental data structure
that allows for efficient insertions and deletions.

## Features

- Find Middle Element: Efficiently locates the middle element of the linked list using the slow and fast pointer technique.
- Cycle Detection: Detects whether the linked list contains a cycle, helping to identify infinite loops.
- Remove Duplicates: Removes duplicate elements from the linked list, ensuring all elements are unique.
- Merge Two Sorted Linked Lists: Combines two sorted linked lists into a single sorted linked list.
- Display Elements: Provides a method to display all elements in the linked list.

## Functions

- find_middle(): Finds the middle element of the linked list.
- has_cycle(): Detects if the linked list has a cycle using the Floyd’s Cycle Detection 
- remove_duplicates(): Removes duplicate values from the linked list.
- merge_sorted(other_list): Merges two sorted linked lists into a new sorted linked list.
- append(data): Appends a new node with the specified data to the end of the linked list.
- display(): Displays the elements of the linked list in a readable format.


# LAB7

This code provides an implementation of a Binary Search Tree (BST), enabling efficient data storage and retrieval
The BST is a type of binary tree that maintains a specific ordering of elements, allowing for fast searches,
insertions, and deletions.

## Features

- Find Maximum Value: Quickly retrieves the maximum value stored in the BST.
- Count Nodes: Counts the total number of nodes in the BST.
- Level-order Traversal: Performs a breadth-first traversal of the tree, returning node values in level order.
- Calculate Height: Computes the height of the BST, indicating the longest path from the root to a leaf.
- Validate BST: Checks if the tree adheres to the properties of a valid binary search tree.
- Traversal Methods: Supports in-order, pre-order, and post-order traversals.

## Functions

- max_value(): Finds the maximum value in the BST.
- count_nodes(): Counts the total number of nodes in the BST.
- level_order_traversal(): Performs a level-order traversal of the BST.
- height(): Calculates the height of the BST.
- is_valid_bst(): Validates whether the tree is a valid binary search tree.

# LAB8

This code implements various sorting algorithms, demonstrating different sorting techniques, including an in-place
version of Quick Sort, an optimized Bubble Sort, a hybrid sorting algorithm, and a visualization of the Bubble Sort
process using Matplotlib.

## Features

- In-Place Quick Sort: Efficiently sorts an array in place using the Quick Sort algorithm.
- Optimized Bubble Sort: Modifies the traditional Bubble Sort to stop early if the list becomes sorted before completing all passes.
- Hybrid Sorting Algorithm: Combines Merge Sort and Insertion Sort, using Insertion Sort for smaller subarrays to optimize performance.
- Sorting Visualization: Uses Matplotlib to visually represent the sorting process of the Bubble Sort algorithm.

## Functions

- in_place_quick_sort(arr, low, high): Sorts an array in place using the Quick Sort algorithm.
- partition(arr, low, high): Partitions the array into two halves based on the pivot.
- optimized_bubble_sort(arr): Sorts an array using an optimized version of the Bubble Sort algorithm that 
- insertion_sort(arr): Sorts an array using the Insertion Sort algorithm.
- hybrid_merge_sort(arr): Implements a hybrid sorting algorithm using Merge Sort for larger arrays 
- bubble_sort(arr, draw, pause): Performs the Bubble Sort algorithm while visualizing the process.
- draw(arr): Draws the current state of the array using Matplotlib.
- main():  The main function that generates a random array and starts the sorting visualization.

# LAB9

This code implements various graph algorithms, focusing on fundamental operations like finding the shortest path, detecting cycles, applying Dijkstra's algorithm for shortest paths, and checking if a graph is bipartite. These algorithms are crucial for solving numerous problems in computer science and real-world applications.

## Features

- Shortest Path (BFS): Finds the shortest path between two vertices using Breadth-First Search (BFS).
- Cycle Detection: Detects cycles in a graph using Depth-First Search (DFS).
- Dijkstra's Algorithm: Computes the shortest paths from a starting vertex to all other vertices in a weighted graph.
- Bipartite Check: Checks if a graph can be colored with two colors such that no two adjacent vertices share the
same color.

## Functions

- shortest_path(self, start_vertex, end_vertex): Finds the shortest path between two vertices using BFS.
- has_cycle(self): Detects cycles in the graph using DFS.
- dijkstra(self, start_vertex): Finds the shortest paths from the start_vertex to all other vertices using 
- is_bipartite(self): Checks if the graph is bipartite.