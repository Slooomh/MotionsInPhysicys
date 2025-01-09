import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def simulate_projectile(initial_velocity, angle_deg, wind_acc, time_step=0.01):
    g = 9.81  # Gravity (m/s^2)
    angle_rad = np.radians(angle_deg)
    vx = initial_velocity * np.cos(angle_rad)
    vy = initial_velocity * np.sin(angle_rad)
    x, y = 0, 0
    x_positions, y_positions = [x], [y]
    max_height = 0

    while y >= 0:
        vy -= g * time_step
        vx += wind_acc * time_step
        x += vx * time_step
        y += vy * time_step
        max_height = max(max_height, y)
        x_positions.append(x)
        y_positions.append(y)

    range_projectile = x_positions[-1]
    return x_positions, y_positions, max_height, range_projectile

st.title("Projectile Motion Simulator")
st.sidebar.header("Inputs")
initial_velocity = st.sidebar.slider("Initial Velocity (m/s)", 1, 100, 20)
angle_deg = st.sidebar.slider("Launch Angle (°)", 0, 90, 45)
wind_acc = st.sidebar.slider("Wind Acceleration (m/s²)", -5.0, 5.0, 0.0)

x_positions, y_positions, max_height, range_projectile = simulate_projectile(
    initial_velocity, angle_deg, wind_acc
)

st.write(f"**Maximum Height**: {max_height:.2f} m")
st.write(f"**Range**: {range_projectile:.2f} m")

fig, ax = plt.subplots()
ax.plot(x_positions, y_positions)
ax.set_title("Projectile Trajectory")
ax.set_xlabel("Horizontal Distance (m)")
ax.set_ylabel("Vertical Distance (m)")
st.pyplot(fig)
