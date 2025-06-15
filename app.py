import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm

# 한글 폰트 설정
matplotlib.rcParams['font.family'] = 'NanumGothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# 데이터 로드 함수
@st.cache_data
def load_bike_data():
    return pd.read_csv('rental_counts_by_date.csv', parse_dates=['날짜'])

@st.cache_data
def load_weather_data():
    df_weather = pd.read_csv('OBS_ASOS_DD_20250610143611 (1).csv', encoding='cp949')
    df_weather = df_weather[['일시', '평균기온(°C)', '일강수량(mm)']]
    df_weather.rename(columns={'일시': '날짜', '평균기온(°C)': '평균기온', '일강수량(mm)': '일강수량'}, inplace=True)
    df_weather['날짜'] = pd.to_datetime(df_weather['날짜']).dt.strftime('%Y-%m-%d')
    return df_weather

# 데이터 로드
bike_data = load_bike_data()
weather_data = load_weather_data()

# 날짜 형식 맞추기
bike_data['날짜'] = bike_data['날짜'].dt.strftime('%Y-%m-%d')
daily_data = pd.merge(bike_data, weather_data, on='날짜', how='left')

# Streamlit 앱 구성
tab1, tab2 = st.tabs(["따릉이 이용 현황", "날씨와 연동한 분석"])

with tab1:
    st.subheader("📅 날짜별 따릉이 대여량")
    fig1, ax1 = plt.subplots(figsize=(12,6))
    ax1.plot(pd.to_datetime(daily_data['날짜']), daily_data['대여 건수'], marker='o', color='blue')
    ax1.set_xlabel('날짜')
    ax1.set_ylabel('대여 건수', color='blue')
    ax1.grid(True)
    st.pyplot(fig1)

with tab2:
    st.subheader("📅 날짜별 대여 건수와 일강수량 비교")
    fig2, ax2 = plt.subplots(figsize=(12,6))
    ax2.set_xlabel('날짜')
    ax2.set_ylabel('대여 건수', color='blue')
    ax2.plot(pd.to_datetime(daily_data['날짜']), daily_data['대여 건수'], color='blue', label='대여 건수')
    ax3 = ax2.twinx()
    ax3.set_ylabel('일강수량 (mm)', color='green')
    ax3.scatter(pd.to_datetime(daily_data['날짜']), daily_data['일강수량'], color='green', label='일강수량', s=40)
    plt.title('날짜별 대여 건수와 일강수량 비교')
    st.pyplot(fig2)
