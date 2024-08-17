"""6. You have been given 3 lists. Your task is to find the duplicates in the 3 lists.
 Write a python program for the same. You can use your own python lists?"""

"""1) take 3 random lists with a common element in all the 3 lists
2) convert each list into a set to remove duplicates in each list 
3) use '&' AND operator to find out the intersection of all lists to get the common elements in all 
4) finally convert all the resulted elements into a list for the output"""


list_1 = [1, 3, 55, 321, 1, 567]
list_2 = [543, 55, 5, 67, 1, 7890, 456, 7656644, 456]
list_3 = [3, 6, 9, 90, 55, 55, 543, 1]

duplicates1 = list(set(list_1) & set(list_2) & set(list_3))

print(duplicates1)
print(type(duplicates1))


