#!/usr/bin/env python
# coding: utf-8

# In[1]:


#
import pandas as pd
import numpy as np
import glob
data = pd.DataFrame()
for i in glob.glob(r"C:/MUNJA_DATA/Courses/Data Visualization/Week-7/learn-data-analysis-w-python-master/datasets/weekly_call_data*.xlsx"):
    df = pd.read_excel(i)
    data = data.append(df,ignore_index=True)
data.head()


# In[ ]:




