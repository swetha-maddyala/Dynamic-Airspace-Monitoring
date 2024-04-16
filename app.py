import streamlit as st
import pandas as pd
from snowflake.connector import connect
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Connect to Snowflake
conn = connect(
    user='STREAMING_USER',
    password='Test1234567',
    role='ADF_STREAMING_RL',
    account='gncpega-sfb41498',
    warehouse='ADF_STREAMING_WH',
    database='ADF_STREAMING_DB',
    schema='ADF_STREAMING_SCHEMA_1'
)

def load_data():
    query = "SELECT DEST, TS_PT FROM flights_vw"
    cursor = conn.cursor()
    cursor.execute(query)
    df = pd.DataFrame.from_records(iter(cursor), columns=[x[0] for x in cursor.description])
    cursor.close()

    # Convert 'TS_PT' to a datetime
    df['TS_PT'] = pd.to_datetime(df['TS_PT'])

    return df

# Load the data
df = load_data()

# Count arrivals by airport
arrivals_by_airport = df.groupby('DEST')['TS_PT'].count().sort_values(ascending=False)

# Streamlit interface setup

# Define custom colors for each airport
custom_colors = ['skyblue', 'orange', 'green', 'red', 'purple']  # Add more colors if needed

# Create a bar chart with custom colors and transparent background
fig, ax = plt.subplots()  # Set the face color to black
arrivals_by_airport.plot(kind='bar', color=custom_colors, ax=ax)  

# Setting title, x-label, and y-label
ax.set_title("Arrivals by Destination Airport", fontsize=20, color='red')
ax.set_xlabel("Destination Airport", fontsize=14, color='darkgreen')  
ax.set_ylabel("Number of Arrivals", fontsize=14, color='darkgreen')

# Coloring the 'DEST' x-axis labels
ax.tick_params(axis='x', colors='chocolate') 

# Remove spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Display the plot
st.pyplot(fig)





