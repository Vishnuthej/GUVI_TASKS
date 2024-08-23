"""
CODE 9: You have been given a python list [10,20,30,9] and a value of 59.
 Write a python program to find the triplet in the list
whose sum is equal to the given value?

STEPS:
1. Iterates through each possible triplet combination in the list.
2. Check if the sum of any triplet equals the target value (59 in this case).
3. If such a triplet is found, return and print the triplet. 
4. If no such triplet exists, return None and print that no triplet was found."""

numbers = [10, 20, 30, 9]
target_sum = 59


def find_triplet(nums, target):
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                
                if nums[i] + nums[j] + nums[k] == target:
                    return nums[i], nums[j], nums[k]
    return None


triplet = find_triplet(numbers, target_sum)
if triplet:
    print("Triplet found:", triplet)
else:
    print("No triplet found with the given sum.")







