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

# [주행 설정 데이터]
if "pilot_assist" not in st.session_state: st.session_state.pilot_assist = True
if "drive_mode" not in st.session_state: st.session_state.drive_mode = "Standard"
if "steering_feel" not in st.session_state: st.session_state.steering_feel = "부드러움"
if "start_stop" not in st.session_state: st.session_state.start_stop = True
if "lane_keeping" not in st.session_state: st.session_state.lane_keeping = True
if "ready_to_drive" not in st.session_state: st.session_state.ready_to_drive = True

# [컨트롤 설정 데이터]
if "interior_brightness" not in st.session_state: st.session_state.interior_brightness = 80
if "interior_light_dim" not in st.session_state: st.session_state.interior_light_dim = "높음"
if "reduce_alarm_sensitivity" not in st.session_state: st.session_state.reduce_alarm_sensitivity = False
if "welcome_light" not in st.session_state: st.session_state.welcome_light = True
if "wireless_charging" not in st.session_state: st.session_state.wireless_charging = True

# [조명 모두 보기 추가 설정 데이터]
if "left_drive_light_adjust" not in st.session_state: st.session_state.left_drive_light_adjust = False
if "cluster_trip_info" not in st.session_state: st.session_state.cluster_trip_info = "자동"

# 🔒 [잠금 모두 보기 추가 설정 데이터]
if "unlock_mode" not in st.session_state: st.session_state.unlock_mode = "모두"
if "sunroof_curtain_auto_close" not in st.session_state: st.session_state.sunroof_curtain_auto_close = False
if "turn_signal_blink" not in st.session_state: st.session_state.turn_signal_blink = True
if "auto_fold_mirror" not in st.session_state: st.session_state.auto_fold_mirror = True

# [시스템 상세 설정 데이터]
if "sys_time_auto" not in st.session_state: st.session_state.sys_time_auto = True
if "sys_timezone_auto" not in st.session_state: st.session_state.sys_timezone_auto = True
if "sys_time_24h" not in st.session_state: st.session_state.sys_time_24h = True
if "selected_language" not in st.session_state: st.session_state.selected_language = "한국어(대한민국)"

# [NUGU Auto 전용 상태 데이터]
if "nugu_enabled" not in st.session_state: st.session_state.nugu_enabled = True
if "nugu_alarm" not in st.session_state: st.session_state.nugu_alarm = True
if "nugu_perf" not in st.session_state: st.session_state.nugu_perf = False
if "nugu_permission_clear" not in st.session_state: st.session_state.nugu_permission_clear = True

# 🔊 [사운드 전용 상태 데이터]
if "sound_focus" not in st.session_state: st.session_state.sound_focus = "모두"
if "sound_surround" not in st.session_state: st.session_state.sound_surround = True
if "sound_surround_level" not in st.session_state: st.session_state.sound_surround_level = 50

# 🎛️ 톤 설정 데이터
if "tone_treble" not in st.session_state: st.session_state.tone_treble = 50
if "tone_bass" not in st.session_state: st.session_state.tone_bass = 50
if "tone_subwoofer" not in st.session_state: st.session_state.tone_subwoofer = 50

# 📢 볼륨 설정 데이터
if "vol_media" not in st.session_state: st.session_state.vol_media = 60
if "vol_ring" not in st.session_state: st.session_state.vol_ring = 50
if "vol_call" not in st.session_state: st.session_state.vol_call = 50
if "vol_assistant" not in st.session_state: st.session_state.vol_assistant = 70
if "vol_navi" not in st.session_state: st.session_state.vol_navi = 55
if "vol_notice" not in st.session_state: st.session_state.vol_notice = 40

# 📶 [연결 전용 상태 데이터]
if "conn_wifi_enabled" not in st.session_state: st.session_state.conn_wifi_enabled = True

# 👤 [프로필 전용 상태 데이터]
if "profile_name" not in st.session_state: st.session_state.profile_name = "오너"

# 볼보 순정 다크 톤 배색 지정
bg_color = "rgb(18, 22, 28)"
card_color = "rgb(28, 34, 44)"
border_color = "rgb(42, 49, 61)"

# 내부 밝기 쿼리 파라미터 연동
if "brightness_slider" in st.query_params:
    st.session_state.interior_brightness = int(st.query_params["brightness_slider"])

