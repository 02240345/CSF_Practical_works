# step1

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Test the function
for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")

# step2

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test the function
for i in range(10):
    print(f"F({i}) = {fibonacci_iterative(i)}")

import time

# step3

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

# Test both functions and compare their execution times
n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n}) = {iterative_result}, Time: {iterative_time:.6f} seconds")

# step4

def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# Test the generator
for i, fib in enumerate(fibonacci_generator(10)):
    print(f"F({i}) = {fib}")

# step5

def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

# Test the memoized function
for i in range(10):
    print(f"F({i}) = {fibonacci_memoized(i)}")

# Compare performance with the original recursive function
n = 30
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")





# Exercises

# 1.Returning a list of Fibonacci numbers up to n, instead of just the nth number.

def fibonacci_list(n):
    if n <= 0:
        return [0]
    sequence = [0, 1]
    for _ in range(2, n + 1):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Test the function
print(f"Fibonacci sequence up to F(10): {fibonacci_list(10)}")




# 2.Finding the index of the first Fibonacci number that exceeds a given value.

def find_fibonacci_exceeding(value):
    a, b = 0, 1
    index = 1
    while b <= value:
        a, b = b, a + b
        index += 1
    return index

# Test the function
value = 50
print(f"The first Fibonacci number greater than {value} is at index {find_fibonacci_exceeding(value)}")




# 3.Determining if a given number is a Fibonacci number.

def is_fibonacci_number(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or num == 0

# Test the function
test_num = 28
print(f"{test_num} is a Fibonacci number: {is_fibonacci_number(test_num)}")




# 4.Calculateing the ratio between consecutive Fibonacci numbers and observe how it approaches the golden ratio.

def fibonacci_ratios(limit):
    a, b = 0, 1
    ratios = []
    for _ in range(2, limit + 1):
        ratio = b / a if a != 0 else 0
        ratios.append(ratio)
        a, b = b, a + b
    return ratios

# Test the function
limit = 10
ratios = fibonacci_ratios(limit)
print("Ratios between consecutive Fibonacci numbers:", ratios)


