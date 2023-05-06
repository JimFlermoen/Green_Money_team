#!/usr/bin/env python3.7

# 1. Create the Script, Make It Executable with python3.7, and Accept User Input
# 2. Print "FizzBuzz" if the Value Is a Multiple of Three and Five
# 3. Print "Fizz" if the Value Is a Multiple of Three
# 4. Print "Buzz" if it's a Multiple of Five
# 5. if non of those are true, print value


value = int(input("Enter an integer value: "))

if value % 5 == 0 and value % 3 == 0:
    print("FizzBuzz")
elif value % 3 == 0:
    print("Fizz")
elif value % 5 == 0:
    print("Buzz")
else:
    print(value)