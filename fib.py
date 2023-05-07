# Recursion Fibonnaci function that tells you which number is in where in the sequence.
  # Example: 15th number is 610
# Fib Sequence: 1, 1, 2, 3, 5, 8, 13, 

# 1+1=2, 1+2=3, 2+3=5, 3+5=8, 5+8=13 ... 

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
        
    return fib(n - 2) + fib(n - 1)
    
item_to_calculate = int(input("What Fibonnaci item would you like to calculate? "))
print(fib(item_to_calculate))