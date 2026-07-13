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

# [데이터 세션 상태 사수]
for key, val in {
    "pilot_assist": True, "drive_mode": "Standard", "steering_feel": "부드러움",
    "start_stop": True, "lane_keeping": True, "ready_to_drive": True,
    "interior_brightness": 80, "interior_light_dim": "높음",
    "reduce_alarm_sensitivity": False, "welcome_light": True, "wireless_charging": True,
    "left_drive_light_adjust": False, "cluster_trip_info": "자동",
    "unlock_mode": "모두", "sunroof_curtain_auto_close": False,
    "turn_signal_blink": True, "auto_fold_mirror": True,
    "sys_time_auto": True, "sys_timezone_auto": True, "sys_time_24h": True,
    "selected_language": "한국어(대한민국)",
    "nugu_enabled": True, "nugu_alarm": True, "nugu_perf": False, "nugu_permission_clear": True
}.items():
    if key not in st.session_state: st.session_state[key] = val

# 볼보 순정 배색
bg_color = "rgb(18, 22, 28)"
card_color = "rgb(28, 34, 44)"
border_color = "rgb(42, 49, 61)"

# 2. [골든 룰] 스타일 정의 (설정 버튼 92px 강제 고정 셋팅)
st.markdown(
    f"""
    <style>
    .stApp {{ background-color: {bg_color} !important; color: #ffffff !important; }}
    
    div[data-testid="stMainBlockContainer"] {{
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
        display: flex; justify-content: space-between; align-items: center;
        font-family: 'Helvetica Neue', sans-serif; font-size: 14px;
        color: #ffffff !important; font-weight: 500; margin-bottom: 25px; padding: 0 10px;
    }}
    
    /* 상단 메인 탭 */
    div.tab-zone button {{
        background-color: transparent !important; color: #8e959e !important;
        border: none !important; font-size: 16px !important; font-weight: 500 !important;
        padding: 8px 0 !important; width: 100% !important; box-shadow: none !important;
    }}
    div.tab-zone button[kind="primary"] {{
        color: #ffffff !important; font-weight: bold !important;
        border-bottom: 2px solid #ffffff !important; border-radius: 0px !important;
    }}
    
    /* 🎯 [수술 부위] 설정 메뉴 버튼 92px 강제 고정 및 개조 */
    div.volvo-setting-grid-box div.stButton > button {{
        height: 92px !important; /* 퀵컨트롤 차선유지 185px의 절반 */
        background-color: rgb(22, 27, 35) !important;
        border: 1px solid {border_color} !important;
        border-radius: 14px !important;
        color: #ffffff !important;
        font-size: 17px !important;
        font-weight: bold !important;
        width: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
    }}
    /* 버튼 안의 텍스트 정중앙 강제 배치 */
    div.volvo-setting-grid-box div.stButton > button div[data-testid="stMarkdownContainer"] p {{
        margin-bottom: 0 !important;
        font-size: 17px !important;
        line-height: 1 !important;
    }}
    
    /* 📱 퀵 컨트롤 전용 (185px) */
    .volvo-card-content {{
        background-color: rgb(22, 27, 35) !important;
        border: 1px solid {border_color} !important;
        border-radius: 14px; display: flex; align-items: center; justify-content: center;
        text-align: center; color: #ffffff !important; font-weight: bold;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3); width: 100%;
    }}
    .side-btn {{ height: 185px; font-size: 16px; line-height: 1.5; }}
    .center-box {{ height: 400px; font-size: 24px; letter-spacing: 5px; font-family: 'Times New Roman', Times, serif; font-weight: 400; }}

    /* 📋 리스트 레이아웃 */
    .text-container-fix {{ display: flex; flex-direction: column; justify-content: center; min-height: 48px; }}
    .system-item-main {{ font-size: 15px; font-weight: 500; color: #ffffff; line-height: 1.2; }}
    .system-item-sub {{ font-size: 12px; color: #8e959e; margin-top: 4px; line-height: 1.3; }}
    div.system-list-zone div.stButton > button {{
        background-color: transparent !important; color: #8e959e !important; border: none !important;
        font-size: 20px !important; font-weight: bold !important; height: 48px !important;
        width: 100% !important; text-align: right !important; padding: 0px 8px 0px 0px !important;
        box-shadow: none !important; display: flex !important; align-items: center !important; justify-content: flex-end !important;
    }}
    
    /* 공조 장치 하단 고정 바 */
    .volvo-bottom-bar {{ display: flex; justify-content: space-between; align-items: center; background-color: #111418; padding: 14px 18px; border-radius: 12px; margin-top: 40px; border: 1px solid #232830; }}
    .bottom-item {{ font-size: 14px; font-weight: 500; color: #ffffff !important; text-align: center; }}
    .bottom-sub-label {{ font-size: 9px; color: #8e959e !important; display: block; margin-top: 2px; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- 1. 상태바 ---
st.markdown('<div class="volvo-status-bar"><span>오전 08:50</span><span>📶 LTE</span></div>', unsafe_allow_html=True)

# --- 2. 메인 탭 ---
if st.session_state.sub_page == "main":
    st.markdown('<div class="tab-zone">', unsafe_allow_html=True)
    top_col1, top_col2, top_col3 = st.columns(3)
    with top_col1:
        if st.button("퀵 컨트롤", key="tab_quick", type="primary" if st.session_state.current_tab == "퀵 컨트롤" else "secondary", use_container_width=True):
            st.session_state.current_tab = "퀵 컨트롤"; st.rerun()
    with top_col2:
        if st.button("설정", key="tab_settings", type="primary" if st.session_state.current_tab == "설정" else "secondary", use_container_width=True):
            st.session_state.current_tab = "설정"; st.rerun()
    with top_col3:
        if st.button("상태", key="tab_status", type="primary" if st.session_state.current_tab == "상태" else "secondary", use_container_width=True):
            st.session_state.current_tab = "상태"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: -10px; margin-bottom: 25px;"></div>', unsafe_allow_html=True)


# --- 3. 화면 분기 ---

# 📊 [상태] 탭
if st.session_state.current_tab == "상태" and st.session_state.sub_page == "main":
    st.markdown('<div class="status-msg-box">ⓘ 업데이트가 없습니다</div>', unsafe_allow_html=True)
    st.markdown('<div class="car-topview-container"><div class="car-visual">🚙</div></div>', unsafe_allow_html=True)
    st.write("<div style='margin-top: 45px;'></div>", unsafe_allow_html=True)
    st.markdown('<div class="status-action-zone">', unsafe_allow_html=True)
    sc1, sc2 = st.columns(2)
    with sc1: 
        if st.button("(!) 타이어 공기압", use_container_width=True): st.session_state.sub_page = "status_tire"; st.rerun()
    with sc2: 
        if st.button("📋 진단", use_container_width=True): st.session_state.sub_page = "status_diag"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ⚙️ [설정] 탭 (🎯 버튼 크기 92px 시원하게 키운 메인 화면!)
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "main":
    st.write("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
    st.markdown('<div class="volvo-setting-grid-box">', unsafe_allow_html=True)
    
    # 1행
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        if st.button("주행", key="set_drv"): st.session_state.sub_page = "driving"; st.rerun()
    with r1c2:
        if st.button("컨트롤", key="set_ctrl"): st.session_state.sub_page = "control"; st.rerun()

    st.write("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)

    # 2행
    r2c1, r2c2 = st.columns(2)
    with r2c1: st.button("사운드", key="set_snd")
    with r2c2: st.button("연결", key="set_con")

    st.write("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)

    # 3행
    r3c1, r3c2, r3c3 = st.columns(3)
    with r3c1: st.button("프로필", key="set_prf")
    with r3c2: st.button("개인정보\n보호", key="set_pvc")
    with r3c3:
        if st.button("시스템", key="set_sys"): st.session_state.sub_page = "system"; st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# [기존 서브페이지 로직 사수 - 주행/컨트롤/시스템 상세]
elif st.session_state.sub_page == "driving":
    if st.button("〈  주행"): st.session_state.sub_page = "main"; st.rerun()
    st.markdown('<div class="subpage-content-zone"><div class="volvo-title-row">운전자 지원 시스템</div></div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.session_state.pilot_assist = st.toggle("Pilot Assist 기본 설정", value=st.session_state.pilot_assist)

elif st.session_state.sub_page == "control":
    if st.button("〈  컨트롤"): st.session_state.sub_page = "main"; st.rerun()
    st.markdown('<div class="volvo-title-row">조명 및 디스플레이</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown(f'<div class="setting-title">내부 밝기 ({st.session_state.interior_brightness}%)</div>', unsafe_allow_html=True)
        st.session_state.interior_brightness = st.slider("brightness", 0, 100, st.session_state.interior_brightness, label_visibility="collapsed")
    with st.container(border=True):
        st.write("무선 장치 충전")
        st.session_state.wireless_charging = st.toggle("Wireless", value=st.session_state.wireless_charging, label_visibility="collapsed")

elif st.session_state.sub_page == "system":
    if st.button("〈  시스템"): st.session_state.sub_page = "main"; st.rerun()
    st.markdown('<div class="volvo-title-row">일반</div>', unsafe_allow_html=True)
    st.markdown('<div class="system-list-zone">', unsafe_allow_html=True)
    c1, c2 = st.columns([4.2, 0.8])
    with c1: st.markdown(f'<div class="text-container-fix"><div class="system-item-main">언어 및 입력</div><div class="system-item-sub">{st.session_state.selected_language}</div></div>', unsafe_allow_html=True)
    with c2: st.button("〉", key="s_lang")
    st.markdown('</div>', unsafe_allow_html=True)

# 📱 [퀵 컨트롤] 탭
else:
    st.write("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True) 
    m1, m2, m3 = st.columns([1, 1.3, 1])
    with m1:
        st.markdown('<div class="volvo-card-content side-btn">차선<br>유지</div>', unsafe_allow_html=True)
        st.write("<div style='margin-top:25px;'></div>")
        st.markdown('<div class="volvo-card-content side-btn">Start<br>Stop</div>', unsafe_allow_html=True)
    with m2: st.markdown('<div class="volvo-card-content center-box">VOLVO</div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="volvo-card-content side-btn">알람<br>줄이기</div>', unsafe_allow_html=True)
        st.write("<div style='margin-top:25px;'></div>")
        st.markdown('<div class="volvo-card-content side-btn">헤드<br>레스트</div>', unsafe_allow_html=True)

# --- 4. 하단 공조 바 ---
st.markdown(
    '<div class="volvo-bottom-bar">'
    '<div class="bottom-item">㗊</div>'
    '<div class="bottom-item">💺 LO</div>'
    '<div class="bottom-item">🌀<span class="bottom-sub-label">공기 재순환</span></div>'
    '<div class="bottom-item">LO 💺</div>'
    '<div class="bottom-item">🚗</div>'
    '</div>', unsafe_allow_html=True
)
