import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Bimodal CLT Demo", layout="wide")

st.title("The Central Limit Theorem on Two Distinct Groups")
st.write(
    "This application proves that even if an underlying population "
    "is highly divided and splits into two distinct peaks (bimodal), the averages of random "
    "samples drawn from it will still converge into a clean, symmetrical normal curve."
)

