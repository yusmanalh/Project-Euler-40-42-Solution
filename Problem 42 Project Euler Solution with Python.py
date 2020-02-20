#!/usr/bin/env python
# coding: utf-8

# In[1]:


# http://radiusofcircle.blogpspot.com

# time module
import time

# sqrt for calculating square root
from math import sqrt

# time at the start of program execution
start = time.time()

# open the file words.txt
f = open('words.txt')

# read the whole file
words = f.read()

# close the file
f.close()

# split the words into a list
words = words.strip().split(',')


def convert(character):
    """function to convert the
    words to alphabetical position"""
    return ord(character)-64

# counter to count the number of instances
counter = 0

# for loop to loop through the words
for word in words:
    # convert the words to numbers and find the sum
    x = sum(map(convert, word[1:-1]))
    # check if the given number is triangle
    if sqrt(8*x+1) == int(sqrt(8*x+1)):
        counter += 1

# printing the result
print (counter)

# time at the end of program execution
end = time.time()

# total time taken
print (end-start)


# In[ ]:




