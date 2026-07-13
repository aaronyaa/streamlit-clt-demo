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

# Sidebar interactive UI controls
st.sidebar.header("Simulation Variables")
sample_size = st.sidebar.slider("Sample Size ($n$)", min_value=2, max_value=150, value=30, step=5)
num_simulations = st.sidebar.slider("Number of Simulations", min_value=100, max_value=5000, value=2000, step=100)

np.random.seed(42)
pool_size = 10000

peak_one = np.random.normal(loc=2.0, scale=0.5, size=pool_size // 2)
peak_two = np.random.normal(loc=6.0, scale=0.8, size=pool_size // 2)
underlying_data = np.concatenate([peak_one, peak_two])

samples_peak1 = np.random.normal(loc=2.0, scale=0.5, size=(num_simulations, sample_size))
samples_peak2 = np.random.normal(loc=6.0, scale=0.8, size=(num_simulations, sample_size))

selector = np.random.binomial(1, 0.5, size=(num_simulations, sample_size))
samples = np.where(selector == 1, samples_peak1, samples_peak2)

# Calculate the mean of each simulation group
sample_means = samples.mean(axis=1)

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Original Bimodal Population")
    fig1, ax1 = plt.subplots()
    ax1.hist(underlying_data, bins=50, color="orange", edgecolor="black", alpha=0.7)
    ax1.set_title("Bimodal Mix Pool")
    ax1.set_xlabel("Value")
    ax1.set_ylabel("Count")
    st.pyplot(fig1)
    st.caption("A messy population where data splits into two completely separate clusters.")

with col2:
    st.subheader("2. Distribution of the Sample Means")
    fig2, ax2 = plt.subplots()
    ax2.hist(sample_means, bins=50, color="teal", edgecolor="black", alpha=0.7)
    ax2.set_title(f"Distribution of {num_simulations} Sample Averages (Size $n$={sample_size})")
    ax2.set_xlabel("Sample Mean Value")
    ax2.set_ylabel("Count")
    st.pyplot(fig2)
    st.caption("The central limit law forces the twin peaks to bridge together into a normal bell curve.")
