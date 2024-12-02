import streamlit as st
import numpy as np
from numba import jit
import time

# Streamlit App Title
st.title("Streamlit App with Numba")

# Introduction
st.write("""
This app demonstrates the use of the `Numba` package for just-in-time (JIT) 
compilation in Python. Numba accelerates numerical computations by compiling Python functions 
to machine code at runtime.
""")

# Define a regular Python function
def compute_sum_regular(array):
    total = 0
    for i in array:
        total += i
    return total

# Define a JIT-optimized function using Numba
@jit(nopython=True)
def compute_sum_numba(array):
    total = 0
    for i in array:
        total += i
    return total

# Create a large random array
array_size = st.slider("Select Array Size", min_value=1000, max_value=10_000_000, step=1000, value=1_000_000)
array = np.random.rand(array_size)

# Run the regular Python function
start_time = time.time()
regular_result = compute_sum_regular(array)
regular_time = time.time() - start_time

# Run the Numba-optimized function
start_time = time.time()
numba_result = compute_sum_numba(array)
numba_time = time.time() - start_time

# Display Results
st.subheader("Results:")
st.write(f"Sum (Regular Python): {regular_result}")
st.write(f"Sum (Numba-Optimized): {numba_result}")

st.subheader("Performance:")
st.write(f"Execution Time (Regular Python): {regular_time:.6f} seconds")
st.write(f"Execution Time (Numba-Optimized): {numba_time:.6f} seconds")

# Highlight performance improvement
improvement = regular_time / numba_time if numba_time > 0 else 0
st.write(f"Performance Improvement: {improvement:.2f}x")
