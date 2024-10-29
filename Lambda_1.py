"""What is the expected output of the following python code given below?
"""
data = [10, 501, 22, 37, 100, 999, 87, 351]
result = filter (lambda x: x>4, data)
print(list(result))

"""Expected output: filter() can filter all the elements
from the data list whihc are greater than 4 and the final output will be
[10, 501, 22, 37, 100, 999, 87, 351] since every element is >4"""