# Version 1.0

import streamlit as st
from predict_app import show_predict_page
from explore_app import show_explore_page

st.set_page_config(page_title='Đoán giá xe máy')

page = st.sidebar.selectbox("Lựa chọn trang", ("Hệ thống đoán giá xe máy", "Khám phá thông tin"))

if page == "Hệ thống đoán giá xe máy":
    show_predict_page()
else:
    show_explore_page()