import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

# Load your CSV file
data = pd.read_csv("your_data.csv")

# Display the data
st.write(data)

# Visualization 1: Education Levels
st.subheader('Education Levels')
fig1, ax1 = plt.subplots()
sns.countplot(y='EdLevel', data=data, ax=ax1)
st.pyplot(fig1)

# Visualization 2: Employment Status
st.subheader('Employment Status')
fig2, ax2 = plt.subplots()
sns.countplot(y='Employment', data=data, ax=ax2)
st.pyplot(fig2)

# Visualization 3: How They Learn
st.subheader('How They Learn')
fig3, ax3 = plt.subplots()
sns.countplot(y='LearnCode', data=data, ax=ax3)
st.pyplot(fig3)

# Visualization 4: Plotly Example
st.subheader('Age Distribution')
fig4 = px.histogram(data, x='Age')
st.plotly_chart(fig4)
