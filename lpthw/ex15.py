'''
	Reading Files
'''

from sys import argv # import modules argv from sys library

script, filename = argv

txt = open(filename) # call the function open() on ex15.py(filename) and return the value into variable txt

print(f"Here's your file {filename}:")
print(txt.read()) # called the read() function on variable txt to show the value of the variable txt

print("Type the filename again:")
file_again = input("> ") # setting a new value to the variable file_again

txt_again = open(file_again) # call the function open() on file_again and return the value into variable txt_again

print(txt_again.read()) # print the variable txt_again