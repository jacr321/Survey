import streamlit as st

def main():
    st.title("Survey Form")

    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:")

    food_options = ['Pizza', 'Hamburger', 'Ice Cream', 'Tacos']
    food = st.selectbox("Select your food preference:", food_options)

    if st.button("Submit"):
        st.write("Name: ", name)
        st.write("Age: ", age)
        st.write("Food Preference: ", food)

if __name__ == '__main__':
    main()
