import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="Volvo Main Display",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. 볼보 UI의 세로형 비율과 버튼 디자인을 위한 CSS 설정
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1a1e24;
        color: #ffffff;
    }
    .block-container {
        max-width: 450px !important;
        padding-top: 1.5rem;
        padding-bottom: 1.5rem;
        margin: 0 auto;
    }
    .volvo-status-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 13px;
        color: #e1e2e3;
        padding: 5px 10px;
        margin-bottom: 5px;
    }
    .stButton > button {
        background-color: transparent !important;
        color: #8e959e !important;
        border: none !important;
        font-size: 15px !important;
        font-weight: 500 !important;
        padding: 8px 0 !important;
        width: 100% !important;
        border-radius: 0px !important;
        box-shadow: none !important;
    }
    .stButton > button[kind="primary"] {
        color: #ffffff !important;
        font-weight: bold !important;
        border-bottom: 3px solid #ffffff !important;
    }
    .volvo-main-grid {
        display: flex;
        justify-content: space-between;
        align-items: center; 
        margin: 30px 0;
        min-height: 240px;
        width: 100%;
    }
    .grid-column {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 30%;
    }
    .volvo-circle-btn {
        width: 65px;
        height: 65px;
        background-color: #383e47; 
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 11px; 
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        line-height: 1.3;
    }
    .btn-bottom-label {
        font-size: 11px;
        color: #8e959e;
        margin-top: 6px;
        text-align: center;
        white-space: nowrap;
    }
    .center-volvo-container {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 40%;
    }
    .center-volvo-text {
        font-size: 36px;
        font-weight: 300;
        color: #ffffff;
        letter-spacing: 6px;
        font-family: 'Times New Roman', Times, serif;
        text-align: center;
    }
    .volvo-bottom-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #111418;
        padding: 10px 15px;
        border-radius: 10px;
        margin-top: 40px;
        border: 1px solid #232830;
    }
    .bottom-item {
        font-size: 14px;
        font-weight: 500;
        color: #ffffff;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .bottom-sub-label {
        font-size: 9px;
        color: #8e959e;
        display: block;
        margin-top: 1px;
    }
    .bottom-setting-circle {
        width: 38px;
        height: 38px;
        background-color: #383e47;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 11px;
        font-weight: bold;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 세션 상태 초기화
if "current_tab" not in st.session_state:
    st.session_state.current_tab = "퀵 컨트롤"

# --- 1. 최상단 상태바 ---
st.markdown('<div class="volvo-status-bar"><span>오전 08:46</span><span>📶 LTE</span></div>', unsafe_allow_html=True)

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

# 구분선
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
    # 밝기 조절 슬라이더
    st.slider("☀️ 밝기 조절", min_value=0, max_value=100, value=85)

    # 💡 스트림릿 오작동 방지를 위해 문자열의 모든 들여쓰기를 제거하여 한 줄로 붙여넣었습니다.
    main_html = (
        '<div class="volvo-main-grid">'
        '<div class="grid-column">'
        '<div style="margin-bottom: 25px; display: flex; flex-direction: column; align-items: center;"><div class="volvo-circle-btn">차선<br>유지</div><div class="btn-bottom-label">차선유지 보조</div></div>'
        '<div style="display: flex; flex-direction: column; align-items: center;"><div class="volvo-circle-btn">S / S</div><div class="btn-bottom-label">Start/Stop</div></div>'
        '</div>'
        '<div class="center-volvo-container"><div class="center-volvo-text">VOLVO</div></div>'
        '<div class="grid-column">'
        '<div style="margin-bottom: 25px; display: flex; flex-direction: column; align-items: center;"><div class="volvo-circle-btn">알람<br>줄이기</div><div class="btn-bottom-label">알람 줄이기</div></div>'
        '<div style="display: flex; flex-direction: column; align-items: center;"><div class="volvo-circle-btn">헤드<br>레스트</div><div class="btn-bottom-label">헤드레스트 접기</div></div>'
        '</div>'
        '</div>'
    )
    st.markdown(main_html, unsafe_allow_html=True)

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
