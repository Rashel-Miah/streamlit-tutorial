"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st 
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

df
st.table(df) # draw as a static table

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]    
}))

# let's create a data frame and change its formatting with a Pandas Styler object. In this example, you'll use Numpy to generate a random sample, and the st.dataframe() method to draw an interactive table.
dataframe = np.random.randn(10,20)
st.dataframe(dataframe)

# Let's expand on the first example using the Pandas Styler object to highlight some elements in the interactive table.
dataframe = pd.DataFrame(
    np.random.randn(10,20),
    columns=('col %d' % i for i in range(20))
)

st.dataframe(dataframe.style.highlight_max(axis=0))

# Draw a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)

st.line_chart(chart_data)

# Plot a map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

## Widgets
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
"""
For example, if the user moves the slider to position 10, Streamlit will rerun the code above and set x to 10 accordingly. So now you should see the text "10 squared is 100".
Widgets can also be accessed by key, if you choose to specify a string to use as the unique key for the widget:
"""
st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name # Every widget with a key is automatically added to Session State.

# Use checkboxes to show/hide data
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

# Use a selectbox for options

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

# # Layout
"""
Streamlit makes it easy to organize your widgets in a left panel sidebar with st.sidebar. Each element that's passed to st.sidebar is pinned to the left, allowing users to focus on the content in your app while still having access to UI controls.

For example, if you want to add a selectbox and a slider to a sidebar, use st.sidebar.slider and st.sidebar.selectbox instead of st.slider and st.selectbox:
"""

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

"""
Beyond the sidebar, Streamlit offers several other ways to control the layout of your app. st.columns lets you place widgets side-by-side, and st.expander lets you conserve space by hiding away large content.
"""
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

# Show progress
"""
When adding long running computations to an app, you can use st.progress() to display status in real time.

First, let's import time. We're going to use the time.sleep() method to simulate a long running computation:
"""    
import time
# Now, let's create a progress bar:

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

## Examples of using Session State
if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")

"""
If you have random number generation in your app, you'd likely use Session State. Here's an example where data is generated randomly 
at the beginning of each session. By saving this random information in Session State, 
each user gets different random data when they open the app but it won't keep changing on them as they interact with it. 
If you select different colors with the picker you'll see that the data does not get re-randomized with each rerun. 
(If you open the app in a new tab to start a new session, you'll see different data!)
"""

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)

# Connections
conn = st.connection("my_database")
df = conn.query("select * from my_table")
st.dataframe(df)
