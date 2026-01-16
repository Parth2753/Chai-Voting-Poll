import streamlit as st

st.title("Chai Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image(
        "https://masalaandchai.com/wp-content/uploads/2021/07/Masala-Chai-Featured.jpg",
        width=200
    )
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image(
        "https://www.teacupsfull.com/cdn/shop/articles/Screenshot_2023-09-05_at_7.00.35_PM.png",
        width=200
    )
    vote2 = st.button("Vote Adrak Chai")

if vote1:
    st.success("Thanks for voting Masala Chai")
elif vote2:
    st.success("Thanks for voting Adrak Chai")

st.sidebar.title("User Info")
name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose your chai:", ["Masala Chai", "Adrak Chai"])

st.write(f"Welcome {name}! Your {tea} is being brewed ☕")
