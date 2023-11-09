import streamlit as st
import send_email as sm
import pandas


st.header("Contact Us")

df = pandas.read_csv("topics.csv", sep=",")

with st.form(key="form"):

    user_email = st.text_input("Your Email Address")
    inquiry = st.selectbox('What topic do you want to discuss',(df["topic"]))
    raw_message = st.text_area("Your Message")
    message = f"""\
Subject: Email from {user_email}

From: {user_email}
Reason: {inquiry}
{raw_message}
"""
    print(message)
    button = st.form_submit_button()
    if button:
        sm.Send_mail(message)
        st.info("Your Email was sent successfully")