# 2. 볼보 헤리티지 UI 스타일 정의
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
    
    /* 📱 퀵 컨트롤 카드 */
    .volvo-card-content {{
        background-color: rgb(22, 27, 35) !important;
        border: 1px solid {border_color} !important;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: #ffffff !important;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        width: 100%;
    }}
    .side-btn {{ height: 185px; font-size: 15px; line-height: 1.5; }}
    .center-box {{ height: 400px; font-size: 24px; letter-spacing: 5px; font-family: 'Times New Roman', Times, serif; font-weight: 400; }}

    /* 📊 상태 탭 메인 스타일 */
    .status-msg-box {{
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 17px;
        font-weight: bold;
        color: #ffffff;
        padding-top: 30px;
        padding-left: 10px;
    }}
    .status-msg-icon {{ font-size: 19px; color: #ffffff; }}
    .car-topview-container {{
        background: radial-gradient(circle at center, rgb(36, 43, 56) 0%, rgb(22, 27, 35) 70%);
        border-radius: 20px;
        height: 300px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 10px;
        box-shadow: inset 0 0 20px rgba(0,0,0,0.5);
    }}
    .car-visual {{ font-size: 90px; transform: rotate(-10deg); filter: drop-shadow(0 10px 15px rgba(0,0,0,0.6)); }}
    
    div.status-action-zone div.stButton > button {{
        background-color: rgb(34, 40, 52) !important;
        color: #ffffff !important;
        border: 1px solid #3d4656 !important;
        border-radius: 10px !important;
        height: 54px !important;
        font-size: 15px !important;
        font-weight: bold !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2) !important;
    }}

    /* ⭕ 타이어 공기압 서브뷰 컴포넌트 */
    .tire-status-header {{ display: flex; align-items: center; gap: 10px; font-size: 16px; color: #ffffff; font-weight: bold; padding: 10px 4px; }}
    .tire-check-circle-green {{
        width: 86px; height: 86px; border-radius: 50%;
        border: 3px solid #00c853; display: flex; align-items: center; justify-content: center;
        margin: 70px auto 40px auto; box-shadow: 0 0 20px rgba(0,200,83,0.2);
    }}
    .tire-check-icon-green {{ font-size: 38px; color: #00c853; font-weight: bold; }}
    .tire-bottom-notice {{ text-align: center; font-size: 13px; color: #8e959e; margin-top: 25px; font-weight: 500; }}
    .tire-blue-text {{ color: #00A3E0 !important; font-weight: bold; }}
    div.tire-action-zone div.stButton > button {{
        background-color: rgb(40, 48, 62) !important;
        color: #ffffff !important;
        border: 1px solid #4f5b72 !important;
        border-radius: 8px !important;
        height: 52px !important;
        font-size: 15px !important;
        font-weight: bold !important;
        max-width: 280px; margin: 0 auto; display: block;
    }}

    /* 🔧 진단 서브뷰 컴포넌트 */
    .diag-container {{ display: flex; flex-direction: column; width: 100%; padding: 5px 8px; }}
    .diag-row-item {{ display: flex; align-items: flex-start; gap: 18px; padding: 22px 4px; width: 100%; }}
    .diag-icon-zone {{ font-size: 26px; color: #a4aab3; width: 30px; text-align: center; padding-top: 2px; }}
    .diag-title-main {{ font-size: 17px; font-weight: bold; color: #ffffff; }}
    .diag-desc-sub {{ font-size: 14px; color: #8e959e; margin-top: 6px; font-weight: 500; }}
    .diag-divider {{ border-bottom: 1px solid #2d3542; width: 100%; margin: 2px 0; }}
    
    /* 진단 오일 상태 바 */
    .oil-bar-bg {{ background-color: #222832; border-radius: 4px; height: 8px; width: 100%; margin-top: 18px; position: relative; border: 1px solid #333c4b; }}
    .oil-bar-fill-green {{ background-color: #00c853; height: 100%; width: 84%; border-radius: 4px 0 0 4px; }}
    .oil-bar-label-row {{ display: flex; justify-content: space-between; font-size: 12px; color: #8e959e; margin-top: 6px; font-weight: bold; padding: 0 2px; }}

    /* ⚙️ 설정 메인 격자 카드 */
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
    
    /* 🛠️ 세팅 박스 타이틀 */
    .volvo-title-row {{ font-size: 14px; color: #8e959e; font-weight: bold; margin-top: 22px; margin-bottom: 12px; padding-left: 5px; }}
    
    div.subpage-content-zone div[data-testid="stVerticalBlockBorderWrapper"] {{
        background-color: rgba(18, 22, 28, 0.4) !important;
        border: 1px solid {border_color} !important;
        border-radius: 14px !important;
        padding: 18px !important;
        margin-bottom: 5px !important;
    }}
    
    .setting-title {{ font-size: 15px; font-weight: bold; color: #ffffff; margin-bottom: 4px; }}
    .setting-title-align-btn {{ font-size: 15px; font-weight: bold; color: #ffffff; padding-top: 6px; }}
    .setting-title-align-tgl {{ font-size: 15px; font-weight: bold; color: #ffffff; padding-top: 2px; }}
    .setting-desc {{ font-size: 12px; color: #8e959e; line-height: 1.4; }}
    
    /* 📋 리스트 통합 레이아웃 정렬 */
    .system-list-zone {{ display: flex; flex-direction: column; width: 100%; }}
    
    /* 텍스트 컬럼 상하 정렬 보정 */
    .text-container-fix {{
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 48px;
    }}
    .system-item-main {{ font-size: 15px; font-weight: 500; color: #ffffff; line-height: 1.2; }}
    .system-item-sub {{ font-size: 12px; color: #8e959e; margin-top: 4px; line-height: 1.3; }}
    
    /* NUGU AUTO 밑 안내 문구 스타일 */
    .app-notice-desc {{ font-size: 13px; color: #8e959e; margin-top: 6px; font-weight: normal; line-height: 1.3; }}
    
    /* 🎯 우측 화살표 버튼 크기 균일화 공통 스타일 */
    div.system-list-zone div.stButton > button {{
        background-color: transparent !important;
        color: #8e959e !important;
        border: none !important;
        font-size: 20px !important;
        font-weight: bold !important;
        height: 48px !important;
        width: 100% !important;
        text-align: right !important;
        padding: 0px 8px 0px 0px !important;
        box-shadow: none !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-end !important;
    }}
    div.system-list-zone div.stButton > button:hover {{ color: #ffffff !important; }}
    
    div.align-arrow-center div.stButton > button {{ height: 68px !important; }}
    
    /* 🔳 순정형 앱 관리 상단 버튼 스타일 */
    div.app-action-zone div.stButton > button {{
        background-color: rgb(38, 45, 56) !important;
        color: #ffffff !important;
        border: 1px solid #4a5464 !important;
        border-radius: 8px !important;
        height: 50px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        box-shadow: none !important;
    }}
    
    /* 🛡️ 권한 설정 화면 전용 커스텀 스타일 */
    .right-top-text {{ font-size: 14px; color: #8e959e; text-align: right; line-height: 38px; font-weight: 500; padding-right: 8px; }}
    .app-header-row {{ display: flex; align-items: center; padding: 10px 4px; margin-bottom: 12px; gap: 14px; }}
    .app-header-icon-custom {{ background-color: #00A3E0; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: bold; color: white; }}
    .app-header-title-custom {{ font-size: 18px; font-weight: bold; color: #ffffff; }}
    
    /* 슬라이더 스타일 */
    .slider-container-custom {{ display: flex; align-items: center; justify-content: space-between; width: 100%; padding: 5px 0; background: transparent !important; }}
    .slider-wrapper {{ position: relative; flex-grow: 1; display: flex; align-items: center; margin-right: 15px; }}
    .slider-custom {{ -webkit-appearance: none; width: 100%; height: 4px; border-radius: 2px; background: #4a525d !important; outline: none; margin: 0; }}
    .slider-custom::-webkit-slider-thumb {{ -webkit-appearance: none; appearance: none; width: 16px; height: 16px; border-radius: 50%; background: #ffffff !important; cursor: pointer; }}
    .slider-val-box {{ font-size: 16px; font-weight: bold; color: #ffffff; min-width: 35px; text-align: right; font-family: 'Helvetica Neue', sans-serif; }}

    /* 알약형 세그먼트 바 */
    div.volvo-segment-row div[data-testid="stHorizontalBlock"] {{ gap: 0px !important; background-color: #1a1f27 !important; border-radius: 25px !important; padding: 4px !important; border: 1px solid #333b46 !important; margin-top: 12px !important; }}
    div.volvo-segment-row div.stButton > button[kind="primary"] {{ background-color: #00A3E0 !important; color: #ffffff !important; border: none !important; border-radius: 22px !important; font-weight: bold !important; height: 40px !important; }}
    div.volvo-segment-row div.stButton > button[kind="secondary"] {{ background-color: transparent !important; color: #727a85 !important; border: none !important; border-radius: 22px !important; height: 40px !important; box-shadow: none !important; }}
    div.volvo-fold-btn-zone div.stButton > button {{ background-color: #383e48 !important; color: #ffffff !important; border: none !important; border-radius: 8px !important; height: 38px !important; font-size: 14px !important; font-weight: bold !important; width: 100% !important; box-shadow: none !important; }}

    div.inline-segment-fix div[data-testid="stHorizontalBlock"] {{ margin-top: 0px !important; }}

    div.right-toggle-align div[data-testid="stComponentBlock"] {{ display: flex !important; justify-content: flex-end !important; padding-top: 2px !important; }}

    .card-divider {{ border-top: 1px solid #333b46; margin-top: 20px; margin-bottom: 0px; }}
    .more-link-btn button {{ background-color: transparent !important; color: #ffffff !important; border: none !important; font-size: 14px !important; font-weight: bold !important; padding: 14px 0 12px 0 !important; box-shadow: none !important; text-align: left !important; width: 100% !important; }}

    /* 뒤로가기 버튼 박스 */
    .back-btn-box {{ display: flex; align-items: center; justify-content: space-between; width: 100%; }}
    .back-btn-box button {{ background-color: transparent !important; color: #ffffff !important; border: none !important; font-size: 18px !important; font-weight: bold !important; padding: 0 !important; box-shadow: none !important; }}
    div[data-testid="stCheckboxToggleHoverTarget"] div[aria-checked="true"] {{ background-color: #00A3E0 !important; }}

    /* 👤 순정형 프로필 원형 아바타 상단 컴포넌트 */
    .profile-avatar-row {{ display: flex; justify-content: center; align-items: center; gap: 30px; margin-top: 5px; margin-bottom: 25px; }}
    .avatar-block {{ display: flex; flex-direction: column; align-items: center; width: 65px; text-align: center; }}
    .avatar-circle-owner {{ width: 56px; height: 56px; border-radius: 50%; background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%); border: 2px solid #ffffff; box-shadow: 0 4px 10px rgba(0,0,0,0.3); }}
    .avatar-circle-guest {{ width: 56px; height: 56px; border-radius: 50%; background-color: #3d4656; display: flex; align-items: center; justify-content: center; font-size: 20px; color: #a4aab3; border: 1px solid #505b6e; }}
    .avatar-circle-add {{ width: 56px; height: 56px; border-radius: 50%; background-color: transparent; border: 1px dashed #505b6e; display: flex; align-items: center; justify-content: center; font-size: 22px; color: #8e959e; }}
    .avatar-label {{ font-size: 13px; font-weight: bold; color: #ffffff; margin-top: 8px; white-space: nowrap; }}

    /* 공조 장치 하단 고정 바 */
    .volvo-bottom-bar {{ display: flex; justify-content: space-between; align-items: center; background-color: #111418; padding: 14px 18px; border-radius: 12px; margin-top: 40px; border: 1px solid #232830; }}
    .bottom-item {{ font-size: 14px; font-weight: 500; color: #ffffff !important; text-align: center; }}
    .bottom-sub-label {{ font-size: 9px; color: #8e959e !important; display: block; margin-top: 2px; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- 1. 최상단 상태바 상시 표시 ---
st.markdown('<div class="volvo-status-bar"><span>오전 08:50</span><span>📶 LTE</span></div>', unsafe_allow_html=True)

# --- 2. 상단 메뉴 탭 (서브 메인 화면에서만 노출) ---
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
            st.session_state.current_tab = "설정"; st.session_state.sub_page = "main"; st.rerun()
    with top_col3:
        is_active = "primary" if st.session_state.current_tab == "상태" else "secondary"
        if st.button("상태", key="tab_status", type=is_active, use_container_width=True):
            st.session_state.current_tab = "상태"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: -10px; margin-bottom: 25px;"></div>', unsafe_allow_html=True)


# --- 3. 화면 분기 처리 ---

# 📊 [상태] 메인 탭 화면
if st.session_state.current_tab == "상태" and st.session_state.sub_page == "main":
    st.write("<div style='margin-top: 5px;'></div>", unsafe_allow_html=True)
    view_col1, view_col2 = st.columns([1.1, 0.9])
    with view_col1:
        st.markdown('<div class="status-msg-box"><span class="status-msg-icon">ⓘ</span><span>업데이트가 없습니다</span></div>', unsafe_allow_html=True)
    with view_col2:
        st.markdown('<div class="car-topview-container"><div class="car-visual">🚙</div></div>', unsafe_allow_html=True)
        
    st.write("<div style='margin-top: 45px;'></div>", unsafe_allow_html=True)
    
    st.markdown('<div class="status-action-zone">', unsafe_allow_html=True)
    status_btn_col1, status_btn_col2 = st.columns(2)
    with status_btn_col1:
        if st.button("(!)   타이어 공기압", key="btn_status_tire", use_container_width=True):
            st.session_state.sub_page = "status_tire"; st.rerun()
    with status_btn_col2:
        if st.button("📋   진단", key="btn_status_diag", use_container_width=True):
            st.session_state.sub_page = "status_diag"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# ⭕ [상태 -> 타이어 공기압] 상세 서브 뷰
elif st.session_state.current_tab == "상태" and st.session_state.sub_page == "status_tire":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈   타이어 공기압", key="back_to_status_main_tire"):
        st.session_state.sub_page = "main"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="tire-status-header">✔️ &nbsp; 모든 타이어 압력 정상</div>', unsafe_allow_html=True)
    st.markdown('<div class="tire-check-circle-green"><span class="tire-check-icon-green">✓</span></div>', unsafe_allow_html=True)
    st.write("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
    st.markdown('<div class="tire-action-zone">', unsafe_allow_html=True)
    st.button("기준 공기압 업데이트", key="btn_update_tire_pressure_dummy")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="tire-bottom-notice"><span class="tire-blue-text">Volvo 권장</span> 타이어 공기압 수치를 확인하십시오</div>', unsafe_allow_html=True)


# 🔧 [상태 -> 진단] 상세 서브 뷰
elif st.session_state.current_tab == "상태" and st.session_state.sub_page == "status_diag":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈   진단", key="back_to_status_main_diag"):
        st.session_state.sub_page = "main"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="diag-container">', unsafe_allow_html=True)
    st.markdown(
        '<div class="diag-row-item">'
        '<div class="diag-icon-zone">🔧</div>'
        '<div>'
        '<div class="diag-title-main">서비스 시기</div>'
        '<div class="diag-desc-sub">125 일 또는 4648 km 후</div>'
        '</div>'
        '</div>'
        '<div class="diag-divider"></div>', 
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="diag-row-item">'
        '<div class="diag-icon-zone">🛢️</div>'
        '<div style="width: 100%;">'
        '<div class="diag-title-main">오일</div>'
        '<div class="diag-desc-sub">레벨 정상</div>'
        '<div class="oil-bar-bg"><div class="oil-bar-fill-green"></div></div>'
        '<div class="oil-bar-label-row"><span>최소</span><span>최대</span></div>'
        '</div>'
        '</div>'
        '<div class="diag-divider"></div>',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)


# 🔊 [설정 -> 사운드] 메인 페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "sound":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈   사운드", key="back_to_settings_from_sound"):
        st.session_state.sub_page = "main"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="subpage-content-zone">', unsafe_allow_html=True)
    st.markdown('<div class="volvo-title-row" style="margin-top:0px;">포커스</div>', unsafe_allow_html=True)
    
    with st.container(border=True):
        selected_focus = st.radio(
            "B 포커스 선택 그룹",
            options=["모두", "운전석", "앞좌석", "뒷좌석"],
            index=["모두", "운전석", "앞좌석", "뒷좌석"].index(st.session_state.sound_focus),
            label_visibility="collapsed"
        )
        if selected_focus != st.session_state.sound_focus:
            st.session_state.sound_focus = selected_focus
            st.rerun()
            
    with st.container(border=True):
        sr_col1, sr_col2 = st.columns([3.6, 1])
        with sr_col1:
            st.markdown('<div class="setting-title" style="padding-top: 4px;">서라운드</div>', unsafe_allow_html=True)
        with sr_col2:
            st.markdown('<div class="right-toggle-align">', unsafe_allow_html=True)
            st.session_state.sound_surround = st.toggle("tgl_sound_surround", value=st.session_state.sound_surround, label_visibility="collapsed")
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-divider" style="margin-top: 15px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)
        st.session_state.sound_surround_level = st.slider("효과 강도 레벨", 0, 100, st.session_state.sound_surround_level, label_visibility="collapsed")
        
    st.write("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
    st.markdown('<div class="system-list-zone">', unsafe_allow_html=True)
    
    tone_col1, tone_col2 = st.columns([4.2, 0.8])
    with tone_col1: st.markdown('<div class="text-container-fix"><div class="system-item-main">🎛️ 톤</div></div>', unsafe_allow_html=True)
    with tone_col2:
        if st.button("〉", key="btn_sound_tone_go", use_container_width=True):
            st.session_state.sub_page = "sound_tone"; st.rerun()
    st.markdown('<div style="border-bottom: 1px solid #232830; margin: 4px 0;"></div>', unsafe_allow_html=True)
    
    vol_col1, vol_col2 = st.columns([4.2, 0.8])
    with vol_col1: st.markdown('<div class="text-container-fix"><div class="system-item-main">🔊 볼륨</div></div>', unsafe_allow_html=True)
    with vol_col2:
        if st.button("〉", key="btn_sound_volume_go", use_container_width=True):
            st.session_state.sub_page = "sound_volume"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# 🎛️ [설정 -> 사운드 -> 톤] 서브 페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "sound_tone":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈   톤", key="back_to_sound_main_from_tone"):
        st.session_state.sub_page = "sound"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="subpage-content-zone">', unsafe_allow_html=True)
    with st.container(border=True):
        t_col1, t_col2 = st.columns([1.5, 3.5])
        with t_col1: st.markdown('<div class="setting-title" style="padding-top: 8px;">고음</div>', unsafe_allow_html=True)
        with t_col2: st.session_state.tone_treble = st.slider("treble_slider", 0, 100, st.session_state.tone_treble, label_visibility="collapsed")
    with st.container(border=True):
        b_col1, b_col2 = st.columns([1.5, 3.5])
        with b_col1: st.markdown('<div class="setting-title" style="padding-top: 8px;">저음</div>', unsafe_allow_html=True)
        with b_col2: st.session_state.tone_bass = st.slider("bass_slider", 0, 100, st.session_state.tone_bass, label_visibility="collapsed")
    with st.container(border=True):
        sw_col1, sw_col2 = st.columns([1.5, 3.5])
        with sw_col1: st.markdown('<div class="setting-title" style="padding-top: 8px;">서브우퍼</div>', unsafe_allow_html=True)
        with sw_col2: st.session_state.tone_subwoofer = st.slider("subwoofer_slider", 0, 100, st.session_state.tone_subwoofer, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)


# 🔊 [설정 -> 사운드 -> 볼륨] 서브 페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "sound_volume":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈   볼륨", key="back_to_sound_main_from_volume"):
        st.session_state.sub_page = "sound"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="subpage-content-zone">', unsafe_allow_html=True)
    with st.container(border=True):
        v_col1, v_col2 = st.columns([1.8, 3.2])
        with v_col1: st.markdown('<div class="setting-title" style="padding-top: 8px;">🎵 미디어</div>', unsafe_allow_html=True)
        with v_col2: st.session_state.vol_media = st.slider("v_med", 0, 100, st.session_state.vol_media, label_visibility="collapsed")
        st.markdown('<div style="border-bottom: 1px solid #232830; margin: 10px 0;"></div>', unsafe_allow_html=True)
        v_col3, v_col4 = st.columns([1.8, 3.2])
        with v_col3: st.markdown('<div class="setting-title" style="padding-top: 8px;">📞 벨소리</div>', unsafe_allow_html=True)
        with v_col4: st.session_state.vol_ring = st.slider("v_ring", 0, 100, st.session_state.vol_ring, label_visibility="collapsed")
        st.markdown('<div style="border-bottom: 1px solid #232830; margin: 10px 0;"></div>', unsafe_allow_html=True)
        v_col5, v_col6 = st.columns([1.8, 3.2])
        with v_col5: st.markdown('<div class="setting-title" style="padding-top: 8px;">🗣️ 통화</div>', unsafe_allow_html=True)
        with v_col6: st.session_state.vol_call = st.slider("v_call", 0, 100, st.session_state.vol_call, label_visibility="collapsed")
        st.markdown('<div style="border-bottom: 1px solid #232830; margin: 10px 0;"></div>', unsafe_allow_html=True)
        v_col7, v_col8 = st.columns([1.8, 3.2])
        with v_col7: st.markdown('<div class="setting-title" style="padding-top: 8px;">🎙️ 어시스턴트</div>', unsafe_allow_html=True)
        with v_col8: st.session_state.vol_assistant = st.slider("v_ast", 0, 100, st.session_state.vol_assistant, label_visibility="collapsed")
        st.markdown('<div style="border-bottom: 1px solid #232830; margin: 10px 0;"></div>', unsafe_allow_html=True)
        v_col9, v_col10 = st.columns([1.8, 3.2])
        with v_col9: st.markdown('<div class="setting-title" style="padding-top: 8px;">🧭 내비게이션</div>', unsafe_allow_html=True)
        with v_col10: st.session_state.vol_navi = st.slider("v_nav", 0, 100, st.session_state.vol_navi, label_visibility="collapsed")
        st.markdown('<div style="border-bottom: 1px solid #232830; margin: 10px 0;"></div>', unsafe_allow_html=True)
        v_col11, v_col12 = st.columns([1.8, 3.2])
        with v_col11: st.markdown('<div class="setting-title" style="padding-top: 8px;">🔔 알림</div>', unsafe_allow_html=True)
        with v_col12: st.session_state.vol_notice = st.slider("v_not", 0, 100, st.session_state.vol_notice, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)


# 📶 [설정 -> 연결] 메인 하위 탭
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "connection":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈   연결", key="back_to_settings_from_conn"):
        st.session_state.sub_page = "main"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="subpage-content-zone">', unsafe_allow_html=True)
    st.markdown('<div class="volvo-title-row" style="margin-top:0px;">연결 설정</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown('<div class="system-list-zone">', unsafe_allow_html=True)
        bt_col1, bt_col2 = st.columns([4.2, 0.8])
        with bt_col1: st.markdown('<div class="text-container-fix"><div class="system-item-main">📱 블루투스</div></div>', unsafe_allow_html=True)
        with bt_col2:
            if st.button("〉", key="btn_conn_bluetooth_go", use_container_width=True):
                st.session_state.sub_page = "conn_bluetooth"; st.rerun()
        st.markdown('<div style="border-bottom: 1px solid #232830; margin: 8px 0;"></div>', unsafe_allow_html=True)
        wf_col1, wf_col2 = st.columns([4.2, 0.8])
        with wf_col1: st.markdown('<div class="text-container-fix"><div class="system-item-main">📶 WI-FI</div></div>', unsafe_allow_html=True)
        with wf_col2:
            if st.button("〉", key="btn_conn_wifi_go", use_container_width=True):
                st.session_state.sub_page = "conn_wifi"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# 📱 [설정 -> 연결 -> 블루투스] 서브 페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "conn_bluetooth":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈   블루투스", key="back_to_conn_main_from_bt"):
        st.session_state.sub_page = "connection"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="subpage-content-zone">', unsafe_allow_html=True)
    st.markdown('<div class="volvo-title-row" style="margin-top:0px;">저장된 기기</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown('<div class="system-list-zone">', unsafe_allow_html=True)
        btd_col1, btd_col2 = st.columns([4.2, 0.8])
        with btd_col1: st.markdown('<div class="text-container-fix"><div class="system-item-main">이밝음</div><div class="system-item-sub" style="color: #00A3E0;">연결됨</div></div>', unsafe_allow_html=True)
        with btd_col2: st.markdown('<div style="display: flex; height: 48px; align-items: center; justify-content: flex-end; font-size: 18px; padding-right: 10px;">⚙️</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="volvo-title-row">확인된 기기</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown('<div class="system-list-zone"><div class="text-container-fix" style="padding-left: 4px;"><div class="system-item-main" style="font-weight: normal;">Volvo XC40</div></div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# 📶 [설정 -> 연결 -> WI-FI] 서브 페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "conn_wifi":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈   WI-FI", key="back_to_conn_main_from_wf"):
        st.session_state.sub_page = "connection"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="subpage-content-zone">', unsafe_allow_html=True)
    st.markdown('<div class="volvo-title-row" style="margin-top:0px;">Wi-Fi 설정</div>', unsafe_allow_html=True)
    with st.container(border=True):
        wf_tcol1, wf_tcol2 = st.columns([3.8, 1.2])
        with wf_tcol1: st.markdown('<div class="setting-title" style="padding-top: 4px;">Wi-Fi 사용</div>', unsafe_allow_html=True)
        with wf_tcol2:
            st.markdown('<div class="right-toggle-align">', unsafe_allow_html=True)
            st.session_state.conn_wifi_enabled = st.toggle("tgl_conn_wifi_toggle", value=st.session_state.conn_wifi_enabled, label_visibility="collapsed")
            st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# 👤 [설정 -> 프로필 -> 프로필 설정] 상세 서브 페이지 (1번 사진 완벽 이식 - A 상단 컴포넌트 + B 타입 디테일 구조)
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "profile_settings":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈   프로필 설정", key="back_to_settings_from_profile"):
        st.session_state.sub_page = "main"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)

    # 1. 상단 아바타 그래픽 존 (오너, 게스트, 추가하기 순정 배치)
    avatar_html = """
    <div class="profile-avatar-row">
        <div class="avatar-block">
            <div class="avatar-circle-owner"></div>
            <div class="avatar-label">오너</div>
        </div>
        <div class="avatar-block">
            <div class="avatar-circle-guest">👤</div>
            <div class="avatar-label" style="color: #8e959e;">게스트</div>
        </div>
        <div class="avatar-block">
            <div class="avatar-circle-add">＋</div>
            <div class="avatar-label" style="color: #8e959e;">추가하기</div>
        </div>
    </div>
    """
    st.markdown(avatar_html, unsafe_allow_html=True)

    # 2. 하단 리스트 설정 구역 (B 타입: 개별 큰 테두리 박스 적용)
    st.markdown('<div class="volvo-title-row">프로필 설정</div>', unsafe_allow_html=True)
    st.markdown('<div class="subpage-content-zone">', unsafe_allow_html=True)
    
    # 항목 1: 프로필 이름 (오측 에디트 아이콘)
    with st.container(border=True):
        st.markdown('<div class="system-list-zone">', unsafe_allow_html=True)
        p_col1, p_col2 = st.columns([4.2, 0.8])
        with p_col1:
            st.markdown(f'<div class="text-container-fix"><div class="system-item-main">프로필 이름</div><div class="system-item-sub" style="font-size: 15px; color: #ffffff; opacity: 0.9;">{st.session_state.profile_name}</div></div>', unsafe_allow_html=True)
        with p_col2:
            st.markdown('<div style="display: flex; height: 48px; align-items: center; justify-content: flex-end; font-size: 18px; padding-right: 6px;">📝</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    # 항목 2: Volvo Cars 앱
    with st.container(border=True):
        st.markdown('<div class="system-list-zone">', unsafe_allow_html=True)
        p_col3, p_col4 = st.columns([4.2, 0.8])
        with p_col3:
            st.markdown('<div class="text-container-fix"><div class="system-item-main">Volvo Cars 앱</div><div class="system-item-sub">커넥티드 서비스를 사용하시려면 차량 소유자로 등록하세요</div></div>', unsafe_allow_html=True)
        with p_col4:
            st.button("〉", key="btn_prof_volvo_app", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    # 항목 3: 차량 키
    with st.container(border=True):
        st.markdown('<div class="system-list-zone">', unsafe_allow_html=True)
        p_col5, p_col6 = st.columns([4.2, 0.8])
        with p_col5:
            st.markdown('<div class="text-container-fix"><div class="system-item-main">차량 키</div><div class="system-item-sub">키 연결 및 관리</div></div>', unsafe_allow_html=True)
        with p_col6:
            st.button("〉", key="btn_prof_car_key", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    # 항목 4: 프로필 잠금
    with st.container(border=True):
        st.markdown('<div class="system-list-zone">', unsafe_allow_html=True)
        p_col7, p_col8 = st.columns([4.2, 0.8])
        with p_col7:
            st.markdown('<div class="text-container-fix"><div class="system-item-main">프로필 잠금</div><div class="system-item-sub">프로필 접속 제한</div></div>', unsafe_allow_html=True)
        with p_col8:
            st.button("〉", key="btn_prof_lock", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    # 항목 5: 다른 프로필 관리
    with st.container(border=True):
        st.markdown('<div class="system-list-zone">', unsafe_allow_html=True)
        p_col9, p_col10 = st.columns([4.2, 0.8])
        with p_col9:
            st.markdown('<div class="text-container-fix" style="min-height:36px;"><div class="system-item-main">다른 프로필 관리</div></div>', unsafe_allow_html=True)
        with p_col10:
            st.button("〉", key="btn_prof_manage_other", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# 🚗 [설정 -> 주행] 서브 페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "driving":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈   주행", key="back_to_settings"):
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
    st.markdown('<div class="volvo-title-row">주행 역학</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown('<div class="setting-title">주행 모드</div><div class="setting-desc">모든 종류의 일상 주행 시 효율성을 위해 가속, 주행 역학 및 조향이 최적화됩니다.</div>', unsafe_allow_html=True)
        st.markdown('<div class="volvo-segment-row">', unsafe_allow_html=True)
        dm_col1, dm_col2 = st.columns(2)
        with dm_col1:
            dm_type = "primary" if st.session_state.drive_mode == "Standard" else "secondary"
            if st.button("Standard", key="btn_seg_std", type=dm_type, use_container_width=True): st.session_state.drive_mode = "Standard"; st.rerun()
        with dm_col2:
            dm_type = "primary" if st.session_state.drive_mode == "Off-road" else "secondary"
            if st.button("Off-road", key="btn_seg_off", type=dm_type, use_container_width=True): st.session_state.drive_mode = "Off-road"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown('<div class="setting-title">스티어링 감도</div>', unsafe_allow_html=True)
        st.markdown('<div class="volvo-segment-row">', unsafe_allow_html=True)
        sf_col1, sf_col2 = st.columns(2)
        with sf_col1:
            sf_type = "primary" if st.session_state.steering_feel == "부드러움" else "secondary"
            if st.button("부드러움", key="btn_seg_sf1", type=sf_type, use_container_width=True): st.session_state.steering_feel = "부드러움"; st.rerun()
        with sf_col2:
            sf_type = "primary" if st.session_state.steering_feel == "단단함" else "secondary"
            if st.button("단단함", key="btn_seg_sf2", type=sf_type, use_container_width=True): st.session_state.steering_feel = "단단함"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with st.container(border=True):
        ss_col1, ss_col2 = st.columns([3.6, 1])
        with ss_col1: st.markdown('<div class="setting-title">Start/Stop</div><div class="setting-desc">정지 시 일시적으로 엔진을 끕니다. 새로 주행할 때마다 켜짐으로 재설정됩니다.</div>', unsafe_allow_html=True)
        with ss_col2:
            st.write("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
            st.session_state.start_stop = st.toggle("SS_tgl", value=st.session_state.start_stop, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)


# 🎛️ [설정 -> 컨트롤] 서브 페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "control":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈   컨트롤", key="back_to_settings_ctrl"):
        st.session_state.sub_page = "main"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="subpage-content-zone">', unsafe_allow_html=True)
    st.markdown('<div class="volvo-title-row">조명 및 디스플레이</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown('<div class="setting-title">내부 밝기</div>', unsafe_allow_html=True)
        slider_html = f"""
        <div class="slider-container-custom" style="padding: 0; margin: 0;">
            <div class="slider-wrapper"><input type="range" min="0" max="100" value="{st.session_state.interior_brightness}" class="slider-custom" id="brightnessRange" style="width: 100%;" oninput="document.getElementById('sliderVal').innerText = this.value"></div>
            <div class="slider-val-box" id="sliderVal">{st.session_state.interior_brightness}</div>
        </div>
        <script>
        var slider = document.getElementById("brightnessRange");
        slider.addEventListener("change", function() {{ window.parent.postMessage({{ type: "streamlit:set_query_params", queryParams: {{"brightness_slider": this.value}} }}, "*"); }});
        </script>
        """
        st.components.v1.html(slider_html, height=35)
        st.write("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
        st.markdown('<div class="setting-title">내부 조명 감도</div>', unsafe_allow_html=True)
        st.markdown('<div class="volvo-segment-row">', unsafe_allow_html=True)
        dim_col1, dim_col2, dim_col3 = st.columns(3)
        with dim_col1:
            t_type = "primary" if st.session_state.interior_light_dim == "끄기" else "secondary"
            if st.button("끄기", key="btn_dim_off", type=t_type, use_container_width=True): st.session_state.interior_light_dim = "끄기"; st.rerun()
        with dim_col2:
            t_type = "primary" if st.session_state.interior_light_dim == "낮음" else "secondary"
            if st.button("낮음", key="btn_dim_low", type=t_type, use_container_width=True): st.session_state.interior_light_dim = "낮음"; st.rerun()
        with dim_col3:
            t_type = "primary" if st.session_state.interior_light_dim == "높음" else "secondary"
            if st.button("높음", key="btn_dim_high", type=t_type, use_container_width=True): st.session_state.interior_light_dim = "높음"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="more-link-btn">', unsafe_allow_html=True)
        if st.button("모두 보기                      〉", key="btn_go_lighting_all"): st.session_state.sub_page = "ctrl_lighting_all"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# 💡 [설정 -> 컨트롤 -> 조명 및 디스플레이 -> 모두 보기] 서브 페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "ctrl_lighting_all":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈   조명 및 디스플레이", key="back_to_control_main"): st.session_state.sub_page = "control"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="subpage-content-zone">', unsafe_allow_html=True)
    st.markdown('<div class="volvo-title-row">내부 조명</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown('<div class="setting-title">내부 밝기</div>', unsafe_allow_html=True)
        slider_html = f"""
        <div class="slider-container-custom" style="padding: 0; margin: 0;">
            <div class="slider-wrapper"><input type="range" min="0" max="100" value="{st.session_state.interior_brightness}" class="slider-custom" id="brightnessRangeAll" style="width: 100%;" oninput="document.getElementById('sliderValAll').innerText = this.value"></div>
            <div class="slider-val-box" id="sliderValAll">{st.session_state.interior_brightness}</div>
        </div>
        <script>
        var slider = document.getElementById("brightnessRangeAll");
        slider.addEventListener("change", function() {{ window.parent.postMessage({{ type: "streamlit:set_query_params", queryParams: {{"brightness_slider": this.value}} }}, "*"); }});
        </script>
        """
        st.components.v1.html(slider_html, height=35)
    st.markdown('</div>', unsafe_allow_html=True)


# 🔒 [설정 -> 컨트롤 -> 잠금 -> 모두 보기] 서브 페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "ctrl_lock_all":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈   잠금", key="back_to_control_main_lock"): st.session_state.sub_page = "control"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)


# 💻 [설정 -> 시스템] 메인 리스트 탭
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "system":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈   시스템", key="back_to_settings_sys"): st.session_state.sub_page = "main"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="volvo-title-row">일반</div>', unsafe_allow_html=True)
    st.markdown('<div class="system-list-zone">', unsafe_allow_html=True)
    c1, c2 = st.columns([4.2, 0.8])
    with c1: st.markdown(f'<div class="text-container-fix"><div class="system-item-main">언어 및 입력</div><div class="system-item-sub">{st.session_state.selected_language}</div></div>', unsafe_allow_html=True)
    with c2:
        if st.button("〉", key="main_sys_lang", use_container_width=True): st.session_state.sub_page = "sys_language"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# 🌐 [시스템 -> 상세 1. 언어 및 입력] 상세페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "sys_language":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈   언어 및 입력", key="back_to_sys_main_1"): st.session_state.sub_page = "system"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# ⏰ [시스템 -> 상세 2. 날짜 및 시간] 상세페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "sys_datetime":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈   날짜 및 시간", key="back_to_sys_main_2"): st.session_state.sub_page = "system"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# 📱 [시스템 -> 상세 3. 애플리케이션 (기본 앱 목록)] 상세페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "sys_apps":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈   애플리케이션", key="back_to_sys_main_3"): st.session_state.sub_page = "system"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# 🔍 [시스템 -> 애플리케이션 -> NUGU Auto 앱 정보] 세부 페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "sys_nugu_info":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈   앱 정보", key="back_to_sys_apps"): st.session_state.sub_page = "sys_apps"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# 🛡️ [시스템 -> 애플리케이션 -> NUGU Auto -> 앱 권한] 세부 설정 뷰
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "sys_nugu_permissions":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈   앱 권한", key="back_to_nugu_info"): st.session_state.sub_page = "sys_nugu_info"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# ⚙️ [설정] 메인 격자 맵 화면
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "main":
    st.write("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
        if st.button("주행", key="btn_drive_go", use_container_width=True): st.session_state.sub_page = "driving"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with row1_col2:
        st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
        if st.button("컨트롤", key="btn_control_go", use_container_width=True): st.session_state.sub_page = "control"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
        if st.button("사운드", key="btn_sound_go", use_container_width=True): st.session_state.sub_page = "sound"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with row2_col2:
        st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
        if st.button("연결", key="btn_connect_go", use_container_width=True): st.session_state.sub_page = "connection"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    row3_col1, row3_col2, row3_col3 = st.columns(3)
    with row3_col1:
        st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
        # 🎯 프로필 버튼 클릭 시 [설정 -> 프로필 설정] 상세 서브 페이지로 라우팅!
        if st.button("프로필", key="btn_profile_go", use_container_width=True):
            st.session_state.sub_page = "profile_settings"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with row3_col2:
        st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
        st.button("개인정보\n보호", key="btn_privacy_go", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with row3_col3:
        st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
        if st.button("시스템", key="btn_system_go", use_container_width=True): st.session_state.sub_page = "system"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)


# 📱 [퀵 컨트롤] 탭 구조 보존
else:
    st.write("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True) 
    main_col1, main_col2, main_col3 = st.columns([1, 1.3, 1])
    with main_col1:
        st.markdown('<div class="volvo-card-content side-btn">차선<br>유지</div>', unsafe_allow_html=True)
        st.write("<div style='margin-top:25px;'></div>", unsafe_allow_html=True)
        st.markdown('<div class="volvo-card-content side-btn">Start<br>Stop</div>', unsafe_allow_html=True)
    with main_col2: st.markdown('<div class="volvo-card-content center-box">VOLVO</div>', unsafe_allow_html=True)
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
