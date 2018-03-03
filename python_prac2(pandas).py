# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 13:14:24 2018

@author: mudit
"""

import pandas as pd
s = pd.Series([1, 2, 3, 5, 8, 9])
print(s)

import pandas as pd
s = pd.Series([1, 2, 3, 5, 8, 9])
print(s)
print(type(s))
print (s.dtype)
print("Convert pandas series to python list")
print(s.tolist())
print(type(s.tolist()))

import pandas as pd
s1 = pd.Series([1,2,3,4])
s2 = pd.Series([0,1,2,3])
print("Add two series:")
s = s1 +s2
print(s)
print("\n"+"Subtract two series:")
s = s1 - s2
print(s)
print("\n"+"Multiply two series:")
s = s1*s2
print(s)
print("\n"+"Divide two series:")
s = s1/s2
print(s)  

import pandas as pd
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([0,1,2,3,5])
print("Series 1:")
print(s1)
print("Series 2:")
print(s2)
print("Compare elements of the said series:")
print("Equals:")
print(s1 == s2)
print("Greater than:")
print(s1 > s2)
print("Less than:")
print(s1 < s2)
