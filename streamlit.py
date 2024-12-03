import streamlit as st
import numpy as np
from numba import jit
import time

# Streamlit App Title
st.title("Streamlit App with NumPy and Numba")

# App description
st.write("""
This app demonstrates the use of **NumPy** and **Numba** together for numerical computations.
We compare the performance of a NumPy-based computation and a Numba-optimized equivalent.
""")

# Create a slider to let the user define the array size
array_size = st.slider("Select Array Size", min_value=1000, max_value=10_000_000, step=1000, value=1_000_000)

# Generate a random NumPy array
array = np.random.rand(array_size)

# Define a NumPy function to compute the sum of squares
def sum_of_squares_numpy(arr):
    return np.sum(arr ** 2)

# Define a Numba-optimized function to compute the sum of squares
@jit(nopython=True)
def sum_of_squares_numba(arr):
    total = 0.0
    for x in arr:
        total += x ** 2
    return total

# Benchmark NumPy function
start_time = time.time()
result_numpy = sum_of_squares_numpy(array)
numpy_time = time.time() - start_time

# Benchmark Numba-optimized function
start_time = time.time()
result_numba = sum_of_squares_numba(array)
numba_time = time.time() - start_time

# Display Results
st.subheader("Results:")
st.write(f"Sum of Squares (NumPy): {result_numpy:.6f}")
st.write(f"Sum of Squares (Numba): {result_numba:.6f}")

# Display Performance Metrics
st.subheader("Performance:")
st.write(f"Execution Time (NumPy): {numpy_time:.6f} seconds")
st.write(f"Execution Time (Numba): {numba_time:.6f} seconds")

# Highlight the performance improvement
if numba_time > 0:
    improvement = numpy_time / numba_time
    st.write(f"Performance Improvement with Numba: {improvement:.2f}x")
else:
    st.write("Performance Improvement: Unable to calculate due to very low execution time.")
