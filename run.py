import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page title
st.title('GitHub Projects Dashboard - Sumesh (officialsumesh07@gmail.com)')

# Load dataset
st.write("Loading dataset...")
data = pd.read_csv('github_dataset.csv')  # Use the appropriate dataset here
st.write("Dataset loaded successfully!")

# Display the first few rows of the dataset
st.subheader('Sample of the Dataset')
st.write(data.head())

# Display basic statistics
st.subheader('Dataset Summary')
st.write(data.describe())

# Example Visualization 1: Distribution of stars
st.subheader('Distribution of GitHub Project Stars')
fig, ax = plt.subplots()
ax.hist(data['stars_count'], bins=20, color='skyblue', edgecolor='black')  # Updated to 'stars_count'
ax.set_xlabel('Stars')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Example Visualization 2: Projects by Language
st.subheader('Top 10 Languages Used in Projects')
top_languages = data['language'].value_counts().head(10)
fig, ax = plt.subplots()
ax.bar(top_languages.index, top_languages.values, color='green')
ax.set_xlabel('Language')
ax.set_ylabel('Number of Projects')
ax.set_xticklabels(top_languages.index, rotation=45)
st.pyplot(fig)

# Filter projects by stars (interactive)
st.subheader('Filter Projects by Stars')
min_stars = st.slider('Minimum number of stars', min_value=int(data['stars_count'].min()), max_value=int(data['stars_count'].max()), value=50)
filtered_data = data[data['stars_count'] >= min_stars]

st.write(f'Projects with at least {min_stars} stars')
st.write(filtered_data[['repositories', 'stars_count', 'language', 'forks_count']])

# Add a footer
st.write("Dashboard created using Streamlit.")