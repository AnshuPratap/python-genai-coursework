# Task 4 : Mini Dashboard
# Create a small dashboard with:
# 1. Title + Description
# "Simple Sales Dashboard"
# 2. A selctbox with months:
# months = ["January", "February", "March", "April"]
# 3. A static dictionary of monthly sales:
# sales = {
#     "January": 1200,
#     "February": 1500,
#     "March": 900,
#     "April": 2000
# }
# 4. Display selected month's sales using:
# st.metric() OR st.write()
# 5. Display a bar chart using:
# st.bar_chart(list(sales.values()))

import streamlit as st
st.title("Simple Sales Dashboard")
st.text("A Sales Dashboard gives a quick overview of business performance, including total revenue, units sold, top-selling products, and sales trends over time. Use filters to explore results by date, product, or category.")

sales = {"January":1200, "February":1500, "March":900, "April":2000}

month = st.selectbox("Choose Month:",("January", "February", "March", "April"))
st.metric(label = f"{month} Sales", value = f"{sales[month]}")

st.bar_chart({"Month" : list(sales.keys()),"Sales" : list(sales.values())},x = "Month",y = "Sales")