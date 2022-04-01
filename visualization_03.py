import streamlit as st
import numpy as np
import pandas as pd

data = pd.DataFrame(np.random.randn(100, 4), columns = ['a', 'b', 'c', 'd'])

#we can change width, height for all charts 
st.line_chart(data)
st.bar_chart(data)
st.area_chart(data)

import matplotlib.pyplot as plt
plt.scatter(data['a'], data['b'])
st.pyplot()
plt.title("scatter plot")
plt.xlabel("A values")
plt.ylabel("B Values")

# crating flow chart

st.graphviz_chart(""" digraph {
                    watch -> like
                    like -> share
                    share -> subscribe
                    share -> watch
}""")


st.map()

demo_map_df = pd.DataFrame({    
    "Cities": ['Pune', 'Delhi', 'Mumbai'], 
    "lat": [18.5204, 28.7041, 19.0760, ],
    "lon": [73.8567, 77.1025, 72.8777, ]
}
)

st.map(demo_map_df)