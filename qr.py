import streamlit as st
import qrcode as qr
from PIL import Image

st.title("QR Code Generator")

data = st.text_input("Enter data")
if st.button("Generate"):
    img = qr.make(data)
    img.save('myqr.png')
    st.image('myqr.png')
