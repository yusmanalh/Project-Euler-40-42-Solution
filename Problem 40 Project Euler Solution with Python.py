#!/usr/bin/env python
# coding: utf-8

# In[31]:


def func():
    """Calculate the product.
    """
    prod = 1
    i = 1
    while i <= 1000000:
        prod *= get_digit(i)
        i *= 10
    return prod
 
# single-digit, total space: 9*1
# double-digit, total space: 90*2
# triple-digit, total space: 900*3
# ...
def get_digit(index):
    """Get the index-th digit of the fractional part.
    """
    i = 1
    n = 9
    while index - n * i > 0:
        index -= n * i
        i += 1
        n *= 10
    the_number = 10 ** (i-1) + (index-1) // i
    return int(str(the_number)[(index%i)-1])
     
if __name__ == '__main__':
    print(func())


# In[ ]:




