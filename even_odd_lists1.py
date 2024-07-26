"""1. You have been given a python List [10,501,22,37,100,999,87,351] your task is to create two list one whihc have all the 
EVEN numbers and another list which will have all the ODD numbers in it?

Steps:
1) Create 2 empty lists one for even & one for odd numbers.
2)Initialize an integer value with zero for index in LIST
3) Pick each number from list and modulo divide it with 2 based on the remainder sort the numbers """


list1= [10,501,22,37,100,999,87,351]
list = sorted(list1)

even_list=[]
odd_list=[]

i=0
for i in list:
    if i%2 ==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("The even numbers from the given list:",even_list)

print("The odd numbers from the given list:",odd_list)


"""Given list of numbers
#to get all the numbers in ascending order 
#Empty lists for even & odd numbers
integer value for List index
Iteration over the given list 
Printing the both the lists"""