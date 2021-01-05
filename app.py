## Importing Packages
import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st
import plotly.io as pio
import plotly.express as px
import bar_chart_race as bcr
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.figure_factory as ff
pio.templates.default = "plotly_dark"
from plotly.subplots import make_subplots

## Importing Data
bcr = pd.read_csv("data/bcr.csv")
Delhi = pd.read_csv("data/Delhi.csv")
df = pd.read_csv("data/df.csv")
eastern_data = pd.read_csv("data/eastern_data.csv")
northern_data = pd.read_csv("data/northern_data.csv")
Sikkim = pd.read_csv("data/Sikkim.csv")
state = pd.read_csv("data/state.csv")

## Opening Images
img_2 = Image.open("assets/img-2.jpg")
img_3 = Image.open("assets/img-3.jpg")

## Page Title
st.title("Delhi vs Sikkim:⚡️Energy Analysis")
st.write("Art Integration Project by [Saurav Maheshkar](https://github.com/SauravMaheshkar) for Grade 12 (2020-21)")
st.markdown("---")
st.image(img_3, use_column_width = True)

## Problem Statement
st.header("Problem Statement")
st.write("""
---
Do comparison of Delhi and Sikkim on the basis of:
* Production and consumption of electricity.
* Renewable sources of energy

Artistic expression has been an integral part of human's growth and development. Over the centuries, as the thrust of education shifted to livelihood, putting the importance of Art in a back seat. Art Integration aims to be a cross-curricular approach to teaching and learning based on collaboration between the teaching of subject with the teaching of Art. This integration is meant not only to make the learning process joyful, but it also lends itself to imbibing a greater appreciation and understanding of the art form being utilized for this purpose.

---
""")

## Datset
st.header("📊 The Data")
st.write("""
We use Two Datasets for this project:

* [Daily Power Generation in India (2017-2020)](https://www.kaggle.com/navinmundhra/daily-power-generation-in-india-20172020)

* [Power consumption in India(2019-2020)](https://www.kaggle.com/twinkle0705/state-wise-power-consumption-in-india)
""")

st.warning("Scroll to the bottom to see the data for yourself")

## Insights
st.header("🥼 Insights")
st.markdown("---")
st.image(img_2, use_column_width = True)
## Comparining Power Consumption
st.subheader("🔌 Power Consumption Comparision")
st.markdown("The following plot shows the Power consumption of the Two states for a period of 17 months beginning from 2nd Jan 2019 till 23rd May 2020.")

fig_0 = go.Figure()
fig_0.add_trace(go.Scatter(
    x=df.Date, y=df.Delhi,
    mode='lines',
    name='Delhi',
    marker=dict(
            color='rgba(300, 50, 50, 0.8)',
            size=5,
            line=dict(
                color='DarkSlateGrey',
                width = 1
                     )
                )
))
fig_0.add_trace(go.Scatter(
    x=df.Date, y=df.Sikkim,
    mode='lines',
    name='Sikkim',
    marker=dict(
            color='rgba(0,0,128, 0.8)',
            size=5,
            line=dict(
                color='DarkSlateGrey',
                width = 1
                     )
                )
))
fig_0.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(step="all")
        ])
    ),
    rangeselector_font_color = "rgba(0,0,0,0.8)"
)
fig_0.update_layout(title='Power Consumption: 🧐 Delhi vs Sikkim (in MU)')
fig_0.update_layout(width=800,height=500)
st.plotly_chart(fig_0, use_container_width = True)
st.markdown("---")

## Video comparison
st.markdown("The following video created using [`bar_chart_race`](https://www.dexplo.org/bar_chart_race/) shows how the Power Consumption varies in the form of a race.")
video = open("assets/power_consumption.mp4", "rb")
video_bytes = video.read()
st.video(video_bytes)
st.markdown("---")

## Production Comparision
st.header("🗼 Delhi vs Sikkim : Maximum Power Usage")
st.markdown("---")
fig_1 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = Delhi['Usage'].max(),
    title = {'text': "Max Power Usage In Delhi (in MU)"},
    gauge = {
        'axis': {'range': [None, 500], 'tickwidth': 1},
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 490}}
))
st.plotly_chart(fig_1, use_container_width = True)
st.markdown("---")
st.info("Delhi uses way more Energy than Sikkim does (around 50x more). Obviously Delhi being the Captial city has way more residents than Sikkim, thus it's huge power consumption")
st.markdown("---")
fig_2= go.Figure(go.Indicator(
    mode = "gauge+number",
    value = Sikkim['Usage'].max(),
    title = {'text': "Max Power Usage In Sikkim (in MU)"},
    gauge = {
        'axis': {'range': [None, 500], 'tickwidth': 1},
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 490}}
))
st.plotly_chart(fig_2, use_container_width = True)

