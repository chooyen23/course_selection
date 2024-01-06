#!/usr/bin/env python
# coding: utf-8


# In[44]:


import pandas as pd
import numpy as np
import streamlit as st

#Hide the github icon in streamlit cloud
st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# In[68]:


df = pd.read_pickle('data.pickle')


# Sample DataFrame

# Streamlit App
st.title('2024 Poly Course Comparison')

st.write("The number of courses for each Polytechnic")
table = df.groupby(by=['Poly'])['Course Name'].size()
table

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
    st.warning('Please select at least one item from the drop downlist.')

# In[79]:


df.set_index('MOE Course Code',inplace=True)
#df


# In[ ]:




