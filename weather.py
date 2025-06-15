import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('🚲 따릉이 대여량과 날씨 분석')

@st.cache_data
def load_data():
    # 따릉이 대여량 데이터 (날짜별 집계된 파일)
    df_bike = pd.read_csv('rental_counts_by_date.csv', parse_dates=['날짜'])
    
    # 날씨 데이터 불러오기, encoding 환경에 맞게 조정하세요
    df_weather = pd.read_csv('OBS_ASOS_DD_20250610143611 (1).csv', encoding='cp949')
    
    # 필요한 컬럼만 추출
    df_weather = df_weather[['일시', '평균기온(°C)', '일강수량(mm)']]
    
    # 컬럼명 바꾸기 (일시 -> 날짜)
    df_weather.rename(columns={'일시': '날짜', '평균기온(°C)': '평균기온', '일강수량(mm)': '일강수량'}, inplace=True)
    
    # 날짜 포맷 맞추기
    df_weather['날짜'] = pd.to_datetime(df_weather['날짜']).dt.strftime('%Y-%m-%d')
    df_bike['날짜'] = pd.to_datetime(df_bike['날짜']).dt.strftime('%Y-%m-%d')

    # 따릉이 대여량이 날짜별로 집계된 상태면 바로 병합
    daily_data = pd.merge(df_bike, df_weather, on='날짜', how='left')
    
    return daily_data

daily_data = load_data()

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
