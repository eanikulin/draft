import random


def fast_sort(array):
    if len(array) <= 1:
        return array
    else:
        queue_el = random.choice(array)
        small_el_array, max_el_array, equals_el_array = [], [], []
        for num in array:
            if num < queue_el:
                small_el_array.append(num)
            elif num > queue_el:
                max_el_array.append(num)
            else:
                equals_el_array.append(num)
        return fast_sort(small_el_array) + equals_el_array + fast_sort(max_el_array)

# Существует множество методов сортировки, например: пузырьковая, выборкой, вставками,
# слиянием и др. Но наиболее быстрой считается, как ни странно «быстрая» сортировка,
# эту сортировку я и выбрал. В среднем время выполнения составляет O(n log n).
# Но не всё так хорошо, если Pivot (опорный) элемент будет равен самому наименьшему/наибольшему элементу,
# то сортировка будет работать медленнее O(n²), в отличии от сортировок «слияния» или «кучей».
# Но так же можно отметить стандартную сортиворку, встроенную в Python, которая использует алгоритм timsort,
# по сложности данная сортировка практически равна "быстрой"