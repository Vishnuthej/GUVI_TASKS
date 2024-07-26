"""1. You have been given a python List [10,501,22,37,100,999,87,351] your task is to create a list one whihc have all the 
prime numbers in it?

Steps:
1) Create an empty list to store all the prime numbers.
2)Initialize an integer value with zero for index in LIST
3) Pick each number from list and modulo divide it with 1& same number based on the remainder sort the numbers """


list_1=[10, 501, 22, 37, 100, 999, 87, 351]


sorted_list = sorted(list_1)
prime_list=[]

for num in sorted_list:
    if num > 1 :
        num_prime = True 
        for j in range(2,num//2):
            if num % j ==0:
                num_prime = False
                break
        if num_prime:
            prime_list.append(num)
print("The list of prime numbers from the given list:", prime_list)
            
"""#Given list of numbers
#to get all the numbers in ascending order
Empty lists for prime numbers 
#Iteration over the given list 
use the floor division by 2 of the number so that we can reduce the no.of iterations
Use a boolean flag for easy to make decision of the state of the number."""