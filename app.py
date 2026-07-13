import streamlit as st
from datetime import datetime, timedelta

# 1. 페이지 설정
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

# [기존 주행/컨트롤 설정 데이터]
if "pilot_assist" not in st.session_state: st.session_state.pilot_assist = True
if "drive_mode" not in st.session_state: st.session_state.drive_mode = "Standard"
if "steering_feel" not in st.session_state: st.session_state.steering_feel = "부드러움"
if "start_stop" not in st.session_state: st.session_state.start_stop = True
if "lane_keeping" not in st.session_state: st.session_state.lane_keeping = True
if "ready_to_drive" not in st.session_state: st.session_state.ready_to_drive = True

if "interior_brightness" not in st.session_state: st.session_state.interior_brightness = 80
if "interior_light_dim" not in st.session_state: st.session_state.interior_light_dim = "높음"
if "reduce_alarm_sensitivity" not in st.session_state: st.session_state.reduce_alarm_sensitivity = False
if "welcome_light" not in st.session_state: st.session_state.welcome_light = True
if "wireless_charging" not in st.session_state: st.session_state.wireless_charging = True

# [시스템 상세 설정 데이터]
if "sys_time_24h" not in st.session_state: st.session_state.sys_time_24h = True
if "selected_language" not in st.session_state: st.session_state.selected_language = "한국어(대한민국)"

# 볼보 순정 다크 톤 배색 지정
bg_color = "rgb(18, 22, 28)"
card_color = "rgb(28, 34, 44)"
border_color = "rgb(42, 49, 61)"

if "brightness_slider" in st.query_params:
    st.session_state.interior_brightness = int(st.query_params["brightness_slider"])

