"""3)Using the python lambda function create a fibonacci series from 1 to 50 elements?"""
# Limit: Generate Fibonacci numbers from 1 to 50
def fibonacci(count):
    fib_list = [1, 1]
 
    any(map(lambda _: fib_list.append(sum(fib_list[-2:])),range(2, count)))
 
    return fib_list[:count]
 
print(fibonacci(50))




