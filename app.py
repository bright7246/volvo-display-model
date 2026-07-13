import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="Volvo Main Display",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. 볼보 UI의 세로형 사각형 박스 레이아웃을 위한 CSS 설정
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
    
    /* 💡 1. 상단 상태 바 글자색을 밝게 수정하여 확실히 보이도록 조치 */
    .volvo-status-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 13px;
        color: #ffffff !important; /* 선명한 흰색 */
        font-weight: 500;
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
    
    /* 중앙 그리드 설정 */
    .volvo-main-grid {
        display: flex;
        justify-content: space-between;
        align-items: center; 
        margin: 30px 0;
        min-height: 280px;
        width: 100%;
    }
    .grid-column {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 32%;
    }
    
    /* 💡 2. 동그라미를 세로가 길쭉한 사각형 박스(가로2:세로3 비율)로 변경 */
    .volvo-rect-btn {
        width: 90px;
        height: 125px;
        background-color: #252b35; /* 살짝 밝은 차콜그레이 박스 */
        border: 1px solid #323945; /* 은은한 테두리 */
        border-radius: 12px; /* 모서리 부드럽게 */
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 13px; 
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        line-height: 1.4;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    
    /* 💡 3. 중앙 VOLVO 텍스트도 비슷한 사각형 박스 형태로 감싸기 */
    .center-volvo-box {
        width: 110px;
        height: 270px; /* 양옆 사각형 2개를 합친 높이와 밸런스를 맞춤 */
        background-color: #1e232b;
        border: 1px solid #2d3440;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .center-volvo-text {
        font-size: 26px;
        font-weight: 300;
        color: #ffffff;
        letter-spacing: 4px;
        font-family: 'Times New Roman', Times, serif;
        transform: rotate(0deg); /* 필요시 세로 정렬 회전 가능 */
        text-align: center;
    }
    
    .btn-bottom-label {
        font-size: 11px;
        color: #8e959e;
        margin-top: 8px;
        text-align: center;
        white-space: nowrap;
    }
    
    /* 하단 공조바 */
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

# --- 1. 최상단 상태바 (보이도록 폰트 컬러 최적화) ---
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

    # 중앙 메인 레이아웃 (세로형 사각형 카드 격자화)
    main_html = (
        '<div class="volvo-main-grid">'
        ''
        '<div class="grid-column">'
        '<div style="margin-bottom: 20px; display: flex; flex-direction: column; align-items: center;"><div class="volvo-rect-btn">차선<br>유지</div><div class="btn-bottom-label">차선유지 보조</div></div>'
        '<div style="display: flex; flex-direction: column; align-items: center;"><div class="volvo-rect-btn">Start<br>Stop</div><div class="btn-bottom-label">Start/Stop</div></div>'
        '</div>'
        
        ''
        '<div class="center-volvo-box">'
        '<div class="center-volvo-text">V<br>O<br>L<br>V<br>O</div>'
        '</div>'
        
        ''
        '<div class="grid-column">'
        '<div style="margin-bottom: 20px; display: flex; flex-direction: column; align-items: center;"><div class="volvo-rect-btn">알람<br>줄이기</div><div class="btn-bottom-label">알람 줄이기</div></div>'
        '<div style="display: flex; flex-direction: column; align-items: center;"><div class="volvo-rect-btn">헤드<br>레스트</div><div class="btn-bottom-label">헤드레스트 접기</div></div>'
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
