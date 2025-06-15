with tab2:
    import matplotlib.dates as mdates
    import matplotlib.font_manager as fm

    # 한글 폰트 설정 (웹 실행 환경이면 기본 폰트 적용됨)
    plt.rcParams['font.family'] = 'Malgun Gothic' if 'Malgun Gothic' in plt.rcParams['font.family'] else 'DejaVu Sans'

    st.subheader("📅 날짜별 대여 건수와 날씨 요소 비교")

    # 날짜를 datetime으로 (혹시 몰라 재확인)
    daily_data['날짜'] = pd.to_datetime(daily_data['날짜'])

    # 📊 대여 건수 vs 일강수량
    st.markdown("#### ☔️ 강수량에 따른 대여 건수 변화")
    fig_rain, ax1 = plt.subplots(figsize=(12, 6))

    ax1.set_xlabel('일')
    ax1.set_ylabel('대여 건수', color='blue')
    ax1.plot(daily_data['날짜'], daily_data['대여 건수'], color='blue', label='대여 건수')
    ax1.tick_params(axis='y', labelcolor='blue')

    # x축 날짜를 "일" 단위로만 표시 (1~31)
    ax1.xaxis.set_major_locator(mdates.DayLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d'))
    fig_rain.autofmt_xdate()

    ax2 = ax1.twinx()
    ax2.set_ylabel('일강수량 (mm)', color='green')
    ax2.plot(daily_data['날짜'], daily_data['일강수량'], color='green', label='일강수량')
    ax2.tick_params(axis='y', labelcolor='green')

    plt.title('일별 대여 건수와 강수량 비교')
    plt.tight_layout()
    st.pyplot(fig_rain)

    # 🌡️ 대여 건수 vs 평균기온
    st.markdown("#### 🌡️ 평균기온에 따른 대여 건수 변화")
    fig_temp, ax3 = plt.subplots(figsize=(12, 6))

    ax3.set_xlabel('일')
    ax3.set_ylabel('대여 건수', color='blue')
    ax3.plot(daily_data['날짜'], daily_data['대여 건수'], color='blue', label='대여 건수')
    ax3.tick_params(axis='y', labelcolor='blue')

    ax3.xaxis.set_major_locator(mdates.DayLocator())
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%d'))
    fig_temp.autofmt_xdate()

    ax4 = ax3.twinx()
    ax4.set_ylabel('평균기온 (°C)', color='red')
    ax4.plot(daily_data['날짜'], daily_data['평균기온'], color='red', label='평균기온')
    ax4.tick_params(axis='y', labelcolor='red')

    plt.title('일별 대여 건수와 평균기온 비교')
    plt.tight_layout()
    st.pyplot(fig_temp)
