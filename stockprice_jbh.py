import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# JBH Hifi Nov-Dec 2022

Closing price and volume of JB Hifi are shown below:

""")



tickerSymbol = 'JBH.AX'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='id', start = '2022-11-01', end = '2022-12-18')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
