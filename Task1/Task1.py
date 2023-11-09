import streamlit as st
import pandas

st.set_page_config(layout="wide")

#st.camera_input("Say Cheese")


st.header("The Best Company")

content="""This is the best organization in the coming future for the next generation to work on the best of the best network of the current generation"""

st.write(content)

st.subheader("Our Team")

df = pandas.read_csv("Task1/Task1.csv")

col1, col2, col3 = st.columns(3)

with col1:
    for index, item in df[:4].iterrows():
        st.subheader((item["first name"] + " " + item["last name"]).title())
        st.write(item["role"])
        st.image(f"Task1/images_task1/{item['image']}")

with col2:
    for index, item in df[4:8].iterrows():
        st.subheader((item["first name"] + " " + item["last name"]).title())
        st.write(item["role"])
        st.image(f"Task1/images_task1/{item['image']}")

with col3:
    for index, item in df[8:].iterrows():
        st.subheader((item["first name"] + " " + item["last name"]).title())
        st.write(item["role"])
        st.image(f"Task1/images_task1/{item['image']}")