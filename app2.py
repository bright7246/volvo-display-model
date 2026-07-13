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
