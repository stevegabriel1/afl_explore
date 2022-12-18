import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# JBH price history

Closing price and volume of JB Hifi are shown below:

""")



tickerSymbol = 'JBH.AX'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='id', start = '2015-1-31', end = '2022-12-15')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
