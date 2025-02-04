import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Coffee Truck Data Analysis')

# Sample data since we can't access the local CSV
data = {
    'Location': ['Park', 'Business', 'Business', 'Park', 'Park', 'Business', 'Business', 'Park', 'Business', 'Park'],
    'Music': ['Alternative', 'Alternative', 'Alternative', 'HipHop', 'HipHop', 'HipHop', 'Alternative', 'Alternative', 'Alternative', 'HipHop'],
    'Price': [28, 35, 35, 32, 35, 32, 32, 32, 32, 32],
    'Sales': [64, 17, 22, 30, 27, 27, 30, 38, 29, 56],
    'Income': [1792, 595, 770, 960, 945, 864, 960, 1216, 928, 1792],
    'Cost': [1248, 919, 954, 1010, 989, 989, 1010, 1066, 1003, 1192],
    'Profit': [544, -324, -184, -50, -44, -125, -50, 150, -75, 600]
}

df = pd.DataFrame(data)

# 1. Location Frequency Table
st.header('1. Location Analysis')
location_freq = df['Location'].value_counts()
st.write("Location Frequency Table:")
st.write(location_freq)
st.write(f"Most frequent location: {location_freq.index[0]}")

# 2. Create and show Indicator variable
st.header('2. Profit/Loss Indicator')
df['Indicator'] = df['Profit'].apply(lambda x: 'Loss' if x < 0 else 'Profit')
st.write("First few rows with the new Indicator:")
st.write(df[['Location', 'Profit', 'Indicator']].head())

# 3. Frequency tables
st.header('3. Music and Indicator Frequencies')
col1, col2 = st.columns(2)

with col1:
    st.write("Music Frequency Table:")
    st.write(df['Music'].value_counts())

with col2:
    st.write("Indicator Frequency Table:")
    st.write(df['Indicator'].value_counts())

# 4. Histogram of profits
st.header('4. Profit Distribution')
fig1 = plt.figure(figsize=(10, 6))
plt.hist(df['Profit'], bins=15, edgecolor='black')
plt.title('Distribution of Coffee Truck Profits')
plt.xlabel('Profit ($)')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
st.pyplot(fig1)
plt.close()

# 5. Barplot of Music variable
st.header('5. Music Types Distribution')
fig2 = plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Music')
plt.title('Distribution of Music Types')
plt.xlabel('Music Type')
plt.ylabel('Count')
st.pyplot(fig2)
plt.close()

# 6. Side-by-side boxplot
st.header('6. Profit Distribution by Location')
fig3 = plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Location', y='Profit')
plt.title('Profit Distribution by Location')
plt.xlabel('Location')
plt.ylabel('Profit ($)')
st.pyplot(fig3)
plt.close()

# 7. Numerical summaries
st.header('7. Profit Summary Statistics by Location')
profit_summary = df.groupby('Location')['Profit'].describe()
st.write(profit_summary)

# 8. BONUS
st.header('8. BONUS - Zoo Analysis')
zoo_profitable = df[
    (df['Location'] == 'Zoo') & 
    (df['Profit'] > 0)
]

if len(zoo_profitable) > 0:
    mean_sales = zoo_profitable['Sales'].mean()
    st.write(f"Mean sales at Zoo when profitable: {mean_sales}")
else:
    st.write("No data available for Zoo location in the dataset")