import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10,20),
    columns=('col %d' % i for i in range(20))
)

st.dataframe(dataframe.style.highlight_max(axis=0))

st.divider()
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)

st.line_chart(chart_data)
st.divider()

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
st.divider()
x = st.slider('Slider')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.text_input("Your Name", key="name")

st.session_state.name