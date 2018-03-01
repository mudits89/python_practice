# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 16:36:21 2018

@author: mudit
"""

import numpy as np
x = np.random.normal(size = 7)
print(x)

import numpy as np
x = np.random.randint(low = 10, high = 30, size = 6)
print(x)

import numpy as np 
x = np.random.random((3, 3, 3))
print(x)

import numpy as np
x = np.random.random((5, 5))
print("Original Array:" )
print(x)
xmin, xmax = x.min(), x.max()
print("Minimum & Maximum values:" )
print(xmin, xmax)

import numpy as np
x = np.random.rand(10 , 4)
print("Original array:" )
print(x)
a = x[:5 , :]
print("First 5 rows of the above array:" )
print(a)

import numpy as np
x = np.arange(10)
np.random.shuffle(x)
print(x)
print(" Same result using permutation():" )
print(np.random.permutation(10))


import numpy as np
x = np.random.random((3,3))
print("Original Array: ")
print(x)
xmin, xmax = x.min(), x.max()
a = (x - xmin)/(xmax - xmin)
print("After normalization: ")
print(a)

import numpy as np
x = np.random.random(10)
print("Original Array: ")
print(x)
x.sort
print("Sorted Array: ")
print(x)
