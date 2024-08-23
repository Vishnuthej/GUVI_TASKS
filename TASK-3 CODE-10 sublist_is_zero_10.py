"""CODE 10: Given a list [4,2,-3,1,6] write a python program to find 
if there is a sub-list with sum equal to zero

STEPS:
1.Use a nested loop to check every possible sub-list (a contiguous part of the list).
2. For each starting point in the list, calculate the sum of elements in all possible sub-lists
that start from that point.
3. If the sum of any sub-list is zero, the function returns True.
4. If no such sub-list is found, the function returns False."""


numbers = [4, 2, -3, 1, 6]

def zero_sum_sublist(nums):
    
    for i in range(len(nums)):
        current_sum = 0
        
        for j in range(i, len(nums)):
            current_sum += nums[j]
            
            if current_sum == 0:
                return True
    
    return False

if zero_sum_sublist(numbers):
    print("There is a sub-list with sum equal to zero.")
else:
    print("There is no sub-list with sum equal to zero.")
