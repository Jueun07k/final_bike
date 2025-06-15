import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('🚲 따릉이 대여량과 날씨 분석')

@st.cache_data
def load_data():
    df_bike = pd.read_csv('rental_counts_by_date.csv', parse_dates=['날짜'])
    df_weather = pd.read_csv('OBS_ASOS_DD_20250610143611 (1).csv', encoding='cp949')  # 인코딩도 환경에 따라 조정
    
    # 날짜 컬럼명 맞춰주기 (예: '일시' 혹은 '날짜'일 가능성 있음)
    # 아래는 예시, 실제 컬럼명 확인 필요
    df_weather.rename(columns={'일시': '날짜', '평균기온(°C)': '평균기온', '일강수량(mm)': '일강수량'}, inplace=True)
    
    # 날짜 포맷 통일 (문자열->날짜->문자열)
    df_weather['날짜'] = pd.to_datetime(df_weather['날짜']).dt.strftime('%Y-%m-%d')
    df_bike['날짜'] = pd.to_datetime(df_bike['날짜']).dt.strftime('%Y-%m-%d')

    # 날짜별 대여 건수 집계
    daily_rentals = df_bike.groupby('날짜').size().reset_index(name='대여 건수')

    # 날씨 데이터 중 필요한 컬럼만 병합
    daily_data = pd.merge(daily_rentals, df_weather[['날짜', '평균기온', '일강수량']], on='날짜', how='left')
    
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
