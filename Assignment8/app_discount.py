# Task2: Price Calculator
# Build a simple price calculator app that;
# 1. Takes product_price (number input)
# 2. Takes discont percentage ( slider from 0 to 50 %)
# 3. On button click, claculates discounted price
# 4. shows a result using st.success()
# Example:
# Original Price : 1000
# Discount : 10%
# Final Price : 900
# Extra : Show comparison in a small table:
# Before| After
# (Use st.table() with a simple list of lists.)

import streamlit as st
price = st.number_input("Enter the Product Price:")
discount_percentage = st.slider("Select Discount Percentage:", 0, 50)
if st.button("Show Price"):
    st.write(f"Original Price : {price}")
    st.write(f"Discount : {discount_percentage}%")
    st.write(f"Final Price : {price - price *(discount_percentage/100)}")


    price_data = [["Before", price],["After", price - price *(discount_percentage/100)]]
    st.table(price_data)