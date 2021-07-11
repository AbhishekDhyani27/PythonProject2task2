# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 10:52:17 2021

@author: dhyani
"""

# Python program to print positive Numbers in a List
  
# list of numbers
list1 = [12,-7,5,64,-14]
num = 0
  
# using while loop     
while(num < len(list1)):
      
    # checking condition
    if list1[num] >= 0:
        print(list1[num], end = " ")
      
    # increment num 
    num += 1