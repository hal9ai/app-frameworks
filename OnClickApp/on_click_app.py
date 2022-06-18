from turtle import onclick
import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_plotly_events import plotly_events


data = pd.read_csv('https://prodhal9.s3.us-west-2.amazonaws.com/users/7be30db96302d198035cec0d76c8ce7a_46079/file_example_XLSX_100.csv')

summary = data.groupby('Country').count().reset_index()
# st.write(summary)

fig = px.bar(summary, x = 'Country', y='First Name')
# st.plotly_chart(fig)
country = plotly_events(fig)

if len(country) > 0:
    st.dataframe(data[data['Country'] == country[0]['x']])
