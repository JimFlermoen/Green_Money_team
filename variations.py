#!/usr/bin/env python3.7

# python implementation here

message = input("Enter a message: ")

print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Caputalized:", message.capitalize())
print("Title Case:", message.title())

words = message.split()
print("words:", words)

sorted_words = sorted(words)
print("Alphabetic First Words:", sorted_words[0])
print("Alphabetic Last Words:", sorted_words[-1])
