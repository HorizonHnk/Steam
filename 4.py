import streamlit as st
import pandas as pd
import numpy as np
# Import matplotlib and seaborn after setting backend
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(page_title="Coffee Truck Analysis")

st.title('Coffee Truck Data Analysis')

# Sample data
data = {
    'Location': ['Park', 'Business', 'Business', 'Park', 'Park', 'Business', 'Business', 'Park', 'Business', 'Park'],
    'Music': ['Alternative', 'Alternative', 'Alternative', 'HipHop', 'HipHop', 'HipHop', 'Alternative', 'Alternative', 'Alternative', 'HipHop'],
    'Profit': [544, -324, -184, -50, -44, -125, -50, 150, -75, 600]
}

df = pd.DataFrame(data)

# 1. Location Analysis
st.header('1. Location Analysis')
location_freq = df['Location'].value_counts()
st.write("Location Frequency Table:")
st.dataframe(location_freq)

# 2. Profit/Loss Indicator
st.header('2. Profit/Loss Indicator')
df['Indicator'] = df['Profit'].apply(lambda x: 'Loss' if x < 0 else 'Profit')
st.write("Sample with Indicator:")
st.dataframe(df[['Location', 'Profit', 'Indicator']].head())

# 3. Frequencies
st.header('3. Music and Indicator Frequencies')
col1, col2 = st.columns(2)

with col1:
    st.write("Music Frequency:")
    st.dataframe(df['Music'].value_counts())

with col2:
    st.write("Profit/Loss Frequency:")
    st.dataframe(df['Indicator'].value_counts())

# 4. Profit Distribution
st.header('4. Profit Distribution')
fig, ax = plt.subplots()
plt.hist(df['Profit'], bins=10)
plt.title('Profit Distribution')
plt.xlabel('Profit ($)')
plt.ylabel('Frequency')
st.pyplot(fig)
plt.close()

# 5. Music Distribution
st.header('5. Music Types')
fig, ax = plt.subplots()
sns.countplot(data=df, x='Music')
plt.title('Music Types Distribution')
st.pyplot(fig)
plt.close()

# 6. Profit by Location
st.header('6. Profit by Location')
fig, ax = plt.subplots()
sns.boxplot(data=df, x='Location', y='Profit')
plt.title('Profit Distribution by Location')
st.pyplot(fig)
plt.close()

# 7. Summary Statistics
st.header('7. Profit Summary by Location')
profit_summary = df.groupby('Location')['Profit'].describe()
st.dataframe(profit_summary)

# 8. Bonus
st.header('8. BONUS - Zoo Analysis')
st.write("No Zoo location data available in the dataset")