#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 3. Write a Python program to find the volume of a sphere with diameter 12 cm.

import math
D =int(input("Enter the Diameter of a sphere:"))
r = D/2
V  = 4.0/3.0 * math.pi* r ** 3
print('The volume of the sphere is:',V)


# In[3]:


# 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

firstname = input("Input your First Name :")
lastname = input("Input your Last Name :")
print (lastname,firstname)


# In[5]:


# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printedin a comma-separated sequence on a single line.

Result1=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        Result1.append(str(i))

print(','.join(Result1))

