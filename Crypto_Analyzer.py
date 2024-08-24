import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Crypto Analyzer")

uploaded_file = st.file_uploader("Upload a Crypto-Coin data", type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader('Coin Chart')
    x_axis = 'Date'
    y_axis = 'High'
    
    # Convert 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Set 'Date' column as index
    df.set_index('Date', inplace=True)
    
    st.line_chart(df[y_axis])

    st.subheader('Statistics')
    col1, col2 = st.columns(2)

    with col1:

        marketcap = df['Marketcap'].tail(1)
        st.metric('Market Cap', marketcap.iloc[0])

        ath = df['High'].max()
        st.metric('All Time High', ath)

        avg_price = df['Close'].mean()
        st.metric('Average Price', avg_price)

    with col2:

        volume = df['Volume'].sum()
        st.metric('Volume', volume)
        
        atl = df['Low'].min()  # Changed 'High' to 'Low'
        st.metric('All Time Low', atl)

    st.write('')
    st.subheader("Basic Data")
    st.write(df[['Symbol', 'Open', 'Close', 'High', 'Low', 'Marketcap']])  # Removed 'Date'