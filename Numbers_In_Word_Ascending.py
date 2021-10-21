#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This program Checks if numbers in_Word are ascending:
# Logic: Check for the numbers in the word by splitting the string and then use single pointer
class Numbers_In_Word_Ascending:
    def areNumbersAscending(self, s):
        list_str = s.split(" ")
        areNumbersAscending = False
        num2 = -1
        for i in list_str:
            # To handle ValueError Exception
            try:
                if type(int(i)) is int:
                    num1= num2
                    num2 = int(i)
                    if num1<num2:
                        areNumbersAscending = True
                        continue
                    else:
                        areNumbersAscending = False
                        break
            except ValueError as ve:
                pass
        return areNumbersAscending

