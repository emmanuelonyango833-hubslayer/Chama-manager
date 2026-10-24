import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Chama Manager", page_icon="💰", layout="wide")

st.title("💰 Chama Manager")
st.markdown("**Ruiru | Kahawa | Githurai - Chama & Church Contributions**")

tab1, tab2 = st.tabs(["📋 Members", "💵 M-Pesa"])

with tab1:
    st.header("Members")
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
    st.success("Add M-Pesa code in next tab!")

with tab2:
    st.header("M-Pesa Tracker")
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
