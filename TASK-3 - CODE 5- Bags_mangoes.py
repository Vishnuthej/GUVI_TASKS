"""code 5. 
You have been given a list of N integers whihc represents the number of Mangoes in a bag.
 Each bag has a variable number of mangoes. There are M students in a GUVI class,
your task is to distribute the mangoes in such a way that each student gets one bag.
The difference between the number of mangoes in a bag with maximum mangoes and bag with 
minimum mangoes given to the student is minimum?

STEPS:
1.Sort the Mangoes list
2. Find the Minimum Difference
3. Find the smallest difference between maximum and minimum of all the possible subsets
4. Find all the possible subsets which gives minimum difference then return the value.
 """

def min_mango_difference(mangoes, M):
    mangoes.sort()
    min_difference = float('inf')
    
    for i in range(len(mangoes) - M + 1):
        current_difference = mangoes[i + M - 1] - mangoes[i]
        if current_difference < min_difference:
            min_difference = current_difference

    return min_difference

mangoes = [10, 15, 8, 20, 12, 7]
M = 3

result = min_mango_difference(mangoes, M)

print("The minimum difference is:", result)



#-----------------------------------------------------------------------------------------
"""Possible subsets:
[7, 8, 10] → Difference: 10 - 7 = 3  this is the final --> minimum
[8, 10, 12] → Difference: 12 - 8 = 4
[10, 12, 15] → Difference: 15 - 10 = 5
[12, 15, 20] → Difference: 20 - 12 = 8"""
