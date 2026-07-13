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

# 💡 볼보 순정 느낌의 고급스러운 고정 다크 톤 배색 지정
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
    .block-container {{
        max-width: 450px !important;
        padding-top: 2.5rem !important; 
        padding-bottom: 1.5rem;
        margin: 0 auto;
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
        margin-bottom: 20px;
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
    
    /* 볼보 스타일 카드 내부 텍스트 및 박스 디자인 */
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
        height: 130px;
        font-size: 14px;
        line-height: 1.4;
    }}
    .center-box {{
        height: 280px;
        font-size: 24px;
        letter-spacing: 5px;
        font-family: 'Times New Roman', Times, serif;
        font-weight: 400;
    }}
    
    /* 하단 바 디자인 */
    .volvo-bottom-bar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #111418;
        padding: 12px 18px;
        border-radius: 12px;
        margin-top: 40px;
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
    .bottom-setting-circle {{
        width: 38px;
        height: 38px;
        background-color: #383e47;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 11px;
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- 1. 최상단 상태바 (한국시간 기준) ---
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

st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: -10px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)


# --- 3. 화면 분기 처리 ---
if st.session_state.current_tab == "설정":
    st.subheader("⚙️ 볼보 시스템 설정")
    st.write("차량 시스템 옵션 설정 페이지입니다.")
    if st.button("⬅️ 메인 화면으로 돌아가기"):
        st.session_state.current_tab = "퀵 컨트롤"
        st.rerun()

elif st.session_state.current_tab == "상태":
    st.subheader("📊 차량 상태")
    st.write("차량 진단 및 정보를 확인합니다.")

else:
    # 💡 복잡했던 슬라이더 및 여백 초기화
    st.write("") 

    # 순수 스트림릿 컬럼 레이아웃으로 완벽 배치
    main_col1, main_col2, main_col3 = st.columns([1, 1.3, 1])

    # 좌측 버튼 레이아웃
    with main_col1:
        st.markdown('<div class="volvo-card-content side-btn">차선<br>유지</div>', unsafe_allow_html=True)
        st.write("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True) 
        st.markdown('<div class="volvo-card-content side-btn">Start<br>Stop</div>', unsafe_allow_html=True)

    # 중앙 VOLVO 긴 세로 박스
    with main_col2:
        st.markdown('<div class="volvo-card-content center-box">VOLVO</div>', unsafe_allow_html=True)

    # 우측 버튼 레이아웃
    with main_col3:
        st.markdown('<div class="volvo-card-content side-btn">알람<br>줄이기</div>', unsafe_allow_html=True)
        st.write("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)
        st.markdown('<div class="volvo-card-content side-btn">헤드<br>레스트</div>', unsafe_allow_html=True)

    # --- 4. 하단 공조 장치 바 ---
    bottom_html = (
        '<div class="volvo-bottom-bar">'
        '<div class="bottom-item" style="color: #8e959e; font-size: 16px;">㗊</div>'
        '<div class="bottom-item">💺 LO</div>'
        '<div class="bottom-item"><span style="font-size: 16px;">🌀</span><span class="bottom-sub-label">공기 재순환</span></div>'
        '<div class="bottom-item">LO 💺</div>'
        '<div class="bottom-item"><div class="bottom-setting-circle">설정</div></div>'
        '</div>'
    )
    st.markdown(bottom_html, unsafe_allow_html=True)
