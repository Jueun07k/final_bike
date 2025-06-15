import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🚲 서울시 따릉이 이용 분석 대시보드")

@st.cache_data
def load_data():
    # 상위 폴더의 data 폴더에서 CSV 불러오기
    return pd.read_csv('../data/rental_counts_by_date.csv', parse_dates=['날짜'])

df = load_data()

# 시각화
st.subheader("📊 날짜별 대여량 추이")
fig, ax = plt.subplots()
ax.plot(df['날짜'], df['대여 건수'], color='green')
ax.set_xlabel("날짜")
ax.set_ylabel("대여 건수")
ax.grid(True)
st.pyplot(fig)
