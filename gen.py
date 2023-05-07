# (REPL) enter: python3.7 -i gen.py

# >>> generator = gen_range(10)
# >>> for num in gen_range(10, step=2):
#....    print(num)
# runs until stop interator
def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step
 
 #
 
 # Converting generator to list
    # >>> generator = gen_range(10)
    # >>> list(Gemerator)
 
 #-------------------------------------------------------------------------
 # (REPL) enter: python3.7 -i gen.py
 
 # >>> fib = gen_fib()
 # >>> next(fib)
 
def gen_fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a
    
# >>> list(fib) would run for ever and never return a number.

# how to get giant list and get the 50th number in the sequence.
# >>> fib = gen_fib()
# >>> [next(fib) for _ in range (50)][-1]
# output: 12586269025