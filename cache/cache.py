import streamlit as st


@st.cache_data(ttl=10)
def market_data(provider, symbol):
    return provider.get_market_data(symbol)


@st.cache_data(ttl=10)
def option_chain(provider, symbol):
    return provider.get_option_chain(symbol)


@st.cache_data(ttl=3600)
def expiry(provider, symbol):
    return provider.get_expiry_list(symbol)