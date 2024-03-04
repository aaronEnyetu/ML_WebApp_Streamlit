import streamlit as st


st.title("Machine Learning App")


st.write("""
         # Explore different classifier
         Which one is the best
         """)

dataset_name = st.sidebar.selectbox("Select Dataset", ("Iris", "Breast Cancer", "Wine dataset"))
st.write(dataset_name)