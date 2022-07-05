#!/usr/bin/env python
# coding: utf-8

# In[1]:


#q1
import numpy as np


a = np.array([[0, 1, 3], [5, 7, 9]])
b = np.array([[0, 2, 4], [6, 8, 10]])
c = np.concatenate((a, b), axis=0)
print(c)


# In[8]:


#q5
# Import pandas library #q5
import pandas as pd
 
# initialize list of lists
data = [['DS', 'Linked_list', 10], ['DS', 'Stack', 9], ['DS', 'Queue', 7],
        ['Algo', 'Greedy', 8], ['Algo', 'DP', 6], ['Algo', 'BackTrack', 5], ]
 
# Create the pandas DataFrame
df = pd.DataFrame(data, columns = ['Category', 'Name', 'Marks'])
 
# print dataframe.
print(df )


# In[5]:


#q2
import numpy as np
list3=[[1,2],[12,45],[3,5],[56,78]]
list4=np.array(list3)
print(list4)
np.array([12,45]) in list4


# In[6]:


#q4
import pandas as pd
 
# initialise data of lists.
data = {'Category':['Array', 'Stack', 'Queue'],
        'Marks':[20, 21, 19]}
 
# Create DataFrame
df = pd.DataFrame(data)
 
# Print the output.
print(df )


# In[7]:


#q3
import pandas as pd
import numpy as np

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print(df)


# In[ ]:




