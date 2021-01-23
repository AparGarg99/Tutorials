################################################# LIBRARIES ##################################################
import yfinance as yf
import streamlit as st

############################################## BACKEND ################################################

#get data on Google ticker
tickerData = yf.Ticker('GOOGL')
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

################################################# MAIN PAGE ##################################################

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Google!

""")


st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)


st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
