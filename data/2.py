import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Coffee Truck Data Analysis')

# Read the data
@st.cache_data
def load_data():
    return pd.read_csv("CoffeeTruck.csv")

df = load_data()

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
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.hist(df['Profit'], bins=15, edgecolor='black')
ax1.set_title('Distribution of Coffee Truck Profits')
ax1.set_xlabel('Profit ($)')
ax1.set_ylabel('Frequency')
ax1.grid(True, alpha=0.3)
st.pyplot(fig1)

# 5. Barplot of Music variable
st.header('5. Music Types Distribution')
fig2, ax2 = plt.subplots(figsize=(8, 6))
sns.countplot(data=df, x='Music', ax=ax2)
ax2.set_title('Distribution of Music Types')
ax2.set_xlabel('Music Type')
ax2.set_ylabel('Count')
st.pyplot(fig2)

# 6. Side-by-side boxplot
st.header('6. Profit Distribution by Location')
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x='Location', y='Profit', ax=ax3)
ax3.set_title('Profit Distribution by Location')
ax3.set_xlabel('Location')
ax3.set_ylabel('Profit ($)')
st.pyplot(fig3)

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