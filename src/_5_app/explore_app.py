import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

DATA = r'/home/duyanh/Documents/VS_WorkSpace/projects/programming_for_DS_v1/data/moto_cleaned_EDA.csv'

df = pd.read_csv(DATA)


def show_explore_page():

    fix1 = plt.figure()
    
    sns.countplot(data=df, x='Hang_xe',
                        order=df['Hang_xe'].value_counts().index)
    plt.xticks(rotation=45)
    
    st.write("### Số lượng xe của mỗi hãng")
    st.pyplot(fix1)

    gia_TB = df.groupby(['Hang_xe', 'Dong_xe'], as_index=False)['Gia_xe'].mean()
    cac_hang = list(set(df['Hang_xe']))
    
    fix2 = plt.figure()

    temp_df = gia_TB[['Dong_xe', 'Gia_xe']][gia_TB['Hang_xe'] == 'Honda']
    sns.barplot(data=temp_df, x="Dong_xe", y="Gia_xe")
    plt.xticks(rotation=90)


    st.write("### Giá xe trung bình của bốn hãng có số lượng xe nhiều nhất:")

    st.write(f"##### 1. Giá xe trung bình của các dòng xe thuộc hãng xe Honda")
    st.pyplot(fix2)

    fix3 = plt.figure()

    temp_df = gia_TB[['Dong_xe', 'Gia_xe']][gia_TB['Hang_xe'] == 'Yamaha']
    sns.barplot(data=temp_df, x="Dong_xe", y="Gia_xe")
    plt.xticks(rotation=90)
        
    st.write(f"##### 2. Giá xe trung bình của các dòng xe thuộc hãng xe Yamaha")
    st.pyplot(fix3)

    fix4 = plt.figure()

    temp_df = gia_TB[['Dong_xe', 'Gia_xe']][gia_TB['Hang_xe'] == 'Piaggio']
    sns.barplot(data=temp_df, x="Dong_xe", y="Gia_xe")
    plt.xticks(rotation=90)
        
    st.write(f"##### 3. Giá xe trung bình của các dòng xe thuộc hãng xe Piaggio")
    st.pyplot(fix4)

    fix5 = plt.figure()

    temp_df = gia_TB[['Dong_xe', 'Gia_xe']][gia_TB['Hang_xe'] == 'Suzuki']
    sns.barplot(data=temp_df, x="Dong_xe", y="Gia_xe")
    plt.xticks(rotation=90)
        
    st.write(f"##### 4. Giá xe trung bình của các dòng xe thuộc hãng xe Suzuki")
    st.pyplot(fix5)


