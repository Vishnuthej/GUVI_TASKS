"""write a python code using lambda function to check every element of a
 list is an integer or string [10, 501, 22, 37, 100, 999, 87, 351]
 STEPS: 
 1. Initialize the data
 2. write the lambda function inside the map()
 3.convert the result into a list then print"""

data = [10, 501, 22, 37, 100, 999, 87, 351]
result = map(lambda x: "Integer" if isinstance(x, int) else "String", data)
result1 = list(result)
print(f"Data:{data}\n",
    f"Type_of_data:{result1}")
