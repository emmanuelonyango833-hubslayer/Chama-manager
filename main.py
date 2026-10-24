import streamlit as st
import pandas as pd
from datetime import datetime

# --- ICON & LOGO SETUP ---
st.set_page_config(page_title="Chama Manager", page_icon="💰", layout="wide")

try:
    st.sidebar.image("logo.png", width=150)
except:
    st.sidebar.title("💰 Chama Manager")

st.title("💰 Chama Manager")
st.markdown("Ruiru | Kahawa | Githurai - Chama System")

# --- TABS ---
tab1, tab2 = st.tabs(["📋 Members", "💵 M-Pesa Payments"])

with tab1:
    st.header("Members List")
    data = {
        "Member": ["John Kamau", "Mary Wanjiku", "Peter Ochieng"],
        "Phone": ["0712xxxxxx", "0723xxxxxx", "0745xxxxxx"],
        "Contribution": [2000, 2000, 1500],
        "Status": ["Paid", "Paid", "Pending"]
    }
    df = pd.DataFrame(data)
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Members", len(df))
    col2.metric("Total Collected", f"KES {df['Contribution'].sum()}")
    col3.metric("Pending", len(df[df['Status']=="Pending"]))
    st.dataframe(df, use_container_width=True)

with tab2:
    st.header("💵 M-Pesa Payment Tracker")
    st.info("Members enter M-Pesa code after paying")
    mpesa_code = st.text_input("Enter M-Pesa Code (e.g. QGH7... )")
    amount = st.number_input("Amount Paid", min_value=0, value=2000)
    member_name = st.selectbox("Select Member", ["John Kamau", "Mary Wanjiku", "Peter Ochieng"])
    if st.button("Confirm Payment"):
        if mpesa_code:
            st.success(f"✅ Payment KES {amount} from {member_name} confirmed! Code: {mpesa_code}")
            st.balloons()
        else:
            st.error("Enter M-Pesa code")
    st.write(f"**Paybill/Till:** Your M-Pesa Till - 07XX XXX XXX")
    st.write(f"**Last updated:** {datetime.now().strftime('%d-%m-%Y %H:%M')}")
