# Dynamic-Airspace-Monitoring
Real-Time Visualization Using Snowflake, Amazon Kinesis Data Firehose, and Streamlit
## Overview
This project demonstrates an innovative solution integrating Snowflake, Amazon Kinesis Data Firehose (ADF), and Streamlit to handle and visualize real-time commercial flight data over the San Francisco Bay Area. This setup facilitates efficient data ingestion, storage, and dynamic visualization, essential for monitoring air traffic within this major hub.

## Architecture
**Data Capture:** Utilize the OpenSky Network to capture live flight data.
**Data Ingestion and Storage:**

a) Amazon Kinesis Data Firehose: Stream data in real-time, applying necessary transformations before loading it into Snowflake.

b) Snowflake: Store and analyze the processed data.

## Visualization:
**Streamlit:** A user-friendly web app to visualize the real-time data through interactive graphs and maps.

## Key Components

**AWS (Amazon Web Services):**

=> EC2 Instance: Hosts the data producer for ingesting data into the Firehose delivery stream.

=> Amazon Kinesis Data Firehose: Manages the real-time data flow between the data source and Snowflake.

**Snowflake:** Manages large datasets using a scalable cloud data warehouse.

**Streamlit:** Provides dynamic visualization capabilities.


## Project Setup
**1. Provision a Linux Jumphost in AWS**
Launch an EC2 instance using AWS CloudFormation.
Configure the instance with an **ADMIN** role to access Kinesis Data Firehose and execute necessary scripts.


**2. Configure Snowflake**
Set up user roles, warehouse, database, and schema as required for the project.
Execute SQL scripts to prepare the database environment for receiving and querying data.


**3. Create an ADF Delivery Stream**
Configure the delivery stream to ingest data directly into Snowflake using PrivateLink to secure communications.


**4. Install Python and Dependencies**
Python 3.x
Streamlit
Pandas
Snowflake Connector for Python
Matplotlib


## Running the Application
**Configure the Streamlit Script:**
Set the Snowflake connection parameters in the script.
Ensure the query is tailored to fetch the desired data.

## Execute Streamlit:
Run the Streamlit script using streamlit run **app.py** to start the web application.
Access the application through the local URL provided by Streamlit.

## Visualization Details
Arrivals by Destination Airport: Visualizes the number of arrivals at each destination using a bar chart.
Interactive Elements: Users can interact with the visualization to explore different time frames or airports.

## Conclusion
This project illustrates a comprehensive real-time data processing and visualization system integrating advanced cloud technologies and dynamic visualization tools. It not only enhances operational efficiencies but also supports proactive decision-making and safety management in air traffic control.
