"""
This module is looping over a given list
when it reaches the end, it starts from the beginning
I used that for splitting the test into different test lists
"""

import itertools

mylist = [1,2,3,4,5,6,7]

sequence = itertools.cycle(mylist)

for i in range(20):
    print sequence.next()