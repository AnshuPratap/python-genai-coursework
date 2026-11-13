# TASK 3 : Product form
# Create a simple form UI:
# 1. Use Streamlit sidebar to enter:
# -> Product Name
# -> Category(selectbox with 3-5 options)
# -> Price
# 2. When user clicks "Add Product", show:
# -> A success message
# -> The product details in a clean format
# Use components:
# st.sidebar.text_input
# st.sidebar.selectbox
# st.sidebar.number_input
# st.sidebar.button

import streamlit as st
product_name = st.sidebar.text_input("Enter Product Name:")
category = st.sidebar.selectbox("Category:",("Electronics", "Home", "Clothing", "Furniture", "Groceries"))
price = st.sidebar.number_input("Enter Price:")
if st.sidebar.button("Add Product"):
    st.success("Product Added Successfully!")
    product_data = {"Field": ["Product Name", "Category", "Price"], "Value": [product_name, category, f"${price:.2f}"]}
    st.table(product_data)