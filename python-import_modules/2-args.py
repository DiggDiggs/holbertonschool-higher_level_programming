#!/usr/bin/python3
def reverse_string(string):
    if string == "":
        return ""
    elif string == "Hello":
        return "olleH"
    else:
        return string[::-1]

print(reverse_string("hello")) # Output: olleh
print(reverse_string("world")) # Output: dlrow
print(reverse_string("")) # Output: 
print(reverse_string("Hello")) # Output: olleH
