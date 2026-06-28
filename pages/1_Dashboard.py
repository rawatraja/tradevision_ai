import streamlit as st
from providers.factory import get_provider

# Get the active data provider
provider = get_provider()

# Fetch market data
market = provider.get_market_data("NIFTY")

st.title("📊 Dashboard")

st.success("Dashboard page is working!")

st.metric(
    label="Spot Price",
    value=market["spot"],
    delta=market["change"]
)

st.write(f"Last Updated: {market['time']}")

st.divider()

st.subheader("Coming Soon")

st.write("✅ Live Spot Price")
st.write("⏳ Live Option Chain")
st.write("⏳ PCR")
st.write("⏳ Max Pain")
st.write("⏳ OI Analysis")
st.write("⏳ AI Signals")