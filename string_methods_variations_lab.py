#!/usr/bin/env python3.7

# python implementation here

# creates "message" as a variable to prompt "Enter a message" and then the user enters a message
message = input("Enter a message: ")

#Print the Lowercase, Uppercase, Capitalized, and Title Case Versions of the User's Input

#The lowercase version using str.lower
print("Lowercase:", message.lower()) 

#The uppercase version using str.upper
print("Uppercase:", message.upper())

#The capitalized version using str.capitalize
print("Capitalized:", message.capitalize())

#The title case version using str.title
print("Title Case:", message.title())

#Separate the String and Present the Individual Words as a List

# words variable is the message variable that will split at each space
words = message.split()
print("words:", words)

#Print the Alphabetic First and Last Words from the User's Input

# makes a sorted list of the words variable and prints the first and last words 
# sorted alphabetic by alpha order
sorted_words = sorted(words)
print("Alphabetic First Words:", sorted_words[0])
print("Alphabetic Last Words:", sorted_words[-1])