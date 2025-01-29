import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image
import time

# Page config
st.set_page_config(page_title="Streamlit Demo App", layout="wide")

# Title
st.title("Streamlit is Amazing")

# Sidebar
st.sidebar.header("Sidebar")
selected_city = st.sidebar.selectbox("Select a city", ["New York", "Los Angeles", "Chicago"])
st.sidebar.write(f"You selected {selected_city}.")

# Main Layout - Two Columns
col1, col2 = st.columns(2)

with col1:
    st.header("User Information")
    
    # Text input with submit button
    name = st.text_input("Enter your name", "Type Here ...")
    if st.button('Submit'):
        result = name.title()
        st.success(result)
    
    # Number inputs
    age = st.number_input("Enter your age", min_value=0, max_value=100, value=25)
    st.write(f"You are {age} years old.")
    
    # Slider
    height = st.slider("Select your height (in cm)", 100, 200, 175)
    st.write(f"Your height is {height} cm.")
    
    # Level slider
    level = st.slider("Select the level", 1, 5)
    st.text(f'Selected: {level}')

with col2:
    st.header("Preferences")
    
    # Gender selection
    status = st.radio("Select Gender:", ('Male', 'Female'))
    if status == 'Male':
        st.success("Male")
    else:
        st.success("Female")
    
    # Hobbies selection
    hobby = st.selectbox("Select a hobby:", ['Dancing', 'Reading', 'Sports'])
    st.write("Your hobby is:", hobby)
    
    # Multiple hobbies
    hobbies = st.multiselect("Select multiple hobbies:", ['Dancing', 'Reading', 'Sports'])
    st.write("You selected", len(hobbies), 'hobbies')

# Data Display Section
st.header("Data Visualization")

# Create sample DataFrame
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

# Create tabs for different visualizations
tab1, tab2, tab3, tab4 = st.tabs(["Interactive Table", "Charts", "Plotly", "Images"])

with tab1:
    st.subheader("Data Display")
    st.dataframe(data)
    st.table(data)
    st.json(data.to_dict())

with tab2:
    # Random data visualizations
    df = pd.DataFrame(np.random.randn(500, 3), columns=['x', 'y', 'z'])
    
    # Altair chart
    chart = alt.Chart(df).mark_circle().encode(
        x='x', 
        y='y', 
        size='z', 
        color='z', 
        tooltip=['x', 'y', 'z']
    )
    st.altair_chart(chart, use_container_width=True)
    
    # Other charts
    st.bar_chart(df[['x', 'y']])
    st.line_chart(df[['x', 'y']])
    st.area_chart(df[['x', 'y']])

with tab3:
    # Plotly chart
    plot_data = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})
    fig = px.line(plot_data, x="x", y="y", title="Simple Plotly Example")
    st.plotly_chart(fig)

with tab4:
    # Image display section
    st.subheader("Image Display")
    try:
        img = Image.open("streamlit.png")
        st.image(img, width=200, caption="Streamlit Logo")
    except FileNotFoundError:
        st.error("Image file 'streamlit.png' not found. Please ensure the image exists in the same directory.")
    
    try:
        kid_img = Image.open("kid.jpg")
        st.image(kid_img, caption="A kid playing")
    except FileNotFoundError:
        st.error("Image file 'kid.jpg' not found. Please ensure the image exists in the same directory.")

# Interactive Elements
st.header("Interactive Elements")

# Expander
with st.expander("Click to expand"):
    st.write("This content is hidden by default.")
    st.write("You can add more content here.")

# Container
with st.container():
    st.write("This is inside the container")
    
    # Show/Hide checkbox
    if st.checkbox("Show/Hide"):
        st.text("Showing the widget")

# File uploader
st.file_uploader('Upload a photo')

# Additional inputs
st.date_input('Traveling date')
st.time_input('School time')
st.text_area('Description')
st.color_picker('Choose your favorite color')

# Status indicators
st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")

# Exception example
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

# Progress bar
progress = st.progress(0)
for i in range(10):
    progress.progress((i + 1) * 10)
    time.sleep(0.1)

# Spinner
with st.spinner('Wait for it...'):
    time.sleep(1)

# Celebration
if st.button("Celebrate!"):
    st.balloons()

# Footer
st.markdown("---")
st.markdown("### Created with Streamlit")