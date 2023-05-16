#!/usr/bin/python3

def add_tuples(a, b):
    x = a[0] + b[0]
    y = a[1] + b[1]
    return (x, y)


result = add_tuples((1, 2), (3, 4))
print(result)
