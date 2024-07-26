"""4. Write a python program to find the sum of the first and last digit of an integer?"""

number = input("Enter a number:")

int_list = list(number)

list_1 = []

for i in int_list:
    list_1.append(int(i))

length = len(list_1)

if length == 1:
    print("The sum of the digits in number is:",list_1[0])
if length > 1:
    first_last_sum = list_1[0] + list_1[-1]
    print ("The sum of the first & last digits of the given number is:",first_last_sum)

"""Take the input from user then we get it in a string type
convert it to list
again iterate over the string type list & convert each element to integer type
find the length of int type list if length ==0 print the same element as its sum
if length >1, add the first & last digits of the list & print as sum"""
