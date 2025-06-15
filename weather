import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title('🚲 따릉이 대여량과 날씨 분석')

st.write(daily_data.head())

fig, ax1 = plt.subplots(figsize=(12,6))

ax1.set_xlabel('날짜')
ax1.set_ylabel('대여 건수', color='blue')
ax1.plot(pd.to_datetime(daily_data['날짜']), daily_data['대여 건수'], color='blue', label='대여 건수')

ax2 = ax1.twinx()
ax2.set_ylabel('일강수량 (mm)', color='green')
ax2.plot(pd.to_datetime(daily_data['날짜']), daily_data['일강수량'], color='green', label='일강수량')

plt.title('날짜별 대여 건수와 일강수량 비교')

st.pyplot(fig)
