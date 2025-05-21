# Module 4: Functions & Modules in Python

# Task 1: Calculate Factorial Using a Function
num = int(input("enter a number = "))
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
factorial = fact(num)
print(f"factorial of {num} is  = {factorial}")

# Task 2: Using the Math Module for Calculations

import math
num = float(input("enter a number : "))
sqrt_val = math.sqrt(num)
log_val = math.log(num)
sine_val = math.sin(num)

print(f"square root : {round(sqrt_val, 1)}")
print(f"logarithm : {log_val}")
print(f"Sine : {sine_val}")

