# Real Estate Analytics Dashboard

## Project Overview

This project implements a comprehensive real estate data analytics pipeline using Azure cloud services and advanced data engineering techniques. It transforms raw property data from Maharashtra into actionable insights through automated collection, processing, and visualization.

![Architecture Diagram](path/to/your/architecture/image.png)

## Key Features

- Automated web scraping of 150,000+ real estate data points.
- Scalable data storage and processing using Azure services.
- Advanced analytics on 500,000+ property records across 3 cities.
- Interactive dashboards for data visualization.

## Technologies Used

- **Web Scraping**: Python (Selenium, Beautiful Soup 4), Azure Functions.
- **Data Storage**: Azure Data Lake Storage Gen2.
- **Data Processing**: Azure Databricks.
- **Analytics**: Azure Synapse Analytics.
- **Visualization**: Power BI, Custom dashboard (Python, Streamlit, Matplotlib).
- **Automation**: Azure Functions, Azure Data Factory.

## Project Architecture

1. **Data Collection**: 
   - Web scraping scripts hosted on Azure Functions
   - Secure credential management with Azure Key Vault

2. **Data Storage**:
   - Raw data stored in Azure Data Lake Storage Gen2

3. **Data Processing**:
   - Large-scale data transformation using Azure Databricks
   - Cleaned data stored in Azure SQL Database
   - Processed data sent to Azure Synapse Analytics

4. **Data Analysis & Visualization**:
   - Complex queries performed in Azure Synapse Analytics
   - Interactive dashboards created with Power BI
   - Custom PoC dashboard using Streamlit, hosted on Azure App Service

5. **Automation & Orchestration**:
   - Scheduled and event-triggered jobs using Azure Functions
   - Data pipelines managed by Azure Data Factory

