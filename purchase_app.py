import streamlit as st


def calculate_total(price, quantity):
    return price * quantity


st.title("🛒 Purchase Calculator")

price = st.number_input("Price", min_value=0.0)
quantity = st.number_input("Quantity", min_value=1, step=1)

if st.button("Calculate Total"):
    total = calculate_total(price, quantity)
    st.success(f"Total Price: ₹{total:.2f}")