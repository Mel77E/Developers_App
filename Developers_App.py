import streamlit as st
import pandas as pd
!pip install matplotlib
pip install -r requirements.txt
import seaborn as sns
import plotly.express as px
import numpy as np

# Function to load the model (if needed)
def load_model(filename='best_model_xgb.pkl'):
    import pickle
    with open(filename, 'rb') as f:
        model = pickle.load(f)
    return model

# Load the model (optional, if you have a model to use for predictions)
# model = load_model()

# Streamlit app
st.title('Developers 2023')

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded file
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:")
    st.write(df)

    # Display basic statistics
    st.subheader("Basic Statistics")
    st.write(df.describe())

    # Visualize data
    st.subheader("Data Visualizations")

    # Histogram for each numerical column
    numerical_columns = df.select_dtypes(include=[np.number]).columns
    for col in numerical_columns:
        st.write(f"Histogram of {col}")
        fig, ax = plt.subplots()
        sns.histplot(df[col], ax=ax, kde=True)
        st.pyplot(fig)

    # Scatter plot for numerical columns
    if len(numerical_columns) > 1:
        x_col = st.selectbox("Select x-axis for scatter plot", numerical_columns)
        y_col = st.selectbox("Select y-axis for scatter plot", numerical_columns)
        if x_col != y_col:
            st.write(f"Scatter plot of {x_col} vs {y_col}")
            fig = px.scatter(df, x=x_col, y=y_col, title=f"Scatter plot of {x_col} vs {y_col}")
            st.plotly_chart(fig)

    # Correlation heatmap
    st.subheader("Correlation Heatmap")
    if len(numerical_columns) > 1:
        correlation = df[numerical_columns].corr()
        fig, ax = plt.subplots()
        sns.heatmap(correlation, annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

    # Bar chart for categorical columns like Education Level
    categorical_columns = df.select_dtypes(include=[object]).columns
    education_column = st.selectbox("Select the Education column", categorical_columns)
    if education_column:
        st.write(f"Bar chart of {education_column}")
        fig, ax = plt.subplots()
        df[education_column].value_counts().plot(kind='bar', ax=ax)
        ax.set_title(f'Distribution of {education_column}')
        st.pyplot(fig)

    # Pie chart for categorical columns like Employment Status
    employment_column = st.selectbox("Select the Employment Status column", categorical_columns)
    if employment_column:
        st.write(f"Pie chart of {employment_column}")
        fig, ax = plt.subplots()
        df[employment_column].value_counts().plot(kind='pie', ax=ax, autopct='%1.1f%%', startangle=90)
        ax.set_title(f'Distribution of {employment_column}')
        st.pyplot(fig)

    # Learning methods visualization
    learning_column = st.selectbox("Select the Learning Methods column", categorical_columns)
    if learning_column:
        st.write(f"Learning Methods Bar Chart")
        fig, ax = plt.subplots()
        df[learning_column].value_counts().plot(kind='bar', ax=ax)
        ax.set_title(f'Distribution of Learning Methods')
        st.pyplot(fig)



    # Button to download the CSV file
    @st.cache_data
    def convert_df(df):
        return df.to_csv().encode('utf-8')

    csv = convert_df(df)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='data_with_visualizations.csv',
        mime='text/csv',
    )
else:
    st.write("Please upload a CSV file.")



