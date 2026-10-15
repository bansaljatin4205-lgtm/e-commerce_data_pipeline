import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector
import os 
# Dashboard layout
st.set_page_config(
    page_title="E-Commerce Sales Dashboard",
    page_icon="🛒",
    layout="wide"
)

# MySQL se data lena

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="ecommerce_db"
)

df = pd.read_sql("SELECT * FROM orders", connection)
connection.close()

# Revenue calculate karna
df["revenue"] = df["quantity"] * df["price"]
df["order_date"] = pd.to_datetime(df["order_date"])

# Dashboard heading
st.title("🛒 E-Commerce Sales Dashboard")
st.write("Analyze your e-commerce sales data.")

# City Filter
st.subheader("🔍 Filter Sales by City")

city_list = ["All Cities"] + sorted(
    df["city"].dropna().unique().tolist()
)

selected_city = st.selectbox("Select City", city_list)

if selected_city != "All Cities":
    filtered_df = df[df["city"] == selected_city].copy()
else:
    filtered_df = df.copy()

# Date Filter
st.subheader("📅 Filter Sales by Date")

selected_date = st.date_input(
    "Select Order Date",
    value=None
)

if selected_date is not None:
    filtered_df = filtered_df[
        filtered_df["order_date"].dt.date == selected_date
    ].copy()

# Metrics - selected filters ke according
total_orders = len(filtered_df)
total_revenue = filtered_df["revenue"].sum()
total_quantity = filtered_df["quantity"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Orders", total_orders)
col2.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col3.metric("Items Sold", total_quantity)

# City-wise Sales Chart
st.subheader("🏙️ City-wise Sales")

city_sales = (
    filtered_df.groupby("city", as_index=False)["revenue"]
    .sum()
    .sort_values("revenue", ascending=False)
)

city_chart = px.bar(
    city_sales,
    x="city",
    y="revenue",
    title="Sales by City",
    labels={"city": "City", "revenue": "Revenue (₹)"}
)

st.plotly_chart(city_chart, use_container_width=True)

# Product-wise Sales Chart
st.subheader("📦 Product-wise Sales")

product_sales = (
    filtered_df.groupby("product", as_index=False)["revenue"]
    .sum()
    .sort_values("revenue", ascending=False)
)

product_chart = px.pie(
    product_sales,
    names="product",
    values="revenue",
    title=f"Product-wise Sales - {selected_city}",
    hover_data=["revenue"]
)

st.plotly_chart(product_chart, use_container_width=True)

# Order Details
st.subheader("📋 Order Details")
st.dataframe(filtered_df, use_container_width=True)