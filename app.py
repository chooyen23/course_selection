#!/usr/bin/env python
# coding: utf-8

#Hide the github icon in streamlit cloud


# In[44]:


import pandas as pd
import numpy as np
import streamlit as st


# Hide the GitHub ribbon and other top menu items
st.markdown("""
<style>
/* This hides the hamburger menu (top right) */
header {visibility: hidden;}

/* This hides the GitHub corner icon */
.css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
.styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
.viewerBadge_text__1JaDK {
    display: none !important;
}

/* Additional elements can be hidden by adding their classes here */
</style>
""", unsafe_allow_html=True)

# In[68]:


df = pd.read_pickle('data.pickle')


# Sample DataFrame

# Streamlit App
st.title('Poly Course Aggregate Score Comparison')

# Sidebar content
st.sidebar.header("About")
st.sidebar.info(
    'The comparison is based on 2023 Aggregate Scores.')

st.write("The number of courses for each Polytechnic:")
df.dropna(inplace=True)
table = df.groupby(by=['Poly'])['Course Name'].size()
table = table.rename('Courses')

#Inject Custom CSS with st.markdown

st.markdown("""
<style>
table, th, td {
    table-layout: auto !important;
    width: auto !important;
    white-space: nowrap;
}
</style>
""", unsafe_allow_html=True)

st.table(table)

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




