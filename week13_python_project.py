#!/usr/bin/env python3.7

#import os allows us to run a command in the Python script
import os

# Change to my working directory
os.chdir('/home/ec2-user/environment/Green_Money_team')

# Create empty file
files = []

# Naming of working directory variable
working_dir = os.getcwd()

# Making files into a list
for file in os.listdir(working_dir):
    
# Get the path/name of the file
    file_path = os.path.realpath(file)
    
# Get the file size    
    file_size = os.path.getsize(file)
    
# Append the file path/name and size to the list of dicionaries
    files.append({'path': file_path, 'size': file_size})

# Print the list of files, each on a new line    
print(*files, sep='\n')