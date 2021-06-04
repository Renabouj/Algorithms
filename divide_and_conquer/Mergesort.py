import math

def merge(array, left, middle, right):
    left_arr = middle - left + 1
    right_arr = right - middle

    n_leftArr = [0] * (left_arr + 1)
    n_rightArr = [0] * (right_arr + 1)


    for k in range(0, left_arr):
        n_leftArr[k] = array[left + k]
    
    for k in range(0, right_arr):
        n_rightArr[k] = array[middle + 1 + k]
    
    n_leftArr[left_arr] = math.inf
    n_rightArr[right_arr] = math.inf

    r = 0
    g = 0

    for k in range(left, right + 1):
        if n_leftArr[r] <= n_rightArr[g]:
            array[k] = n_leftArr[r]
            r += 1
        else:
            array[k] = n_rightArr[g]
            g += 1

def mergeSort(array, left, right):
    if left < right:
        middle = (left + right) // 2
        mergeSort(array, left, middle)
        mergeSort(array, middle + 1, right)
        merge(array, left, middle, right)

lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
mergeSort(lista, 0, len(lista) - 1)
print(lista)

