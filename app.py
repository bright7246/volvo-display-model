import streamlit as st
from datetime import datetime, timedelta

# 1. 페이지 설정 (3번 사진의 황금 규격 고정)
st.set_page_config(
    page_title="Volvo Main Display",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 세션 상태 초기화
if "current_tab" not in st.session_state:
    st.session_state.current_tab = "설정"
if "sub_page" not in st.session_state:
    st.session_state.sub_page = "main"

# 주행 설정 값 저장용 세션 상태
if "pilot_assist" not in st.session_state: st.session_state.pilot_assist = True
if "drive_mode" not in st.session_state: st.session_state.drive_mode = "Standard"
if "steering_feel" not in st.session_state: st.session_state.steering_feel = "부드러움"
if "start_stop" not in st.session_state: st.session_state.start_stop = True
if "lane_keeping" not in st.session_state: st.session_state.lane_keeping = True
if "ready_to_drive" not in st.session_state: st.session_state.ready_to_drive = True

# 볼보 순정 다크 톤 배색 지정
bg_color = "rgb(18, 22, 28)"
card_color = "rgb(28, 34, 44)"
border_color = "rgb(42, 49, 61)"

# 2. [골든 룰] 최상단 스타일 정의 (절대 수정 금지 구역)
st.markdown(
    f"""
    <style>
    /* 전체 앱 배경 */
    .stApp {{
        background-color: {bg_color} !important;
        color: #ffffff !important;
    }}
    
    /* 상단 여백 보정 컨테이너 */
    .block-container {{
        max-width: 480px !important;
        padding-top: 4rem !important; 
        padding-bottom: 2rem !important;
        margin: 0 auto;
        min-height: 850px; 
    }}
    
    /* 상단 시계 및 상태바 */
    .volvo-status-bar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 14px;
        color: #ffffff !important;
        font-weight: 500;
        padding: 5px 10px;
        margin-bottom: 25px;
    }}
    
    /* 상단 메인 탭 메뉴 */
    div.tab-zone button {{
        background-color: transparent !important;
        color: #8e959e !important;
        border: none !important;
        font-size: 16px !important;
        font-weight: 500 !important;
        padding: 8px 0 !important;
        width: 100% !important;
        box-shadow: none !important;
        border-radius: 0px !important;
    }}
    div.tab-zone button[kind="primary"] {{
        color: #ffffff !important;
        font-weight: bold !important;
        border-bottom: 2px solid #ffffff !important;
    }}
    
    /* 📱 퀵 컨트롤 전용 카드 스타일 */
    .volvo-card-content {{
        background-color: {card_color} !important;
        border: 1px solid {border_color} !important;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: #ffffff !important;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
        width: 100%;
    }}
    .side-btn {{ height: 185px; font-size: 15px; line-height: 1.5; }}
    .center-box {{ height: 400px; font-size: 24px; letter-spacing: 5px; font-family: 'Times New Roman', Times, serif; font-weight: 400; }}
    
    /* ⚙️ [버그 해결 핵심] 분리 현상을 원천 차단하는 스트림릿 전용 락(Lock) 타겟팅 */
    div.volvo-grid-card div.stButton > button {{
        background-color: {card_color} !important;
        color: #ffffff !important;
        border: 1px solid {border_color} !important;
        border-radius: 14px !important;
        height: 135px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4) !important;
        width: 100% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        white-space: pre-line !important; /* 개인정보 보호 줄바꿈 처리 대응 */
    }}
    
    /* 🚗 주행 서브페이지용 스타일 */
    .back-btn-box button {{
        background-color: transparent !important;
        color: #ffffff !important;
        border: none !important;
        font-size: 18px !important;
        font-weight: bold !important;
        padding: 0 !important;
        box-shadow: none !important;
    }}
    .sub-section-title {{
        font-size: 14px;
        color: #8e959e;
        font-weight: bold;
        margin-top: 25px;
        margin-bottom: 12px;
        padding-left: 5px;
    }}
    .setting-row-box {{
        background-color: {card_color};
        border: 1px solid {border_color};
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 12px;
    }}
    .setting-title {{ font-size: 15px; font-weight: bold; color: #ffffff; margin-bottom: 4px; }}
    .setting-desc {{ font-size: 12px; color: #8e959e; line-height: 1.4; }}
    
    /* 주행 세그먼트형 버튼 활성화 (순정 스카이블루) */
    div.stButton > button[id^="active-seg"] {{
        background-color: #00A3E0 !important;
        color: #ffffff !important;
        border: 1px solid #00A3E0 !important;
        border-radius: 20px !important;
        font-weight: bold !important;
        height: 42px !important;
    }}
    /* 주행 세그먼트형 버튼 비활성화 */
    div.stButton > button[id^="inactive-seg"] {{
        background-color: #232a35 !important;
        color: #8e959e !important;
        border: 1px solid {border_color} !important;
        border-radius: 20px !important;
        height: 42px !important;
    }}
    
    /* 하단 공조 바 */
    .volvo-bottom-bar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #111418;
        padding: 14px 18px;
        border-radius: 12px;
        margin-top: 50px; 
        border: 1px solid #232830;
    }}
    .bottom-item {{ font-size: 14px; font-weight: 500; color: #ffffff !important; text-align: center; }}
    .bottom-sub-label {{ font-size: 9px; color: #8e959e !important; display: block; margin-top: 2px; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- 1. 최상단 상태바 상시 표시 ---
utc_now = datetime.utcnow()
kor_now = utc_now + timedelta(hours=9)
ampm = "오전" if kor_now.hour < 12 else "오후"
display_hour = kor_now.hour % 12
display_hour = 12 if display_hour == 0 else display_hour
time_string = f"{ampm} {display_hour:02d}:{kor_now.minute:02d}"

st.markdown(
    f'<div class="volvo-status-bar"><span>{time_string}</span><span>📶 LTE</span></div>', 
    unsafe_allow_html=True
)

# --- 2. 상단 메뉴 탭 ---
if st.session_state.sub_page == "main":
    st.markdown('<div class="tab-zone">', unsafe_allow_html=True)
    top_col1, top_col2, top_col3 = st.columns(3)
    with top_col1:
        is_active = "primary" if st.session_state.current_tab == "퀵 컨트롤" else "secondary"
        if st.button("퀵 컨트롤", key="tab_quick", type=is_active, use_container_width=True):
            st.session_state.current_tab = "퀵 컨트롤"
            st.rerun()
    with top_col2:
        is_active = "primary" if st.session_state.current_tab == "설정" else "secondary"
        if st.button("설정", key="tab_settings", type=is_active, use_container_width=True):
            st.session_state.current_tab = "설정"
            st.rerun()
    with top_col3:
        is_active = "primary" if st.session_state.current_tab == "상태" else "secondary"
        if st.button("상태", key="tab_status", type=is_active, use_container_width=True):
            st.session_state.current_tab = "상태"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: -10px; margin-bottom: 25px;"></div>', unsafe_allow_html=True)


# --- 3. 화면 분기 처리 ---

# 🚗 [설정 -> 주행] 서브 페이지
if st.session_state.current_tab == "설정" and st.session_state.sub_page == "driving":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈  주행", key="back_to_settings"):
        st.session_state.sub_page = "main"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-section-title">운전자 지원 시스템</div>', unsafe_allow_html=True)
    st.markdown('<div class="setting-row-box">', unsafe_allow_html=True)
    pa_col1, pa_col2 = st.columns([3.6, 1])
    with pa_col1:
        st.markdown(
            '<div class="setting-title">Pilot Assist 기본 설정</div>'
            '<div class="setting-desc">스티어링 휠에서 ▶을 눌러 어댑티브 크루즈 컨트롤과 Pilot Assist를 전환합니다.</div>',
            unsafe_allow_html=True
        )
    with pa_col2:
        st.write("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
        st.session_state.pilot_assist = st.toggle("PA_tgl", value=st.session_state.pilot_assist, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-section-title">주행 역학</div>', unsafe_allow_html=True)
    st.markdown('<div class="setting-row-box">', unsafe_allow_html=True)
    st.markdown('<div class="setting-title">주행 모드</div>', unsafe_allow_html=True)
    st.markdown('<div class="setting-desc" style="margin-bottom:12px;">모든 종류의 일상 주행 시 효율성을 위해 가속, 주행 역학 및 조향이 최적화됩니다.</div>', unsafe_allow_html=True)
    dm_col1, dm_col2 = st.columns(2)
    with dm_col1:
        btn_id = "active-seg-std" if st.session_state.drive_mode == "Standard" else "inactive-seg-std"
        if st.button("Standard", key=btn_id, use_container_width=True):
            st.session_state.drive_mode = "Standard"
            st.rerun()
    with dm_col2:
        btn_id = "active-seg-off" if st.session_state.drive_mode == "Off-road" else "inactive-seg-off"
        if st.button("Off-road", key=btn_id, use_container_width=True):
            st.session_state.drive_mode = "Off-road"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="setting-row-box">', unsafe_allow_html=True)
    st.markdown('<div class="setting-title">스티어링 감도</div>', unsafe_allow_html=True)
    st.write("<div style='margin-top:6px;'></div>", unsafe_allow_html=True)
    sf_col1, sf_col2 = st.columns(2)
    with sf_col1:
        btn_id = "active-seg-sf1" if st.session_state.steering_feel == "부드러움" else "inactive-seg-sf1"
        if st.button("부드러움", key=btn_id, use_container_width=True):
            st.session_state.steering_feel = "부드러움"
            st.rerun()
    with sf_col2:
        btn_id = "active-seg-sf2" if st.session_state.steering_feel == "단단함" else "inactive-seg-sf2"
        if st.button("단단함", key=btn_id, use_container_width=True):
            st.session_state.steering_feel = "단단함"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="setting-row-box">', unsafe_allow_html=True)
    ss_col1, ss_col2 = st.columns([3.6, 1])
    with ss_col1:
        st.markdown(
            '<div class="setting-title">Start/Stop</div>'
            '<div class="setting-desc">정지 시 일시적으로 엔진을 끕니다. 새로 주행할 때마다 켜짐으로 재설정됩니다.</div>',
            unsafe_allow_html=True
        )
    with ss_col2:
        st.write("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
        st.session_state.start_stop = st.toggle("SS_tgl", value=st.session_state.start_stop, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-section-title">안전 어시스트</div>', unsafe_allow_html=True)
    st.markdown('<div class="setting-row-box">', unsafe_allow_html=True)
    lk_col1, lk_col2 = st.columns([3.6, 1])
    with lk_col1:
        st.markdown(
            '<div class="setting-title">차선유지 보조 시스템</div>'
            '<div class="setting-desc">갑작스런 차선 이탈을 방지하도록 도와줍니다.</div>',
            unsafe_allow_html=True
        )
    with lk_col2:
        st.write("<div style='margin-top:5px;'></div>", unsafe_allow_html=True)
        st.session_state.lane_keeping = st.toggle("LK_tgl", value=st.session_state.lane_keeping, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="setting-row-box">', unsafe_allow_html=True)
    rd_col1, rd_col2 = st.columns([3.6, 1])
    with rd_col1:
        st.markdown(
            '<div class="setting-title">주행 준비 알림</div>'
            '<div class="setting-desc">전방 차량이 주행을 시작한 후 알림을 제공합니다.</div>',
            unsafe_allow_html=True
        )
    with rd_col2:
        st.write("<div style='margin-top:5px;'></div>", unsafe_allow_html=True)
        st.session_state.ready_to_drive = st.toggle("RD_tgl", value=st.session_state.ready_to_drive, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)


# ⚙️ [설정] 메인 탭 화면 (★HTML 찌꺼기 완벽 제거형 컨테이너 구조★)
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "main":
    st.write("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

    # 1라인: 주행 / 컨트롤
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        with st.container(border=False):
            st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
            if st.button("주행", key="btn_drive_go", use_container_width=True):
                st.session_state.sub_page = "driving"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
    with row1_col2:
        with st.container(border=False):
            st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
            st.button("컨트롤", key="btn_control_go", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # 2라인: 사운드 / 연결
    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        with st.container(border=False):
            st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
            st.button("사운드", key="btn_sound_go", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    with row2_col2:
        with st.container(border=False):
            st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
            st.button("연결", key="btn_connect_go", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # 3라인: 프로필 / 개인정보 보호 / 시스템
    row3_col1, row3_col2, row3_col3 = st.columns(3)
    with row3_col1:
        with st.container(border=False):
            st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
            st.button("프로필", key="btn_profile_go", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    with row3_col2:
        with st.container(border=False):
            st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
            st.button("개인정보\n보호", key="btn_privacy_go", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    with row3_col3:
        with st.container(border=False):
            st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
            st.button("시스템", key="btn_system_go", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)


# 📊 [상태] 탭 화면
elif st.session_state.current_tab == "상태":
    st.subheader("📊 차량 상태")
    st.write("차량 진단 및 정보를 확인합니다.")


# 📱 [퀵 컨트롤] 탭 화면 (골든 룰 수호)
else:
    st.write("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True) 
    main_col1, main_col2, main_col3 = st.columns([1, 1.3, 1])

    with main_col1:
        st.markdown('<div class="volvo-card-content side-btn">차선<br>유지</div>', unsafe_allow_html=True)
        st.write("<div style='margin-top:25px;'></div>", unsafe_allow_html=True)
        st.markdown('<div class="volvo-card-content side-btn">Start<br>Stop</div>', unsafe_allow_html=True)

    with main_col2:
        st.markdown('<div class="volvo-card-content center-box">VOLVO</div>', unsafe_allow_html=True)

    with main_col3:
        st.markdown('<div class="volvo-card-content side-btn">알람<br>줄이기</div>', unsafe_allow_html=True)
        st.write("<div style='margin-top:25px;'></div>", unsafe_allow_html=True)
        st.markdown('<div class="volvo-card-content side-btn">헤드<br>레스트</div>', unsafe_allow_html=True)


# --- 4. 하단 공조 장치 바 ---
bottom_html = (
    '<div class="volvo-bottom-bar">'
    '<div class="bottom-item" style="color: #8e959e; font-size: 16px;">㗊</div>'
    '<div class="bottom-item">💺 LO</div>'
    '<div class="bottom-item"><span style="font-size: 16px;">🌀</span><span class="bottom-sub-label">공기 재순환</span></div>'
    '<div class="bottom-item">LO 💺</div>'
    '<div class="bottom-item" style="font-size: 16px; opacity: 0.9;">🚗</div>'
    '</div>'
)
st.markdown(bottom_html, unsafe_allow_html=True)
