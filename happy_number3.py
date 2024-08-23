"""Code 3. Given a Python List [10,501,22,37,100,999,87,351]
Find out how many numbers are there in the given Python List, which are Happy Numbers
"""
"""Steps:
1)The function is_happy_number() is to check if the number is a happy number using recursive loop
2) the list checked_lst[] keeps track of the numbers already processed to avoid cycles.
3) The function calculates the sum of the squares of the digits of n and 
recursively checks if the new number is a Happy Number.
4) Before the function, check the n is 1 then return 'True' or if the num is present in checked_list 
then 'FALSE'
5)Iterate over the given list & find out the list of happy_numbers[]"""

def is_happy_number(n, checked_lst=None):
    if checked_lst is None:
        checked_lst = []

    if n == 1:
        return True
    if n in checked_lst:
        return False

    checked_lst.append(n)
    next_num = sum(int(digit) ** 2 for digit in str(n))
    return is_happy_number(next_num, checked_lst)

numbers = [10, 501, 22, 37, 100, 999, 87, 351]
happy_numbers = []

for num in numbers:
    if is_happy_number(num):
        happy_numbers.append(num)

print("Happy Numbers in the list are:", happy_numbers)


