import os 
import random

print("This is an automated program to determine the business costs")

print("Input the fixed costs in dollars")

num1 = input()

num1 = int(num1)

print("Input the total variable costs in dollars")

num2 = input()

num2 = int(num2)

print("The amount of units produced")

num3 = input()

num3 = int(num3)

print(f'The total cost of production is ${num1 + num2}')

print(f'The variable cost per unit is ${num2/num3}')

print(f'The unitary cost is ${(num1+num2)/num3}')

print(f'The recommended selling price accounting for the total costs and profit of 40% is ${1.4*((num1+num2)/num3)}')

