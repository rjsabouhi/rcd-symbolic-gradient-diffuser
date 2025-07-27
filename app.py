
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Symbolic Gradient Diffuser", layout="wide")
st.title("Symbolic Gradient Diffuser")

st.markdown("""
This tool models how symbolic entropy gradients diffuse across a cognitive field,
illustrating how coherence degrades or stabilizes in relation to symbolic pressure.
""")

# Sidebar parameters
st.sidebar.header("Diffusion Parameters")
gradient_strength = st.sidebar.slider("Initial Entropy Gradient (∇S)", 0.1, 5.0, 2.0)
coherence_tension = st.sidebar.slider("Coherence Tension (γ)", 0.1, 1.0, 0.5)
time_steps = st.sidebar.slider("Time Steps", 10, 100, 50)

# Initial symbolic field
field_size = 100
symbolic_field = np.zeros(field_size)
symbolic_field[field_size // 2] = gradient_strength  # Injected symbolic pressure at center

# Diffusion simulation
history = [symbolic_field.copy()]
for _ in range(time_steps):
    laplacian = np.roll(symbolic_field, 1) + np.roll(symbolic_field, -1) - 2 * symbolic_field
    symbolic_field += coherence_tension * laplacian
    history.append(symbolic_field.copy())

# Plotting results
st.subheader("Symbolic Entropy Diffusion Over Time")
fig, ax = plt.subplots(figsize=(10, 5))
im = ax.imshow(np.array(history), aspect='auto', cmap='viridis')
plt.xlabel("Symbolic Position")
plt.ylabel("Time Step")
st.pyplot(fig)
