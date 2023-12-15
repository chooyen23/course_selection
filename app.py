#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pandas as pd
import numpy as np
import streamlit as st
import os

# In[68]:


current_directory = os.getcwd()

#Construct a relative path 

relative_path = os.path.join(current_directory, 'data', 'Poly 2023 LAS Reference.xlsx')



df =dict()
sheet_names = pd.ExcelFile(relative_path).sheet_names

for sheet in sheet_names:
    df[sheet]=pd.read_excel(relative_path,sheet_name=sheet)
    df[sheet]['Poly'] = sheet

df= pd.concat(df, ignore_index=True)


# In[71]:


df.columns = df.columns.str.strip()


# In[84]:


df['Poly-Course']= df['Course Name']+" "+"("+ df['MOE Course Code']+")"

df.sort_values(by='Poly-Course',inplace=True)



# In[78]:


# Sample DataFrame

# Streamlit App
st.title('2024 Poly Course Comparison')

# Multiselect to choose multiple items
selected_items = st.multiselect('Choose Course:', df['Poly-Course'])

# Button to trigger result display
result_button = st.button('Result')

# Display the selected items from the DataFrame
if result_button:
    selected_rows = df[df['Poly-Course'].isin(selected_items)]
    st.write('### Selected Items Details:')
    for index, row in selected_rows.iterrows():
        st.write(f"**Course:** {row['Poly']} {row['Poly-Course']}, **Range of Aggregate Score:** {row['2023 Range of Aggregate Score (Net)']}")
        
else:
    st.warning('Please select at least one item.')

# In[79]:


df.set_index('MOE Course Code',inplace=True)
df


# In[ ]:




