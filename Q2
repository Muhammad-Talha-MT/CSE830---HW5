import random
import timeit
import matplotlib.pyplot as plt

# Insertion sort implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge sort implementation
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

# Hybrid sort implementation
def hybrid_sort(arr, k):
    if len(arr) > k:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        hybrid_sort(left, k)
        hybrid_sort(right, k)
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
    else:
        insertion_sort(arr)

# Generate random input array of size n
def generate_input(n):
    return [random.randint(0, 100000) for i in range(n)]

# Measure time taken for hybrid sort with given k
def measure_time(n, k):
    arr = generate_input(n)
    hybrid_sort(arr, k)

    # Time hybrid sort
    hybrid_time = timeit.timeit(lambda: hybrid_sort(arr, k), number=100)

    # Time insertion sort
    arr = generate_input(n)
    insertion_time = timeit.timeit(lambda: insertion_sort(arr), number=100)

    # Time merge sort
    arr = generate_input(n)
    merge_time = timeit.timeit(lambda: merge_sort(arr), number=100)

    return hybrid_time, insertion_time, merge_time

# Test hybrid sort with various k values for given n
def test_k_values(n, k_values):
    hybrid_times = []
    insertion_times = []
    merge_times = []

    for k in k_values:
        hybrid_time, insertion_time, merge_time = measure_time(n, k)
        hybrid_times.append(hybrid_time)
        insertion_times.append(insertion_time)
        merge_times.append(merge_time)

    # Plot the results
    plt.plot(k_values, hybrid_times, label="Hybrid Sort")
    plt.plot(k_values, insertion_times, label="Insertion Sort")
    plt.plot(k_values, merge_times, label="Merge Sort")
    plt.legend()
    plt.show()

n = 10000
k_values = [10, 50, 100, 500, 1000, 5000]
test_k_values(n, k_values)
