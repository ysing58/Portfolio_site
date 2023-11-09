import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=450)

with col2:
    st.title("Yadvendra singh")
    content = """
    As an experienced engineer with a focus on Hive, SQL, Unix scripting, and Python, I am passionate about leveraging data to drive meaningful insights and solve complex problems. With nearly 2 years of hands-on experience in the field, I have developed a strong technical skill set and a deep understanding of data processing, analysis, and visualization.

In my previous roles, I have successfully designed, developed, and optimized Hive queries to extract, unix scripting language to transform, and load large datasets for various business use cases. My expertise in Unix scripting has allowed me to automate data processing tasks and streamline workflows, improving efficiency and accuracy.
    """
    st.info(content)

content1 = """Below you can find some of the apps i have built in python. Feel free to contact me!! be the best or be the last"""

st.write(content1)

col3, blank_column,  col4 = st.columns([1.5, .1, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.link_button("Source code", url=row["url"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.link_button("Source code", url=row["url"])