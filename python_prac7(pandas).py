# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 20:45:35 2018

@author: mudit
"""

import numpy as np
import pandas as pd

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

d = pd.DataFrame(exam_data, index = labels)
print("Original Rows:")
print(d)
print("\n Delete the 'attempts'column from the dataframe:")
d.pop('attempts')
print(d)


import numpy as np
import pandas as pd

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

d = pd.DataFrame(exam_data, index = labels)
print("Original Rows:")
print(d)
colour = ['Red', 'Blue', 'Green', 'White', 'Black', 'Orange', 'Silver', 'Grey', 'Peach', 'Purple']
d['colour'] = colour
print("\n Insert a new column in existing Data Frame:")
print(d)


import numpy as np
import pandas as pd 
exam_data = [{'name':'Anastasia', 'score':13}, {'name':'Dima','score': 9}, {'name': 'Katherine','score':16.5}]
d = pd.DataFrame(exam_data)
for index,row in d.iterrows():
    print(row['name'],row['score'])
    
    
import numpy as np
import pandas as pd

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
d = pd.DataFrame(exam_data, index = labels)
print(list(d.columns.values))