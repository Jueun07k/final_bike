import streamlit as st
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm

# ✅ 한글 폰트 설정
font_path = './NanumBarunGothic.ttf'
fontprop = fm.FontProperties(fname=font_path)
mpl.rc('font', family=fontprop.get_name())
mpl.rcParams['axes.unicode_minus'] = False

# 📌 페이지 타이틀
st.title('🚲 서울시 따릉이 및 날씨 데이터 분석')

# ✅ 데이터 로드 함수들
@st.cache_data
def load_bike_data():
    return pd.read_csv('rental_counts_by_date.csv', parse_dates=['날짜'])

@st.cache_data
def load_weather_data():
    df_weather = pd.read_csv('OBS_ASOS_DD_20250610143611 (1).csv', encoding='cp949')
    df_weather = df_weather[['일시', '평균기온(°C)', '일강수량(mm)']]
    df_weather.rename(columns={
        '일시': '날짜',
        '평균기온(°C)': '평균기온',
        '일강수량(mm)': '일강수량'
    }, inplace=True)
    df_weather['날짜'] = pd.to_datetime(df_weather['날짜']).dt.strftime('%Y-%m-%d')
    return df_weather

# ✅ 데이터 불러오기 및 병합
bike_data = load_bike_data()
weather_data = load_weather_data()

bike_data['날짜'] = bike_data['날짜'].dt.strftime('%Y-%m-%d')
daily_data = pd.merge(bike_data, weather_data, on='날짜', how='left')
daily_data['날짜'] = pd.to_datetime(daily_data['날짜'])

# ✅ 탭 생성
tab1, tab2 = st.tabs(["🚲 따릉이 이용 현황", "🌦️ 날씨와의 관계 분석"])

# -------------------------------
# 🚲 탭1: 따릉이 이용 현황
# -------------------------------
with tab1:
    st.subheader("📅 날짜별 따릉이 대여량")
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(daily_data['날짜'], daily_data['대여 건수'], color='blue', marker='o')
    ax1.set_xlabel('날짜')
    ax1.set_ylabel('대여 건수')
    ax1.xaxis.set_major_locator(mdates.DayLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d'))
    fig1.autofmt_xdate()
    ax1.grid(True)
    plt.title("일별 대여 건수 추이")
    st.pyplot(fig1)

# -------------------------------
# 🌦️ 탭2: 날씨와의 관계 분석
# -------------------------------
with tab2:
    st.subheader("📈 날씨 요소에 따른 따릉이 이용 변화")

    # ☔️ 강수량 vs 대여량
    st.markdown("#### ☔️ 강수량에 따른 대여 건수 변화")
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    ax2.set_xlabel('일')
    ax2.set_ylabel('대여 건수', color='blue')
    ax2.plot(daily_data['날짜'], daily_data['대여 건수'], color='blue', label='대여 건수')
    ax2.tick_params(axis='y', labelcolor='blue')
    ax2.xaxis.set_major_locator(mdates.DayLocator())
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%d'))
    fig2.autofmt_xdate()
    ax2.grid(True)

    ax3 = ax2.twinx()
    ax3.set_ylabel('일강수량 (mm)', color='green')

    # ✅ 선 → 점으로 변경
    ax3.scatter(daily_data['날짜'], daily_data['일강수량'], color='green', label='일강수량', s=40)
    ax3.tick_params(axis='y', labelcolor='green')

    plt.title("일별 대여 건수와 강수량 비교")
    st.pyplot(fig2)

    # 🌡️ 평균기온 vs 대여량
    st.markdown("#### 🌡️ 평균기온에 따른 대여 건수 변화")
    fig3, ax4 = plt.subplots(figsize=(12, 6))
    ax4.set_xlabel('일')
    ax4.set_ylabel('대여 건수', color='blue')
    ax4.plot(daily_data['날짜'], daily_data['대여 건수'], color='blue')
    ax4.tick_params(axis='y', labelcolor='blue')
    ax4.xaxis.set_major_locator(mdates.DayLocator())
    ax4.xaxis.set_major_formatter(mdates.DateFormatter('%d'))
    fig3.autofmt_xdate()
    ax4.grid(True)

    ax5 = ax4.twinx()
    ax5.set_ylabel('평균기온 (°C)', color='red')
    ax5.plot(daily_data['날짜'], daily_data['평균기온'], color='red')
    ax5.tick_params(axis='y', labelcolor='red')

    plt.title("일별 대여 건수와 평균기온 비교")
    st.pyplot(fig3)
