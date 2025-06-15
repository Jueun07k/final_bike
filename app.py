import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🚲 서울시 따릉이 이용 분석")

@st.cache_data
def load_data():
    return pd.read_csv('rental_counts_by_date.csv', parse_dates=['날짜'])

df = load_data()

# 🔹 '일(day)'만 추출해서 새로운 컬럼 만들기
df['일'] = df['날짜'].dt.day

st.subheader("📅 날짜별 대여량 (일자 기준)"
             
fig, ax = plt.subplots(figsize=(12, 6))  # 🔸 가로(width)=12, 세로(height)=6
ax.plot(df['일'], df['대여 건수'], color='green', marker='o')
ax.set_xlabel('일')
ax.set_ylabel('대여 건수')
ax.set_xticks(df['일'])  # 일 단위로 x축 표시
ax.grid(True)

st.pyplot(fig)
