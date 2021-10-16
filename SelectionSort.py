#Time O(N^2) time | O(1) Space 

def SelectionSort(array):
    current = 0
    while current < len(array) - 1:
        smallest = current
        for i in range (current + 1, len(array)):
            if array[smallest] > array[i]:
                smallest = i
        swap(current, smallest, array)
        current += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

array = [1,3,10,9,8,23,0,1,2]
print("Array Before Sorting" , array);
SelectionSort(array)
print("Array After Sorting " , array)
