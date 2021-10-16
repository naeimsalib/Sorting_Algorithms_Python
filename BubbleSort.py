#Time O(N^2) time | O(1) Space

import array as arr

def BubbleSort(array):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                isSorted = False
        counter += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

array = [1,3,10,9,8,23,0,1,2]
print("Array Before Sorting" , array);
BubbleSort(array)
print("Array After Sorting " , array)
