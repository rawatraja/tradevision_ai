import streamlit as st
from services.market_service import get_market

market = get_market("NIFTY")

spot = market["spot"]
change = market["change"]
updated = market["time"]

st.title("📊 Dashboard")

st.success("Dashboard page is working!")

st.metric(
    label="Spot Price",
    value=spot,
    delta=change
)

st.caption(f"Updated: {updated}")

st.divider()

st.subheader("Coming Soon")

st.write("✅ Live Spot Price")
st.write("⏳ Live Option Chain")
st.write("⏳ PCR")
st.write("⏳ Max Pain")
st.write("⏳ OI Analysis")
st.write("⏳ AI Signals")