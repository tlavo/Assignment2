import sys
import matplotlib.pyplot as plt
from time import perf_counter
import json
sys.setrecursionlimit(20000)

# opening the file
with open('ex2.json', 'r') as f:
    data = json.load(f)


# The Quick Sort Algorithm Given
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


# code for accessing records and plotting
time = []
recordNum = []
for record in data:
    time_start = perf_counter()
    # len(record) - 1 was changed to 950 because the whole legth of the array would not run
    func1(record, 0, 950)
    time_end = perf_counter()
    time_each = time_end - time_start
    time.append(time_each)
    recordNum.append(data.index(record) + 1)

plt.plot(time)
plt.title("Time for Quick Sort Algorithm")
plt.xlabel("Records")
plt.ylabel("Time (s)")
plt.xticks(recordNum)
plt.show()