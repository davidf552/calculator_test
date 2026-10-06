import streamlit as st

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

st.title("Welcome to the Wonder Calculator!")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

st.write("Numbers entered are:", num1, "and", num2)


st.write("Select operation:")
st.write("1. Addition")
st.write("2. Subtraction")
st.write("3. Multiplication")
st.write("4. Division")

operation = st.selectbox(
    "Choose an operation",
    (1, 2, 3, 4)
) 

if operation == 1:
    result = add(num1, num2)
    st.write("The result of addition is:", result)

elif operation == 2:
    result = subtract(num1, num2)
    st.write("The result of subtraction is:", result)

elif operation == 3:
    result = multiply(num1, num2)
    st.write("The result of multiplication is:", result)

elif operation == 4:
    result = divide(num1, num2)
    st.write("The result of division is:", result)