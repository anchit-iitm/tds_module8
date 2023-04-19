import streamlit as st

def find_largest(val1, val2, val3):
    largest = max(val1, val2, val3)
    return largest

st.title("Find the largest among the 3 given numbers(value greater than the other two).")

value1 = st.number_input("Enter the first number")
value2 = st.number_input("Enter the second number")
value3 = st.number_input("Enter the third number")

if st.button("Find the largest number"):
    largest = find_largest(value1, value2, value3)
    st.write(f"The largest number is {largest}")
