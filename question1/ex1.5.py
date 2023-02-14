# Imports
import timeit
from matplotlib import pyplot as plt

# Given Recursive Fibonacci Function
def func1(n):
    if n == 0 or n == 1:
        return n
    else:
        return func1(n-1) + func1(n-2)

# Memoization Fibonacci Function
def func2(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = func2(n-1, memo) + func2(n-2, memo)
    return memo[n]

recursive_times = []
memoization_times = []

for i in range(36):
    recursive_time = timeit.timeit(lambda : func1(i), number=100)
    recursive_times.append(recursive_time)
    dynamic_time = timeit.timeit(lambda : func2(i), number=100)
    memoization_times.append(dynamic_time)

plt.plot(range(36), recursive_times, label='Recursive', color='purple')
plt.plot(range(36), memoization_times, label='Memoized', color='limegreen')
plt.xlabel('Input (n)')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()