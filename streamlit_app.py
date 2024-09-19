import streamlit as st
import numpy as np
import pandas as pd
import time
from io import StringIO

_COMPARE = """
The result of the technical comparison of the uploaded file with current 
ThermoFisher Scientific IP documents shows no inflictions so far.
"""

# begin: main page setup
st.set_page_config(layout="wide")
st.title("Gene.AI IP Checker")

col1, col2 = st.columns([1, 2])
# end: main page setup

# begin: left sidebar
with open("sidebar.md") as sidebar_file:
    sidebar_content = sidebar_file.read()
st.sidebar.image("Challenge-picture2.png", width=250)
st.sidebar.markdown(sidebar_content)

with col1:
    st.header("IP to Compare")
    st.divider()
    text="""Scanned/Converted PDFs of images, presentations, or spreadsheets are unsupported."""
    st.markdown(text)
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        #st.write(bytes_data)

        # To convert to a string based IO:
        #stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        #st.write(stringio)

        # To read file as string:
        #string_data = stringio.read()
        #st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        #dataframe = pd.read_csv(uploaded_file)
        #st.write(dataframe)

with col2:
    st.header("Result Output")
    st.divider()

    def stream_data():
       for word in _COMPARE.split(" "):
           yield word + " "
           time.sleep(0.1)
    if st.button("Compare", type="primary"):
        st.write_stream(stream_data)























st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