## Power Production Comparision
st.header("📡 Delhi vs Sikkim : Power Production (in Natural Share%)")
st.markdown("---")
st.info("Here, we compare the Power Distribution between Delhi and Sikkim. Interestingly, Sikkim contributes more than Delhi (around 0.15%) to the National Share of Power Generation while it uses way less than Delhi.")
st.markdown("---")
fig_3 = px.bar(state.nlargest(2, "National Share (%)"),
       x = 'National Share (%)',
       y = 'State / Union territory (UT)',
       text="National Share (%)",
      color ='State / Union territory (UT)')
st.plotly_chart(fig_3, use_container_width = True)
st.markdown("---")

## Energy Source Comparision
st.header("🌊 Delhi vs Sikkim: Energy Sources")
st.markdown("Here, we compare between the Expected and Actual values of Thermal, Nuclear and Hydroelectric sources in Northern and Eastern Regions")
def time_series_overall(df1, df2, groupby, dict_features_1, dict_features_2, filter=None):

    temp1 = df1.groupby(groupby).agg(dict_features_1)
    temp2 = df2.groupby(groupby).agg(dict_features_2)
    fig = go.Figure()

    for f,c in zip(dict_features_1, px.colors.qualitative.D3):
        fig.add_traces(go.Scatter(y=temp1[f].values,
                              x=temp1.index,
                              name=f,
                              marker=dict(color=c)
                             ))
    for f,c in zip(dict_features_2, px.colors.qualitative.D3):
        fig.add_traces(go.Scatter(y=temp2[f].values,
                              x=temp2.index,
                              name=f,
                              marker=dict(color=c)
                             ))
    fig.update_traces(marker_line_color='rgb(255,255,255)',
                      marker_line_width=2.5, opacity=0.7)

    fig.update_layout(
                    width=1000,
                    xaxis=dict(title="Date", showgrid=False),
                    yaxis=dict(title="MU", showgrid=False),
                    legend=dict(
                                x=0,
                                y=1.2))

    st.plotly_chart(fig, use_container_width = True)

dict_features_1 = {
    "Thermal Generation Actual (in MU) in Northern Region": "sum"
}

dict_features_2 = {
    "Thermal Generation Actual (in MU) in Eastern Region": "sum"
}
time_series_overall(northern_data,
                    eastern_data,
                    groupby="Date",
                    dict_features_1 = dict_features_1,
                    dict_features_2 = dict_features_2)

dict_features_1 = {
    "Thermal Generation Estimated (in MU) in Northern Region": "sum"
}

dict_features_2 = {
    "Thermal Generation Estimated (in MU) in Eastern Region": "sum"
}

time_series_overall(northern_data,
                    eastern_data,
                    groupby="Date",
                    dict_features_1 = dict_features_1,
                    dict_features_2 = dict_features_2)

dict_features_1 = {
    "Nuclear Generation Actual (in MU) in Northern Region": "sum"
}

dict_features_2 = {
    "Nuclear Generation Actual (in MU) in Eastern Region": "sum"
}

time_series_overall(northern_data,
                    eastern_data,
                    groupby="Date",
                    dict_features_1 = dict_features_1,
                    dict_features_2 = dict_features_2)

dict_features_1 = {
    "Nuclear Generation Estimated (in MU) in Northern Region": "sum"
}

dict_features_2 = {
    "Nuclear Generation Estimated (in MU) in Eastern Region": "sum"
}

time_series_overall(northern_data,
                    eastern_data,
                    groupby="Date",
                    dict_features_1 = dict_features_1,
                    dict_features_2 = dict_features_2)

dict_features_1 = {
    "Hydro Generation Actual (in MU) in Northern Region": "sum"
}

dict_features_2 = {
    "Hydro Generation Actual (in MU) in Eastern Region": "sum"
}
time_series_overall(northern_data,
                    eastern_data,
                    groupby="Date",
                    dict_features_1 = dict_features_1,
                    dict_features_2 = dict_features_2)

dict_features_1 = {
    "Hydro Generation Estimated (in MU) in Northern Region": "sum"
}

dict_features_2 = {
    "Hydro Generation Estimated (in MU) in Eastern Region": "sum"
}
time_series_overall(northern_data,
                    eastern_data,
                    groupby="Date",
                    dict_features_1 = dict_features_1,
                    dict_features_2 = dict_features_2)

st.header("Data used")
st.markdown("---")
st.subheader("Northern India's Energy Generation")
st.dataframe(northern_data)
st.subheader("Eastern India's Energy Generation")
st.dataframe(eastern_data)
st.subheader("Delhi's Power Consumption")
st.dataframe(Delhi)
st.subheader("Sikkim's Power Consumption")
st.dataframe(Sikkim)
st.markdown("---")

st.markdown("Follow me on [Github](https://github.com/SauravMaheshkar), and show some ❤️ by starring some of my repositories")
