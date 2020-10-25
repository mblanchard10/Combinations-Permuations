#!/usr/bin/env python3

__author__ = "Mike Blanchard"
__copyright__ = "Copyright 2020"
__credits__ = ["Cam Bortle"]
__license__ = "GPLv3"
__version__ = "0.0.0"
__maintainer__ = ""
__email__ = "mblancha@highpoint.edu"
__status__ = "Lab 5 Complete"
import math

def main():

    o = input("Does order matter? Enter y for yes and n for no: ")
    sum = 0
    product = 1
    
    if o == 'n' or o == 'N':
        n = int(input("How many sets are you going to input?: "))
        for i in range(0,n):
            set = input("Enter set: ") 
            element = set.split(",")
            sum += len(element)
            product *= len(element)
    elif o == 'y' or o == 'Y':
        set1 = input("Enter all elements of the set (n): ") 
        element1 = set1.split(",")
        sub = int(input("Enter the size of the subset(r): "))

        sum = len(element1) + sub
        if sub == 0:
            product = math.factorial(len(element1))
        elif sub != 0:
            product = (math.factorial(len(element1))) / (math.factorial(len(element1) - sub))

    print("Using Sum Rule: ", sum)
    print("Using Product Rule: ", product)

if __name__ == "__main__": 
    main() 






        
