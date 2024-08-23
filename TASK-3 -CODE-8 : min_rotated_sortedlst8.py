"""8. Write a python program to find the minimum element in a rated and sorted list?
STEPS:
1: Initialize variables for the first and last index
2: Check if the list is not rotated (smallest element is at the start)
3: Use a loop to find the minimum element
4:  Check if the middle element is the smallest
5: The loop ends when left and right point to the minimum element"""

def find_min_in_rotated_list(arr):
    left = 0
    right = len(arr) - 1
    
    if arr[left] < arr[right]:
        return arr[left]
    
    
    while left < right:
        mid = (left + right) // 2
        
        
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    return arr[left]

arr = [4, 5, 6, 7, 0, 1, 2]


min_element = find_min_in_rotated_list(arr)
print("The minimum element is:", min_element)
