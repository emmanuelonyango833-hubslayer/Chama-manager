import streamlit as st
import pandas as pd

# --- APP ICON AND NAME ---
st.set_page_config(page_title="Chama Manager", page_icon="💰", layout="wide")

st.title("💰 Chama Manager")
st.subheader(" Chamas | Members & Contributions")

# --- SIDEBAR ---
st.sidebar.header("Add New Member")
new_member = st.sidebar.text_input("Member Name")
phone = st.sidebar.text_input("Phone Number")
if st.sidebar.button("Add Member"):
    if new_member:
        st.sidebar.success(f"{new_member} Added!")
    else:
        st.sidebar.error("Enter name")

# --- MAIN DATA ---
# Sample data - you can connect to Google Sheets later
data = {
    "Member": ["John Kamau", "Mary Wanjiku", "Peter Ochieng"],
    "Phone": ["0712xxxxxx", "0723xxxxxx", "0745xxxxxx"],
    "Contribution": [2000, 2000, 1500],
    "Status": ["Paid", "Paid", "Pending"]
}
df = pd.DataFrame(data)

# --- DISPLAY ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Members", len(df))
col2.metric("Total Collected", f"KES {df['Contribution'].sum()}")
col3.metric("Pending", len(df[df['Status']=="Pending"]))

st.divider()

st.dataframe(df, use_container_width=True)

st.divider()
st.write("📱 **How to use:** Add members on the left, mark contributions, and share this link with your chama chairman.")

st.success("Live Link: Share this app with your customers!")
