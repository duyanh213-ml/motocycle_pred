import streamlit as st
import pickle
import numpy as np
import pandas as pd

THIS_YEAR = 2023

DATA = r'./model_and_data/moto_cleaned_EDA.csv'

SAVE_MODEL = r'./model_and_data/model.pkl'


def load_model():
    with open(SAVE_MODEL, 'rb') as file:
        predict_system = pickle.load(file)
    return predict_system


def dong(hang):
    dong_xe = list(set(df['Dong_xe'][df['Hang_xe'] == hang]))
    return dong_xe


predict_system = load_model()

df = pd.read_csv(DATA)


def show_predict_page():
    st.title("Trang web dự đoán giá xe máy")

    st.write("""### Hoàn tất các thông tin sau:""")

    hang_xe_lst = list(set(df['Hang_xe']))

    nam_dang_ky_lst = list(set(df['Nam_dang_ky']))

    nam_dang_ky_lst.append("Trước năm 1980")

    dung_tich_lst = list(set(df['Dung_tich_xe']))
    loai_xe_lst = list(set(df['Loai_xe']))

    hang_xe = st.selectbox("Hãng xe", hang_xe_lst)

    if hang_xe:
        dong_xe_lst = dong(hang_xe)
        dong_xe = st.selectbox("Dòng xe", dong_xe_lst)

    so_km = st.slider("Số km đã đi", 0, 100000, 10000)

    nam_dk = st.selectbox("Năm đăng ký", nam_dang_ky_lst)

    if nam_dk == "Trước năm 1980":
        nam_dk = "1980"

    tinh_trang = st.selectbox("Tình trạng xe", ['Đã sử dụng', 'Mới'])

    dung_tich_xe = st.selectbox("Khoảng dung tích xe", dung_tich_lst)

    loai_xe = st.selectbox("Loại xe", loai_xe_lst)

    ok = st.button("Dự đoán giá xe")
    if ok:

        st.write("(Dự đoán mang tính chất tham khảo)")

        x = np.array([[(THIS_YEAR - int(nam_dk)), tinh_trang,
                     dung_tich_xe, dong_xe, so_km, loai_xe]])

        x[:, 1] = predict_system['le_tinh_trg'].transform(x[:, 1])
        x[:, 2] = predict_system['le_dung_tich'].transform(x[:, 2])
        x[:, 3] = predict_system['le_dong_xe'].transform(x[:, 3])
        x[:, 5] = predict_system['le_loai_xe'].transform(x[:, 5])

        x = x.astype(float)
        cols = predict_system['cols']

        for i in range(len(x[0])):
            x[:, i] = (x[:, i] - cols[i][0]) / (cols[i][1] - cols[i][2])

        price_pred = round(float(predict_system['model'].predict(x)), 1)

        price_pred = f"{price_pred}00.000"

        st.subheader(f"Giá xe được dự đoán là {price_pred}đ")
