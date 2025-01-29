# Required package installations 
# pip install streamlit pandas numpy altair plotly matplotlib pillow

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Complete Streamlit Demo", layout="wide")

# Sidebar
with st.sidebar:
    st.header("Sidebar Navigation")
    selected_city = st.selectbox("Select a city", ["New York", "Los Angeles", "Chicago"])
    st.write(f"You selected {selected_city}.")
    
    # Add sidebar widgets
    st.subheader("Settings")
    show_metrics = st.checkbox("Show Metrics", True)
    show_charts = st.checkbox("Show Charts", True)

# Main Content
st.title("Complete Streamlit Application Demo")

# User Input Section
st.header("User Input Section")
col1, col2 = st.columns(2)

with col1:
    # Text input
    name = st.text_input("Enter your name", "John Doe")
    st.write(f"Hello, {name}!")

    # Number input
    age = st.number_input("Enter your age", min_value=0, max_value=100, value=25)
    st.write(f"You are {age} years old.")

    # Slider
    height = st.slider("Select your height (in cm)", 100, 200, 175)
    st.write(f"Your height is {height} cm.")

with col2:
    # Selectbox
    city = st.selectbox("Select your city", ["New York", "Los Angeles", "Chicago"])
    
    # Multiselect
    hobbies = st.multiselect("Select your hobbies", ["Reading", "Traveling", "Coding", "Sports"])
    if hobbies:
        st.write(f"Your hobbies are: {', '.join(hobbies)}")
    
    # Checkbox
    agree = st.checkbox("I agree to the terms and conditions")
    if agree:
        st.success("Thank you for agreeing!")

# Data Display Section
st.header("Data Display Section")

# Create a DataFrame
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [50000, 60000, 75000, 65000, 70000]
})

# Display options
display_option = st.radio(
    "Choose display format:",
    ["Interactive Table", "Static Table", "JSON"]
)

if display_option == "Interactive Table":
    st.dataframe(data)
elif display_option == "Static Table":
    st.table(data)
else:
    st.json(data.to_dict())

# Visualization Section
if show_charts:
    st.header("Data Visualization Section")
    
    # Create tabs for different visualizations
    tab1, tab2, tab3, tab4 = st.tabs(["Scatter Plot", "Bar Chart", "Line Chart", "Area Chart"])
    
    with tab1:
        # Scatter plot using Altair
        df_scatter = pd.DataFrame(np.random.randn(500, 3), columns=['x', 'y', 'z'])
        chart = alt.Chart(df_scatter).mark_circle().encode(
            x='x',
            y='y',
            size='z',
            color='z',
            tooltip=['x', 'y', 'z']
        ).properties(title="Interactive Scatter Plot")
        st.altair_chart(chart, use_container_width=True)
    
    with tab2:
        # Bar chart
        st.subheader("Bar Chart")
        df_bar = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
        st.bar_chart(df_bar)
    
    with tab3:
        # Line chart
        st.subheader("Line Chart")
        df_line = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
        st.line_chart(df_line)
    
    with tab4:
        # Area chart
        st.subheader("Area Chart")
        df_area = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
        st.area_chart(df_area)

    # Plotly chart
    st.subheader("Plotly Chart Example")
    fig = px.line(data, x="Name", y="Salary", title="Salary Distribution")
    st.plotly_chart(fig, use_container_width=True)

# Metrics Section
if show_metrics:
    st.header("Metrics Section")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Temperature", value="24 °C", delta="1.2 °C")
    with col2:
        st.metric(label="Humidity", value="48%", delta="-2%")
    with col3:
        st.metric(label="Wind Speed", value="15 km/h", delta="3 km/h")

# File Upload Section
st.header("File Upload Section")
uploaded_file = st.file_uploader("Choose an image file", type=['png', 'jpg', 'jpeg'])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Expander
with st.expander("Click to see more information"):
    st.write("This is hidden content that can be expanded.")
    st.markdown("""
    ### Features demonstrated in this app:
    - Basic input widgets
    - Data display options
    - Various chart types
    - File upload functionality
    - Metrics and indicators
    - Layout options (columns, tabs, expanders)
    """)

# Progress and Status Indicators
st.header("Progress and Status Indicators")

# Progress bar
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)

# Success/Info/Warning/Error messages
st.success("This is a success message!")
st.info("This is an informational message")
st.warning("This is a warning message")
st.error("This is an error message")

# Exception
exp = ZeroDivisionError("Example error message")
st.exception(exp)

# Balloons
if st.button("Celebrate!"):
    st.balloons()

# Footer
st.markdown("---")
st.markdown("### Created with Streamlit")
with st.expander("About this app"):
    st.write("""
    This is a comprehensive demo of Streamlit features including:
    - Input widgets
    - Data visualization
    - Layout options
    - Status indicators
    - File handling
    - And more!
    """)