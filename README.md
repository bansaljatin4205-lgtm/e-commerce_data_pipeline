E-Commerce Data Pipeline

Project Overview

This project analyzes e-commerce order data using Python, Pandas, and MySQL. It cleans the data and displays sales insights through an interactive dashboard.

Technologies Used

- Python
- Pandas
- MySQL
- Streamlit
- Plotly
- CSV

Features

- Loads order data from a CSV file.
- Removes duplicate orders.
- Handles missing values and invalid dates.
- Calculates revenue using quantity × price.
- Stores order records in MySQL.
- Displays interactive sales charts.
- Filters sales by city and date.

Project Structure

- "main.py" — Main Python file
- "load_data.py" — Loads data into MySQL
- "data/app.py" — Sales dashboard
- "data/clean_data.py" — Data cleaning
- "data/orders.csv" — Original dataset
- "data/cleaned_orders.csv" — Cleaned dataset

How to Run

1. Install the required Python libraries.
2. Configure your MySQL database credentials.
3. Run the cleaning script:
   "python data/clean_data.py"
4. Start the dashboard:
   "python -m streamlit run data/app.py"

Learning Outcomes

This project demonstrates data cleaning, data processing, MySQL integration, and data visualization.