import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Chama Manager", page_icon="💰", layout="wide")

# --- SIDEBAR - MONEY SECTION ---
try:
    st.sidebar.image("logo.png", width=150)
except:
    st.sidebar.title("💰 Chama Manager")

st.sidebar.divider()
st.sidebar.header("💵 Lipa Na M-Pesa")
st.sidebar.write("**Till / Number:**")
st.sidebar.code("0142929374", language="text")
st.sidebar.write("**Setup Fee: KES 3,000**")
st.sidebar.write("Pay to activate your Chama")
st.sidebar.divider()
st.sidebar.write("📞 Need Help? WhatsApp: 0142929374")
st.sidebar.write("📍 Ruiru | Kahawa | Githurai")

# --- MAIN APP ---
st.title("💰 Chama Manager")
st.markdown("**Ruiru's #1 Chama & Church Contribution System**")
st.success("✅ Free Demo - Pay KES 3,000 to get your own Chama setup!")

tab1, tab2, tab3 = st.tabs(["📋 Members Demo", "💵 M-Pesa Payments", "🔑 Activate Your Chama"])

with tab1:
    st.header("Demo - Members List")
    data = {
        "Member": ["John Kamau", "Mary Wanjiku", "Peter Ochieng"],
        "Phone": ["0712xxxxxx", "0723xxxxxx", "0745xxxxxx"],
        "Contribution": [2000, 2000, 1500],
        "Status": ["Paid", "Paid", "Pending"]
    }
    df = pd.DataFrame(data)
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Members", len(df))
    c2.metric("Collected", f"KES {df['Contribution'].sum()}")
    c3.metric("Pending", 1)
    st.dataframe(df, use_container_width=True)
    st.info("This is DEMO data. Your real chama members will appear after you pay KES 3,000 setup.")

with tab2:
    st.header("💵 M-Pesa Tracker")
    code = st.text_input("M-Pesa Code (e.g. QGH7... )")
    amount = st.number_input("Amount", value=2000)
    name = st.selectbox("Member", ["John Kamau", "Mary Wanjiku", "Peter Ochieng"])
    if st.button("Confirm Payment"):
        if code:
            st.success(f"✅ {name} paid KES {amount} - Code: {code}")
            st.balloons()
        else:
            st.error("Enter M-Pesa code")
    st.write(f"Date: {datetime.now().strftime('%d-%m-%Y')}")

with tab3:
    st.header("🔑 Get Your Own Chama System - KES 3,000")
    st.write("Fill this after paying to 0142929374")
    
    mpesa_code = st.text_input("Your M-Pesa Payment Code (from 0142929374 payment)")
    chama_name = st.text_input("Your Chama Name")
    num_members = st.number_input("How many members?", min_value=1, value=10)
    whatsapp = st.text_input("Your WhatsApp Number")
    
    if st.button("Submit - Activate My Chama"):
        if mpesa_code and chama_name and whatsapp:
            st.success(f"✅ Payment received! Code: {mpesa_code}")
            st.success(f"We are setting up '{chama_name}' for {num_members} members. We will WhatsApp you at {whatsapp} in 30 mins!")
            st.balloons()
            st.write("---")
            st.write("**Admin will contact you soon. Keep your M-Pesa message ready.**")
        else:
            st.error("Fill all fields: M-Pesa code, Chama name, WhatsApp")

    st.divider()
    st.markdown("""
    ### What you get for KES 3,000:
    - ✅ Your own Chama Link (e.g. chama-manager-yourname)
    - ✅ All members added
    - ✅ M-Pesa automatic tracking
    - ✅ Monthly PDF reports
    - ✅ Free support
    """)v
