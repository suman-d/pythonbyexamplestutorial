#! /usr/bin/env python

"""
Write a program to solve (a + b) * ( a + b).
"""

# Below is function definition
def main():
    # Create variables a and b.
    # Use the formula a * a + 2 * a * b + b * b
    # print the result back
    # (5 + 3) * (5 + 3)
    a, b = 5, 3
    result = a * a + 2 * a * b + b * b
    print "({} + {}) ^ 2) = {}".format(a, b, result)

# __name__ holds the name of the current module
if __name__ == "__main__":
    main() # call main function
