#!/usr/bin/env python3

__author__ = "Mike Blanchard"
__copyright__ = "Copyright 2020"
__credits__ = ["Cam Bortle"]
__license__ = "GPLv3"
__version__ = "0.0.0"
__maintainer__ = ""
__email__ = "mblancha@highpoint.edu"
__status__ = "Lab 5 Complete"

def main():
    
    n = int(input("How many sets are you going to input?: "))
    sum = 0
    product = 1
    
    for i in range(0,n):
        set = input("Enter set: ") 
        element = set.split(",")
        sum += len(element)
        product *= len(element)

    print("Using Sum Rule: ", sum)
    print("Using Product Rule: ", product)


if __name__ == "__main__": 
    main() 






        
