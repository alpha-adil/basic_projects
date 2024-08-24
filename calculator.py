import streamlit as st

st.title("Simple Calculator")

operation = ['+', '-', 'x', '/']
# Create a dropdown select box
selected_option = st.selectbox('Choose an option:', operation)

num_1 = st.number_input('Enter num1')
num_2 = st.number_input('Enter num2')

if selected_option == '+':
    sol = num_1 + num_2
    st.write(sol)

elif selected_option == '-':
    sol = num_1 - num_2
    st.write(sol)

elif selected_option == 'x':
    sol = num_1 * num_2
    st.write(sol)

else:
    #note
    if num_2 != 0:
        sol = num_1 / num_2
        st.write(sol)
    else:
        st.write("Error: Division by zero is not allowed")