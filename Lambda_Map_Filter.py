# 1. Example without lambda
def fahrenheit(T):
    return ((float(9) / 5) * T + 32)


def celsius(T):
    return (float(5) / 9) * (T - 32)


temperatures = (36.5, 37, 37.5, 38, 39)

# Python 2 - returns list
F = map(fahrenheit, temperatures)
C = map(celsius, F)
print(F)
print(C)

# Python 3
# temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures))
# temperatures_in_Celsius = list(map(celsius, temperatures_in_Fahrenheit))
# print(temperatures_in_Fahrenheit)
# [97.7, 98.60000000000001, 99.5, 100.4, 102.2]
# print(temperatures_in_Celsius)
# [36.5, 37.00000000000001, 37.5, 38.00000000000001, 39.0]


# 2. Example with lambda
temperatures = [36.5, 37, 37.5, 38, 39]
# C = [39.2, 36.5, 37.3, 38, 37.8]
F = list(map(lambda x: (float(9) / 5) * x + 32, temperatures))
print(F)
# [97.7, 98.60000000000001, 99.5, 100.4, 102.2]
C = list(map(lambda x: (float(5) / 9) * (x - 32), F))
print(C)
# [36.5, 37.00000000000001, 37.5, 38.00000000000001, 39.0]


# 3. Example with multiple lists
a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]
print(list(map(lambda x, y: x + y, a, b)))
# [18, 14, 14, 14]
print(list(map(lambda x, y, z: x + y + z, a, b, c)))
# [17, 10, 19, 23]
print(list(map(lambda x, y, z: 2.5 * x + 2 * y - z, a, b, c)))
# [37.5, 33.0, 24.5, 21.0]


# 4. Example with filter
# Following example filters out first the odd and then the even elements of the sequence of the first 11 Fibonacci numbers
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print(odd_numbers)
# [1, 1, 3, 5, 13, 21, 55]
even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)
# [0, 2, 8, 34]

# 5. Three simple examples of reduce function of Python. It is in functools module in Python 3.
from functools import reduce

# Determining the maximum of a list of numerical values
f = lambda a, b: a if (a > b) else b
print(reduce(f, [47, 11, 42, 102, 13]))
# 102

# Calculating the sum of the numbers from 1 to 100:
print(reduce(lambda x, y: x + y, range(1, 101)))
# 5050

# Calculating the factorial from 1 to a number
print(reduce(lambda x, y: x * y, range(1, 49)))
# 12413915592536072670862289047373375038521486354677760000000000


# 5. Lambda and map() example
orders = [["34587", "Learning Python, Mark Lutz", 4, 40.95],
          ["98762", "Programming Python, Mark Lutz", 5, 56.80],
          ["77226", "Head First Python, Paul Barry", 3, 32.95]]

min_order = 100
invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10),
                          map(lambda x: (x[0], x[2] * x[3]), orders)))
print(invoice_totals)
