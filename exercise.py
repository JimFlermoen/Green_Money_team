# Create test String
teststring = "Hello World!"

print ("Original String: "+ teststring)

# Converting a string to lower case
print("Converting to Lowercase: "+ teststring.lower())

# Converting a string to upper case
print("Converting to Upper Case: "+ teststring.upper())

# Capitalizing a string
print("Capitalizing the String: "+ teststring.capitalize())

################################################################################################
# Trying to slice out a substring (of "Hello World!") between given indexes

# 1. Substring from index 1 to 7
# 2. Substring from the start till character at index = 7 (start of string is index 0)
# 3. Substring from the character at index = 7, till the end of the string
print("Substring from index 1 to 7: "+ teststring[1:8])
print("Substring from the start until index 7: "+ teststring[:8])
print("Substring from the character at index 7 until the end of the string: "+ teststring[7:])

#######################################################################################################
#Find the position of a substring within the string

# 1.1 This gives us the first index during a left to right scan. If the string is not found, it returns -1
print("Find the index from which the substring 'llo' begins within the test string: ")
print(teststring.find('llo')) #2
# 1.2
print("look for a substring which is not a part of the given string: ")
print(teststring.find('xxy')) #-1

# 2. Now, trying to find the index of a substring between specified indexes only
print("find a substring between specified indexes only: looking for 'l' between 4 and 9: ")
print(teststring.find('1',4,9)) #-1

#  3.1 rfind is used, to find the index from the reverse
#      So, teststring.rfind('l') will look for the last index of l in the string
print("find('l') on the given string returns the following index (scanning the string from left to right): ")
print(teststring.find('1')) #-1 supposed to be 2
#  3.2
print("rfind('l') on the given string returns the following index (this scans the string from right to left): ")
print(teststring.rfind('1')) #-1 supposed to be 9

# Now let us try to replace/substitute a substring of this string with another string
print("Replacing World with Planet: "+ teststring.replace("World","Planet"))

# Try to split the string, into separate words

# split it wherever there is a space
print("Splitting the string into words, wherever there is a space:") 
print(teststring.split(" ")) # ['Hello', 'World!']
print(teststring.rsplit(" ")) # ['Hello', 'World!']

# Remove leading and trailing whitespace characters
teststring2 = "Hello World!  "

print("Current Test String: "+ teststring2)
print("Length (there are whitespaces at the end): ")
print(len(teststring2))
print("Length after stripping: ") 
print(len(teststring2.strip()))