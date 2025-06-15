import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('🚲 서울시 따릉이 및 날씨 데이터 분석')

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

bike_data = load_bike_data()
weather_data = load_weather_data()

bike_data['날짜'] = bike_data['날짜'].dt.strftime('%Y-%m-%d')
daily_data = pd.merge(bike_data, weather_data, on='날짜', how='left')

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
    import matplotlib.dates as mdates  # 반드시 tab2 내부 or 파일 상단에 있어야 합니다

    st.subheader("📅 날짜별 대여 건수와 일강수량 비교")

    # 날짜 타입 변환 (혹시 문자열일 경우 대비)
    daily_data['날짜'] = pd.to_datetime(daily_data['날짜'])

    fig2, ax1 = plt.subplots(figsize=(12, 6))

    # 왼쪽 y축: 대여 건수
    ax1.set_xlabel('날짜')
    ax1.set_ylabel('대여 건수', color='blue')
    ax1.plot(daily_data['날짜'], daily_data['대여 건수'], color='blue', label='대여 건수')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.grid(True)

    # x축 날짜 포맷 조정
    ax1.xaxis.set_major_locator(mdates.MonthLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    fig2.autofmt_xdate()

    # 오른쪽 y축: 일강수량
    ax2 = ax1.twinx()
    ax2.set_ylabel('일강수량 (mm)', color='green')
    ax2.plot(daily_data['날짜'], daily_data['일강수량'], color='green', label='일강수량')
    ax2.tick_params(axis='y', labelcolor='green')

    plt.title('📊 날짜별 대여 건수와 일강수량 비교')
    plt.tight_layout()
    st.pyplot(fig2)
