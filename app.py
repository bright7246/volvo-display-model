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
    st.session_state.current_tab = "퀵 컨트롤"

# 볼보 순정 느낌의 고급스러운 고정 다크 톤 배색 지정
bg_color = "rgb(18, 22, 28)"
card_color = "rgb(28, 34, 44)"
border_color = "rgb(42, 49, 61)"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {bg_color} !important;
        color: #ffffff !important;
    }}
    
    /* 💡 전체 세로 길이를 시원하게 뽑기 위해 최대 너비와 최소 세로 높이 최적화 */
    .block-container {{
        max-width: 480px !important;
        padding-top: 2rem !important; 
        padding-bottom: 3rem !important;
        margin: 0 auto;
        min-height: 850px; 
    }}
    
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
    .stButton > button {{
        background-color: transparent !important;
        color: #8e959e !important;
        border: none !important;
        font-size: 15px !important;
        font-weight: 500 !important;
        padding: 8px 0 !important;
        width: 100% !important;
        box-shadow: none !important;
    }}
    .stButton > button[kind="primary"] {{
        color: #ffffff !important;
        font-weight: bold !important;
        border-bottom: 3px solid #ffffff !important;
    }}
    
    /* 📱 퀵 컨트롤 전용 카드 디자인 - 세로 길이 대폭 확장 */
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
    .side-btn {{
        height: 185px; /* 140px -> 185px로 늘려서 위아래 꽉 차게 변경 */
        font-size: 15px;
        line-height: 1.5;
    }}
    .center-box {{
        height: 400px; /* 300px -> 400px로 대폭 늘려 메인 존재감 확보 */
        font-size: 24px;
        letter-spacing: 5px;
        font-family: 'Times New Roman', Times, serif;
        font-weight: 400;
    }}
    
    /* ⚙️ 설정 탭 전용 카드 디자인 */
    .volvo-set-card {{
        background-color: {card_color} !important;
        border: 1px solid {border_color} !important;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: #ffffff !important;
        font-weight: bold;
        font-size: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        width: 100%;
        height: 125px; 
        margin-bottom: 18px; 
    }}
    
    /* 하단 바 디자인 */
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
    .bottom-item {{
        font-size: 14px;
        font-weight: 500;
        color: #ffffff !important;
        text-align: center;
    }}
    .bottom-sub-label {{
        font-size: 9px;
        color: #8e959e !important;
        display: block;
        margin-top: 2px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- 1. 최상단 상태바 ---
utc_now = datetime.utcnow()
kor_now = utc_now + timedelta(hours=9)
ampm = "오후" if kor_now.hour >= 12 else "오전"
display_hour = kor_now.hour % 12
display_hour = 12 if display_hour == 0 else display_hour
time_string = f"{ampm} {display_hour:02d}:{kor_now.minute:02d}"

st.markdown(
    f'<div class="volvo-status-bar"><span>{time_string}</span><span>📶 LTE</span></div>', 
    unsafe_allow_html=True
)

# --- 2. 상단 메뉴 탭 ---
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

st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: -10px; margin-bottom: 25px;"></div>', unsafe_allow_html=True)


# --- 3. 화면 분기 처리 ---

# ⚙️ [설정] 탭 내용
if st.session_state.current_tab == "설정":
    st.write("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

    # 1라인: 주행 / 컨트롤
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        st.markdown('<div class="volvo-set-card">주행</div>', unsafe_allow_html=True)
    with row1_col2:
        st.markdown('<div class="volvo-set-card">컨트롤</div>', unsafe_allow_html=True)

    # 2라인: 사운드 / 연결
    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        st.markdown('<div class="volvo-set-card">사운드</div>', unsafe_allow_html=True)
    with row2_col2:
        st.markdown('<div class="volvo-set-card">연결</div>', unsafe_allow_html=True)

    # 3라인: 프로필 / 개인정보 보호 / 시스템
    row3_col1, row3_col2, row3_col3 = st.columns([1, 1.2, 1])
    with row3_col1:
        st.markdown('<div class="volvo-set-card" style="font-size: 14px;">프로필</div>', unsafe_allow_html=True)
    with row3_col2:
        st.markdown('<div class="volvo-set-card" style="font-size: 14px;">개인정보<br>보호</div>', unsafe_allow_html=True)
    with row3_col3:
        st.markdown('<div class="volvo-set-card" style="font-size: 14px;">시스템</div>', unsafe_allow_html=True)

# 📊 [상태] 탭 내용
elif st.session_state.current_tab == "상태":
    st.subheader("📊 차량 상태")
    st.write("차량 진단 및 정보를 확인합니다.")

# 📱 [퀵 컨트롤] 탭 내용 (기본값)
else:
    st.write("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True) 
    main_col1, main_col2, main_col3 = st.columns([1, 1.3, 1])

    # 💡 세로 길이를 시원하게 늘리고 버튼 간 격차 조절을 위한 margin-bottom 최적화
    with main_col1:
        st.markdown('<div class="volvo-card-content side-btn">차선<br>유지</div>', unsafe_allow_html=True)
        st.write("<div style='margin-bottom: 30px;'></div>", unsafe_allow_html=
