import streamlit as st
from datetime import datetime

# 1. 페이지 설정
st.set_page_config(
    page_title="Volvo Main Display",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 세션 상태 초기화
if "current_tab" not in st.session_state: st.session_state.current_tab = "설정"
if "sub_page" not in st.session_state: st.session_state.sub_page = "main"

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

# 쿼리 파라미터 연동 (안전하게 가져오기)
if "brightness_slider" in st.query_params:
    try:
        st.session_state.interior_brightness = int(st.query_params["brightness_slider"])
    except ValueError:
        pass

# 볼보 순정 다크 톤 배색 지정
bg_color = "rgb(18, 22, 28)"
card_color = "rgb(28, 34, 44)"
border_color = "rgb(42, 49, 61)"

# 2. 볼보 헤리티지 UI 스타일 정의 (</style> 태그 누락 수정)
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
    </style>
    """,
    unsafe_allow_html=True,
)

# --- 3. 실제 화면에 그려지는 UI 영역 (예시) ---

# 상단 상태바
current_time = datetime.now().strftime("%H:%M")
st.markdown(
    f"""
    <div class="volvo-status-bar">
        <span>LTE</span>
        <span>{current_time}</span>
        <span>22.0 °C</span>
    </div>
    """, 
    unsafe_allow_html=True
)

# 메인 레이아웃 구성
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.markdown('<div class="volvo-card-content side-btn"><div>왼쪽<br>컨트롤</div></div>', unsafe_allow_html=True)
    if st.button("파일럿 어시스트", use_container_width=True):
        st.session_state.pilot_assist = not st.session_state.pilot_assist

with col2:
    st.markdown('<div class="volvo-card-content center-box"><div>VOLVO</div></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="volvo-card-content side-btn"><div>오른쪽<br>컨트롤</div></div>', unsafe_allow_html=True)
    st.toggle("무선 충전", value=st.session_state.wireless_charging)
