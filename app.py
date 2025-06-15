import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🚲 서울시 따릉이 이용 분석")

@st.cache_data
def load_data():
    # ✅ 현재 폴더에 있는 파일만 읽어옵니다.
    return pd.read_csv('rental_counts_by_date.csv', parse_dates=['날짜'])

df = load_data()

st.subheader("📅 날짜별 대여량")
fig, ax = plt.subplots()
ax.plot(df['날짜'], df['대여 건수'], color='green')
ax.set_xlabel('날짜')
ax.set_ylabel('대여 건수')
ax.grid(True)
st.pyplot(fig)
