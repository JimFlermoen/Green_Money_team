#!/usr/bin/env python3.7

#Fizzbuzz

# 1. prompt the user for a value, convert it to an int, and store it off in a variable.
# 2. Print "FizzBuzz" if the Value Is a Multiple of Three and Five.
# 3. Print "Fizz" if the Value Is a Multiple of Three. 
# 4. Print "Buzz" if It's a Multiple of Five.
# 5. Otherwise print the number
upper_number = int(input("How many values should we process: "))

for number in range(1, upper_number + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)