# 2. 볼보 헤리티지 UI 스타일 정의
st.markdown(
    f"""
    <style>
    .stApp {{ background-color: {bg_color} !important; color: #ffffff !important; }}
    
    .block-container {{
        max-width: 510px !important;
        padding-top: 2.5rem !important;
        padding-bottom: 2rem !important;
        background-color: {card_color} !important;
        border-radius: 16px;
        box-shadow: 0 0 40px rgba(0, 0, 0, 0.6);
        margin: 0 auto;
    }}
    
    /* 상단 상태바 */
    .volvo-status-bar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 14px;
        color: #ffffff !important;
        font-weight: 500;
        margin-bottom: 25px;
        padding: 0 10px;
    }}
    
    /* 상단 메인 탭 */
    div.tab-zone button {{
        background-color: transparent !important;
        color: #8e959e !important;
        border: none !important;
        font-size: 16px !important;
        font-weight: 500 !important;
        padding: 8px 0 !important;
        width: 100% !important;
        box-shadow: none !important;
    }}
    div.tab-zone button[kind="primary"] {{
        color: #ffffff !important;
        font-weight: bold !important;
        border-bottom: 2px solid #ffffff !important;
        border-radius: 0px !important;
    }}
    
    /* ⚙️ 그리드 레이아웃 */
    div.volvo-grid-card div.stButton > button {{
        background-color: rgb(22, 27, 35) !important;
        color: #ffffff !important;
        border: 1px solid {border_color} !important;
        border-radius: 14px !important;
        height: 135px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
        width: 100% !important;
        white-space: pre-line !important;
    }}
    
    /* 🛠️ 세팅 박스 구조 */
    .volvo-title-row {{ font-size: 14px; color: #8e959e; font-weight: bold; margin-top: 22px; margin-bottom: 12px; padding-left: 5px; }}
    
    div.subpage-content-zone div[data-testid="stVerticalBlockBorderWrapper"] {{
        background-color: rgba(18, 22, 28, 0.4) !important;
        border: 1px solid {border_color} !important;
        border-radius: 14px !important;
        padding: 18px !important;
        margin-bottom: 5px !important;
    }}
    
    .setting-title {{ font-size: 15px; font-weight: bold; color: #ffffff; margin-bottom: 4px; }}
    .setting-desc {{ font-size: 12px; color: #8e959e; line-height: 1.4; }}
    
    /* 📋 시스템 리스트 항목 UI */
    .system-list-zone {{ display: flex; flex-direction: column; width: 100%; margin-top: -5px; }}
    .system-list-item {{ display: flex; justify-content: space-between; align-items: center; width: 100%; padding: 15px 8px; border-bottom: 1px solid #333b46; }}
    .system-list-item:last-child {{ border-bottom: none; }}
    .system-item-main {{ font-size: 15px; font-weight: 500; color: #ffffff; }}
    .system-item-sub {{ font-size: 12px; color: #8e959e; margin-top: 3px; }}
    .system-arrow {{ color: #5d646e; font-size: 15px; font-weight: bold; }}
    
    /* 알약형 세그먼트 */
    div.volvo-segment-row div[data-testid="stHorizontalBlock"] {{ gap: 0px !important; background-color: #1a1f27 !important; border-radius: 25px !important; padding: 4px !important; border: 1px solid #333b46 !important; margin-top: 12px !important; }}
    div.volvo-segment-row div.stButton > button[kind="primary"] {{ background-color: #00A3E0 !important; color: #ffffff !important; border: none !important; border-radius: 22px !important; font-weight: bold !important; height: 40px !important; }}
    div.volvo-segment-row div.stButton > button[kind="secondary"] {{ background-color: transparent !important; color: #727a85 !important; border: none !important; border-radius: 22px !important; height: 40px !important; box-shadow: none !important; }}
    
    /* 뒤로가기 버튼 */
    .back-btn-box button {{ background-color: transparent !important; color: #ffffff !important; border: none !important; font-size: 18px !important; font-weight: bold !important; padding: 0 !important; box-shadow: none !important; }}
    
    /* 공조 바 바닥 안착 */
    .volvo-bottom-bar {{ display: flex; justify-content: space-between; align-items: center; background-color: #111418; padding: 14px 18px; border-radius: 12px; margin-top: 40px; border: 1px solid #232830; }}
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

st.markdown(f'<div class="volvo-status-bar"><span>{time_string}</span><span>📶 LTE</span></div>', unsafe_allow_html=True)

# --- 2. 상단 메뉴 탭 (서브 메인 화면에서만 상단 노출) ---
if st.session_state.sub_page == "main":
    st.markdown('<div class="tab-zone">', unsafe_allow_html=True)
    top_col1, top_col2, top_col3 = st.columns(3)
    with top_col1:
        is_active = "primary" if st.session_state.current_tab == "퀵 컨트롤" else "secondary"
        if st.button("퀵 컨트롤", key="tab_quick", type=is_active, use_container_width=True):
            st.session_state.current_tab = "퀵 컨트롤"; st.rerun()
    with top_col2:
        is_active = "primary" if st.session_state.current_tab == "설정" else "secondary"
        if st.button("설정", key="tab_settings", type=is_active, use_container_width=True):
            st.session_state.current_tab = "설정"; st.rerun()
    with top_col3:
        is_active = "primary" if st.session_state.current_tab == "상태" else "secondary"
        if st.button("상태", key="tab_status", type=is_active, use_container_width=True):
            st.session_state.current_tab = "상태"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: -10px; margin-bottom: 25px;"></div>', unsafe_allow_html=True)


# --- 3. 화면 분기 처리 ---

# 🚗 [설정 -> 주행] 서브 페이지
if st.session_state.current_tab == "설정" and st.session_state.sub_page == "driving":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈  주행", key="back_to_settings"):
        st.session_state.sub_page = "main"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="subpage-content-zone">', unsafe_allow_html=True)
    st.markdown('<div class="volvo-title-row">운전자 지원 시스템</div>', unsafe_allow_html=True)
    with st.container(border=True):
        pa_col1, pa_col2 = st.columns([3.6, 1])
        with pa_col1: st.markdown('<div class="setting-title">Pilot Assist 기본 설정</div><div class="setting-desc">스티어링 휠에서 ▶을 눌러 어댑티브 크루즈 컨트롤과 Pilot Assist를 전환합니다.</div>', unsafe_allow_html=True)
        with pa_col2: 
            st.write("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
            st.session_state.pilot_assist = st.toggle("PA_tgl", value=st.session_state.pilot_assist, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

# 🎛️ [설정 -> 컨트롤] 서브 페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "control":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈  컨트롤", key="back_to_settings_ctrl"):
        st.session_state.sub_page = "main"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="subpage-content-zone"><div class="volvo-title-row">조명 및 디스플레이</div></div>', unsafe_allow_html=True)

# 💻 [설정 -> 시스템] 메인 리스트 페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "system":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈  시스템", key="back_to_settings_sys"):
        st.session_state.sub_page = "main"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="volvo-title-row">보안 상태</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin-bottom: 10px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="volvo-title-row">일반</div>', unsafe_allow_html=True)
    
    # 순정 디자인 클릭 링크를 구현하기 위해 버튼과 레이아웃 병합 처리
    st.markdown('<div class="system-list-zone">', unsafe_allow_html=True)
    
    col_a, col_b = st.columns([4.2, 0.8])
    with col_a: st.markdown(f'<div class="system-item-main">언어 및 입력</div><div class="system-item-sub">{st.session_state.selected_language}</div>', unsafe_allow_html=True)
    with col_b: 
        if st.button("〉", key="go_sys_language", use_container_width=True):
            st.session_state.sub_page = "sys_language"; st.rerun()
            
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin: 8px 0;"></div>', unsafe_allow_html=True)

    col_c, col_d = st.columns([4.2, 0.8])
    with col_c: st.markdown(f'<div class="system-item-main">날짜 및 시간</div><div class="system-item-sub">2026년 7월 13일, {"24시간 시계" if st.session_state.sys_time_24h else "12시간 시계"}</div>', unsafe_allow_html=True)
    with col_d:
        if st.button("〉", key="go_sys_datetime", use_container_width=True):
            st.session_state.sub_page = "sys_datetime"; st.rerun()
            
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin: 8px 0;"></div>', unsafe_allow_html=True)

    col_e, col_f = st.columns([4.2, 0.8])
    with col_e: st.markdown('<div class="system-item-main">애플리케이션</div><div class="system-item-sub">앱 권한</div>', unsafe_allow_html=True)
    with col_f:
        if st.button("〉", key="go_sys_apps", use_container_width=True):
            st.session_state.sub_page = "sys_apps"; st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)

# 🌐 [시스템 -> 1. 언어 및 입력] 상세페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "sys_language":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈  언어 및 입력", key="back_to_sys_main_1"):
        st.session_state.sub_page = "system"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="volvo-title-row">언어</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown('<div class="setting-title">시스템 언어</div>', unsafe_allow_html=True)
        lang_options = ["한국어(대한민국)", "English (United States)", "Deutsch", "Français"]
        idx = lang_options.index(st.session_state.selected_language) if st.session_state.selected_language in lang_options else 0
        selected = st.selectbox("Lang_select", options=lang_options, index=idx, label_visibility="collapsed")
        if selected != st.session_state.selected_language:
            st.session_state.selected_language = selected; st.rerun()
            
    st.markdown('<div class="volvo-title-row">입력</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown('<div class="setting-title">화면 키보드</div><div class="setting-desc">Android 키보드 (AOSP)</div>', unsafe_allow_html=True)

# ⏰ [시스템 -> 2. 날짜 및 시간] 상세페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "sys_datetime":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈  날짜 및 시간", key="back_to_sys_main_2"):
        st.session_state.sub_page = "system"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)

    with st.container(border=True):
        t24_col1, t24_col2 = st.columns([3.6, 1])
        with t24_col1:
            st.markdown('<div class="setting-title">24시간 형식 사용</div><div class="setting-desc">오후 1:00 대신 13:00 표기</div>', unsafe_allow_html=True)
        with t24_col2:
            st.write("<div style='margin-top:6px;'></div>", unsafe_allow_html=True)
            st.session_state.sys_time_24h = st.toggle("T24_tgl", value=st.session_state.sys_time_24h, label_visibility="collapsed")
            
    st.markdown('<div class="volvo-title-row">네트워크 동기화</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown('<div class="setting-title">자동 날짜 및 시간 설정</div><div class="setting-desc">차량 내부 GPS 및 네트워크 시간 기준 자동 보정 활성화</div>', unsafe_allow_html=True)

# 📱 [시스템 -> 3, 4. 애플리케이션] 상세페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "sys_apps":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈  애플리케이션", key="back_to_sys_main_3"):
        st.session_state.sub_page = "system"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="volvo-title-row">일반</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown('<div class="setting-title">앱 권한 관리자</div><div class="setting-desc">위치, 마이크, 캘린더 등 앱별 데이터 접근 제한</div>', unsafe_allow_html=True)
        
    st.markdown('<div class="volvo-title-row">고급 설정</div>', unsafe_allow_html=True)
    st.markdown('<div class="system-list-zone">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([4.2, 0.8])
    with col1: st.markdown('<div class="system-item-main">특별한 앱 액세스 권한</div><div class="system-item-sub">알림 최적화, 방해 금지 권한 관리</div>', unsafe_allow_html=True)
    with col2: st.button("〉", key="btn_app_acc1")
    
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin: 8px 0;"></div>', unsafe_allow_html=True)
    
    col3, col4 = st.columns([4.2, 0.8])
    with col3: st.markdown('<div class="system-item-main">기본 애플리케이션 설정</div><div class="system-item-sub">기본 네비게이션 및 어시스턴트 앱 지정</div>', unsafe_allow_html=True)
    with col4: st.button("〉", key="btn_app_acc2")
    
    st.markdown('</div>', unsafe_allow_html=True)

# ⚙️ [설정] 메인 탭 화면
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "main":
    st.write("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
        if st.button("주행", key="btn_drive_go", use_container_width=True):
            st.session_state.sub_page = "driving"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with row1_col2:
        st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
        if st.button("컨트롤", key="btn_control_go", use_container_width=True):
            st.session_state.sub_page = "control"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
        st.button("사운드", key="btn_sound_go", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with row2_col2:
        st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
        st.button("연결", key="btn_connect_go", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    row3_col1, row3_col2, row3_col3 = st.columns(3)
    with row3_col1:
        st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
        st.button("프로필", key="btn_profile_go", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with row3_col2:
        st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
        st.button("개인정보\n보호", key="btn_privacy_go", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with row3_col3:
        st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
        if st.button("시스템", key="btn_system_go", use_container_width=True):
            st.session_state.sub_page = "system"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# 📊 [상태] 및 📱 [퀵 컨트롤] 탭 처리 생략 (구조 보존)
else:
    st.write(f"현재 탭: {st.session_state.current_tab}")

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
