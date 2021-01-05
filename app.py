import numpy as np
import pandas as pd
import streamlit as st
import plotly.io as pio
import plotly.express as px
import bar_chart_race as bcr
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.figure_factory as ff
pio.templates.default = "plotly_dark"
from plotly.subplots import make_subplots

bcr = pd.read_csv("data/bcr.csv")
Delhi = pd.read_csv("data/Delhi.csv")
df = pd.read_csv("data/df.csv")
eastern_data = pd.read_csv("data/eastern_data.csv")
northern_data = pd.read_csv("data/northern_data.csv")
Sikkim = pd.read_csv("data/Sikkim.csv")
state = pd.read_csv("data/state.csv")

st.title("Delhi vs Sikkim:⚡️Energy Analysis")
st.write("Art Integration Project by [Saurav Maheshkar](https://github.com/SauravMaheshkar) for Grade 12 (2020-21)")
st.markdown("---")
