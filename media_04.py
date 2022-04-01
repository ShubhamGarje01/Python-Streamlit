import streamlit as st
st.title(' Widgets')
var = st.button("Subscribe")

if var:
    st.write("Like The Video Brooooh.")

#rext input from user

var_name = st.text_input("Enter Your Name Plase brooh ;)")
st.write(var_name)

var_address = st.text_area("Enter Your Addresss")
st.write(var_address)


st.date_input("Enter Date")

st.time_input("Enter time")

var_tc = st.checkbox("Do you accept the T&C ?", value = False)
if var_tc:
    st.write("Thank You Bruh")

st.radio("color", ["r", "b", "g"], index = 2)
st.selectbox("color", ["r", "b", "g"], index = 1)

st.multiselect("color", ["r", "b", "g"])

st.number_input("number", step = 0.05)






#