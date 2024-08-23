""" 7. Write a python progrsm to find the first non repeating elements in a
 given list of integers?"""

"""STEPS:
1. Count the Frequencies how often each number appears in the list using a dictionary 
called frequency.
2. Identifying the First Non-Repeating Element after counting the frequencies
3. If a non-repeating element is found, it is printed; otherwise, print a message indicating that all 
elements are repeating.
"""

def find_first_non_repeating(lst):
    
    frequency = {}
    
    
    for num in lst:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    
    for num in lst:
        if frequency[num] == 1:
            return num
    
    return None  

lst = [4, 5, 1, 2, 0, 4, 1, 2]
result = find_first_non_repeating(lst)
if result:
    print(f"The first non-repeating element is: {result}")
else:
    print("There is no non-repeating element in the list.")