import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("3. Charts Demo")
st.header("Line, area, and bar charts")

# Fake time series data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

# Line chart
st.subheader("Line chart")
st.line_chart(data)

# Area chart
st.subheader("Area chart")
st.area_chart(data)

# Bar chart
st.subheader("Bar chart")
st.bar_chart(data)

st.divider()

# Scatter chart
st.header("Scatter chart & map")
scatter_data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=["x", "y", "size"]
)
st.subheader("Scatter chart")
scatter_chart = alt.Chart(scatter_data).mark_circle().encode(
    x="x",
    y="y",
    size="size",
    tooltip=["x", "y", "size"]
)
st.altair_chart(scatter_chart, use_container_width=True)

# Map (requires latitude and longitude columns)
st.subheader("Map")
map_data = pd.DataFrame({
    "lat": 51.5 + np.random.randn(100) * 0.01,
    "lon": -0.12 + np.random.randn(100) * 0.01,
})
st.map(map_data)

# Altair example
st.header("Altair example")
chart = (
    alt.Chart(data.reset_index())
    .mark_line()
    .encode(
        x="index",
        y="A",
    )
)
st.altair_chart(chart, use_container_width=True)
