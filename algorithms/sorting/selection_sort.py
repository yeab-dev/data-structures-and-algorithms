from typing import List
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr: List):
    sortedList = []
    while arr:
        smallest_index = findSmallest(arr)
        sortedList.append(arr.pop(smallest_index))
    return sortedList