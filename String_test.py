#!/usr/bin/env python
# coding: utf-8

# In[198]:


"""All functions to implement for the first part of the Techincal test."""

#   imports, no other import is allowed.
# You don't have to necessary use them all to complete the test.
import math
from functools import reduce
from math import sqrt
from typing import Dict, List


# In[199]:


def unique_strings(strings_1: List[str], strings_2: List[str]) -> List[str]:   
    #Returns a list of unique strings sorted by alphabetic order.
        # 1
        
    # Arguments
    con = strings_1 + strings_2
        
    ## Result
    result = sorted(set(con)) 
    return [result]


# In[200]:


def unique_multiple_strings(*args: List[str]) -> List[str]:
    #Returns a list of unique strings sorted by alphabetic order with multiples arguments.
    
    result = sorted(set(sum(args,[])))
    
    return(result)


# In[307]:



class Word():
    
    def __init__(self, word: str) -> None:
        
        self._w = word # we use an underscore '_' to specify a private variable 

    def get_word(self) -> str:
        self._word = str.lower(self._w)
        return self._word

    def is_palindrome(self) -> bool: 
        self._word = self.get_word()
        return self._word == self._word[::-1]
        
    def is_kalindrome(self) -> bool:
        self._word = self.get_word()
        for i in range(0, int(len(self._word)/2)):
            if self._word[i] == self._word[len(self._word)-i-1]:
                return True,"Nothing to remove"
            else:
                self._word1 = self._word.replace(self._word[i], '')
                if self._word1[i] == self._word[len(self._word)-i-1]:
                    return True,"need to remove"+" "+ self._word[i]
                else:
                    return False


# In[312]:


if __name__ == "__main__":
    # Here is some material to test your code:
    strings_test_1 = ["a","b","c","d"]
    strings_test_2 = ["a","d","e","f"]
    strings_test_3 = ["b","d","f","g","h","i"]
    strings_test_4 = ["i","j","k","l","e"]
    simple = unique_strings(strings_test_1, strings_test_2)
    print(simple)
    multiples = unique_multiple_strings(
        strings_test_4, 
        strings_test_3,
        strings_test_1,
        strings_test_2
    )
    print(multiples)
    
    print(Word("anna").is_kalindrome()) # True
    print(Word("anna").is_palindrome()) # True
    print(Word("bob").is_palindrome()) # True
    print(Word("alex").is_palindrome()) # False
    print(Word("melvil").is_palindrome()) # False
    print(Word("yolo").is_kalindrome()) # True
    print(Word("olo").is_kalindrome()) # True
    print(Word("alo").is_kalindrome()) # False


# In[ ]:




