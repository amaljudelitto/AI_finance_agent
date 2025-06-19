# app.py

import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Indian Stock Price Checker", layout="centered")

st.title("📈 Indian Stock Price Checker")

symbol_input = st.text_input("Enter Stock Symbol (NSE)", placeholder="e.g. RELIANCE, INFY, TCS")

if symbol_input:
    symbol = symbol_input.strip().upper()
    full_symbol = f"{symbol}.NS"

    try:
        ticker = yf.Ticker(full_symbol)
        data = ticker.history(period="1d")
        if data.empty:
            st.error(f"⚠️ No data found for {symbol}. Please check the symbol.")
        else:
            price = data['Close'].iloc[-1]
            st.success(f"💰 Current price of **{symbol}** is ₹{price:.2f}")
            st.write(data.tail())  # Optional: show full row
    except Exception as e:
        st.error(f"❌ Error fetching data: {e}")
