# if name is greater than or equal too 6: print
    # if correct, prints this and doesn't check rest

# elif your name is greater than or equal to 4: print
    # will print if only 4 characters, because will print top line if more   

#elif your name is equal to 5: print
    # This is a dead branch

# else: print 
    # will print if name is 3 or less characters
    
name = input("What is your name? ")

if len(name) >= 6:
    print("Your name is long")
elif len(name) >= 4:
    print("Your name is 4 or more characters")
elif len(name) == 5:
    print("Your name is 5 characters")

else:
    print("Your name is short")

    