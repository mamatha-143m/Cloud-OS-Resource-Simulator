import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from allocator import allocate_resources

# Page config
st.set_page_config(page_title="Cloud OS Simulator", layout="wide")

# Title
st.markdown("<h1 style='text-align: center;'>☁️ Cloud OS Resource Allocation Dashboard</h1>", unsafe_allow_html=True)

st.markdown("---")

# Sidebar inputs
st.sidebar.header("⚙️ System Configuration")

total_cpu = st.sidebar.slider("Total CPU", 1, 32, 8)
total_ram = st.sidebar.slider("Total RAM (GB)", 1, 64, 16)

num_users = st.sidebar.slider("Number of Users", 1, 10, 3)

st.sidebar.markdown("---")

# User inputs
st.subheader("👥 User Requests")

users = []

cols = st.columns(3)

for i in range(num_users):
    with cols[i % 3]:
        st.markdown(f"### User {i+1}")
        cpu = st.number_input(f"CPU", min_value=1, value=1, key=f"cpu{i}")
        ram = st.number_input(f"RAM", min_value=1, value=2, key=f"ram{i}")
        priority = st.selectbox(f"Priority", [1,2,3], key=f"priority{i}")
        
        users.append({
            "id": i+1,
            "cpu": cpu,
            "ram": ram,
            "priority": priority
        })

st.markdown("---")

# Allocation button
if st.button("🚀 Allocate Resources"):

    allocated, waiting, rem_cpu, rem_ram = allocate_resources(users, total_cpu, total_ram)

    # Convert to DataFrame
    df_alloc = pd.DataFrame(allocated)
    df_wait = pd.DataFrame(waiting)

    col1, col2 = st.columns(2)

    with col1:
        st.success("✅ Allocated Users")
        st.dataframe(df_alloc)

    with col2:
        st.warning("⏳ Waiting Users")
        st.dataframe(df_wait)

    st.markdown("---")

    # Metrics
    cpu_used = total_cpu - rem_cpu
    ram_used = total_ram - rem_ram

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total CPU", total_cpu)
    m2.metric("Used CPU", cpu_used)
    m3.metric("Total RAM", total_ram)
    m4.metric("Used RAM", ram_used)

    st.markdown("---")

    # Graphs
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("📊 CPU Usage")
        fig1, ax1 = plt.subplots()
        ax1.pie([cpu_used, rem_cpu], labels=["Used", "Free"], autopct="%1.1f%%")
        st.pyplot(fig1)

    with col4:
        st.subheader("📊 RAM Usage")
        fig2, ax2 = plt.subplots()
        ax2.pie([ram_used, rem_ram], labels=["Used", "Free"], autopct="%1.1f%%")
        st.pyplot(fig2)