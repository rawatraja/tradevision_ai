import streamlit as st

st.set_page_config(
    page_title="TradeVision AI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📈 TradeVision AI")

st.markdown("""
## Professional Options Analysis Platform

Welcome to **TradeVision AI**.

Use the navigation menu on the left to explore the application.
""")

st.info("Project Status: Milestone 1 - Dashboard UI")

col1, col2, col3 = st.columns(3)

col1.metric("Market", "Closed")
col2.metric("Version", "0.1")
col3.metric("Modules", "5")

st.divider()

st.subheader("Roadmap")

st.checkbox("Dashboard UI", value=True)
st.checkbox("Live Market Data")
st.checkbox("Option Chain")
st.checkbox("PCR")
st.checkbox("Max Pain")
st.checkbox("OI Analysis")
st.checkbox("Trading Signals")
st.checkbox("AI Prediction")