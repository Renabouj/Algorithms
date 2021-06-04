############################################################################################
# Reference: Introduction to Algorithms
# Book by Charles E. Leiserson, Clifford Stein, Ronald Rivest, and Thomas H. Cormen
############################################################################################



import math        #used to create the sentinels


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


def main():
    list = []

    flag = True
    while flag:
        prompt = str(input("Type 'no' to start running the algorithm or wait to insert a number: "))
        if prompt == 'no':
            flag  = False
        else:
            number = int(input("Please insert a number: "))
            list.append(number)


if __name__ == '__main__':
    main()
