import streamlit as st
import pandas as pd
from allocator import allocate_resources
import matplotlib.pyplot as plt

st.title("☁️ Cloud OS Resource Allocation Simulator")

# Input total resources
total_cpu = st.number_input("Total CPU", value=8)
total_ram = st.number_input("Total RAM", value=16)

st.subheader("Enter User Requests")

num_users = st.number_input("Number of Users", min_value=1, max_value=10, value=3)

users = []

for i in range(num_users):
    cpu = st.number_input(f"User {i+1} CPU", value=1, key=f"cpu{i}")
    ram = st.number_input(f"User {i+1} RAM", value=2, key=f"ram{i}")
    
    users.append({"id": i+1, "cpu": cpu, "ram": ram})

if st.button("Allocate Resources"):
    allocated, waiting, rem_cpu, rem_ram = allocate_resources(users, total_cpu, total_ram)

    st.success("Allocation Complete!")

    st.write("### ✅ Allocated Users")
    st.write(allocated)

    st.write("### ⏳ Waiting Users")
    st.write(waiting)

    st.write(f"Remaining CPU: {rem_cpu}")
    st.write(f"Remaining RAM: {rem_ram}")
cpu_used = total_cpu - rem_cpu

st.subheader("📊 CPU Usage")

fig1, ax1 = plt.subplots()
ax1.pie([cpu_used, rem_cpu], labels=["Used", "Free"], autopct="%1.1f%%")
st.pyplot(fig1)

ram_used = total_ram - rem_ram

st.subheader("📊 RAM Usage")

fig2, ax2 = plt.subplots()
ax2.pie([ram_used, rem_ram], labels=["Used", "Free"], autopct="%1.1f%%")
st.pyplot(fig2)

    