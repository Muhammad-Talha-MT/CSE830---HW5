import random
import time
import matplotlib.pyplot as plt
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    


# Test each algorithm on a range of input sizes
sizes = [i for i in range(10, 1000, 10)]
print(sizes)
merge_sort_times = []
insertion_sort_times = []

for n in sizes:
    
    start = time.time()
    for i in range(1000):
        arr = [random.randint(0, 100) for _ in range(n)]
        merge_sort(arr)
    end = time.time()
    merge_sort_times.append((end - start)/1000)

    start = time.time()
    for i in range(1000):
        arr = [random.randint(0, 100) for _ in range(n)]
        insertion_sort(arr)
    end = time.time()
    insertion_sort_times.append((end - start)/1000)
# Plot the results
plt.plot(sizes, merge_sort_times, label='Merge sort')
plt.plot(sizes, insertion_sort_times, label='Insertion sort')
plt.xlabel('Input size')
plt.ylabel('Time (seconds)')
plt.title('Comparison of Merge sort and Insertion sort')
plt.legend()
plt.show()
