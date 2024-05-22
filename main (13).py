import time
import random

def shell_sort(arr):
    """
    Сортировка Шелла
    """
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def heap_sort(arr):
    """
    Пирамидальная сортировка
    """
    n = len(arr)

    # Строим пирамиду
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Сортируем пирамиду
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def heapify(arr, n, i):
    """
    Восстанавливаем пирамиду
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def quick_sort(arr):
    """
    Сортировка Хоара
    """
    n = len(arr)

    if n <= 1:
        return

    pivot = arr[n // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    quick_sort(left)
    quick_sort(right)

    arr[:len(left)] = left
    arr[len(left):len(left) + len(middle)] = middle
    arr[len(left) + len(middle):] = right

def is_sorted(arr):
    """
    Проверка на упорядоченность массива
    """
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def measure_sort_time(sort_func, arr):
    """
    Измерение времени сортировки
    """
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

# Генерация большого массива
large_array = [random.randint(1, 1000000) for _ in range(100000)]
arr = [10, 7, 8, 9, 1, 5]

# Сортировка Шелла
shell_sort(arr)
print("После сортировки Шелла:", arr)
arr = large_array.copy()
time_taken = measure_sort_time(shell_sort, arr)
print("Время сортировки Шелла:", time_taken)
print("Массив отсортирован:", is_sorted(arr))

# Пирамидальная сортировка 
arr = [10, 7, 8, 9, 1, 5]
heap_sort(arr)
print("После пирамидальной сортировки:", arr)
arr = large_array.copy()
time_taken = measure_sort_time(heap_sort, arr)
print("Время пирамидальной сортировки:", time_taken)
print("Массив отсортирован:", is_sorted(arr))

# Сортировка Хоара
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr)
print("После сортировки Хоара:", arr)
arr = large_array.copy()
time_taken = measure_sort_time(quick_sort, arr)
print("Время сортировки Хоара:", time_taken)
print("Массив отсортирован:", is_sorted(arr))
