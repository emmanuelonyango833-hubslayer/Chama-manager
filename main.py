import streamlit as st
from datetime import date

st.set_page_config(page_title="Chama Manager PRO")
st.title("💰 Chama Manager PRO")
st.caption("Ruiru - Members + Money + Attendance")

if "members" not in st.session_state:
    st.session_state.members = []
    st.session_state.contrib = []
    st.session_state.attendance = {}

st.subheader("1. Add Member")
name = st.text_input("Member name")
if st.button("Add Member"):
    if name and name not in st.session_state.members:
        st.session_state.members.append(name)
        st.success(f"Added {name}")

if st.session_state.members:
    st.divider()
    st.subheader(f"2. Attendance - {date.today()}")
    for m in st.session_state.members:
        st.checkbox(f"{m}", key=f"att_{m}")
    
    st.divider()
    st.subheader("3. Record Payment")
    who = st.selectbox("Who paid?", st.session_state.members)
    amt = st.number_input("Amount KES", min_value=0, step=100)
    if st.button("Record Payment", type="primary", use_container_width=True):
        st.session_state.contrib.append({"member": who, "amount": amt})
        st.success(f"Recorded KES {amt}")

if st.session_state.contrib:
    st.divider()
    st.subheader("Report")
    total = sum(c["amount"] for c in st.session_state.contrib)
    st.metric("TOTAL", f"KES {total:,}")
    for m in st.session_state.members:
        paid = sum(c["amount"] for c in st.session_state.contrib if c["member"] == m)
        present = "✅" if st.session_state.get(f"att_{m}") else "❌"
        st.write(f"{present} {m} - KES {paid}")
