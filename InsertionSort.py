#Time O(N^2) time | O(1) Space
def InsertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1, array)
            j-=1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

array = [1,3,10,9,8,23,0,1,2]
print("Array Before Sorting" , array);
InsertionSort(array)
print("Array After Sorting " , array)
