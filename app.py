import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="Volvo Main Display",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. 볼보 UI 스타일을 맞추기 위한 CSS 커스텀
st.markdown(
    """
    <style>
    /* 전체 배경색: 볼보 특유의 짙은 네이비/차콜 블랙 */
    .stApp {
        background-color: #1a1e24;
        color: #ffffff;
    }
    
    /* 기본 스트림릿 여백 줄이기 */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* 상단 상태 바 스타일 */
    .volvo-status-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 14px;
        color: #e1e2e3;
        padding: 5px 10px;
        margin-bottom: 10px;
    }

    /* 스트림릿 기본 버튼 스타일 초기화 및 볼보 탭 메뉴화 */
    .stButton > button {
        background-color: transparent !important;
        color: #8e959e !important;
        border: none !important;
        font-size: 16px !important;
        font-weight: 500 !important;
        padding: 10px 0 !important;
        width: 100% !important;
        border-radius: 0px !important;
        box-shadow: none !important;
    }
    
    /* 활성화된 탭 스타일 (흰색 글씨 + 하단 흰색 밑줄) */
    .stButton > button[kind="primary"] {
        color: #ffffff !important;
        font-weight: bold !important;
        border-bottom: 3px solid #ffffff !important;
    }

    .stButton > button:hover {
        background-color: transparent !important;
        color: #ffffff !important;
    }

    /* 슬라이더 스타일 */
    div[data-testid="stSlider"] {
        padding-top: 10px;
        padding-bottom: 20px;
    }

    /* 텍스트형 원형 버튼 컨테이너 */
    .volvo-btn-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin: 25px 0;
        text-align: center;
    }

    /* 파란색 활성화 원형 (그림 없이 빈 원 또는 은은한 배경만) */
    .icon-circle-blue {
        width: 60px;
        height: 60px;
        background-color: #00a0e9;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 8px;
    }

    /* 회색 비활성화 원형 */
    .icon-circle-grey {
        width: 60px;
        height: 60px;
        background-color: #383e47;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 8px;
    }

    .btn-label {
        font-size: 14px;
        color: #e1e2e3;
        font-weight: 500;
        margin-top: 4px;
    }

    /* 중앙 대형 VOLVO 텍스트 스타일 */
    .center-volvo-text {
        text-align: center;
        font-size: 45px;
        font-weight: 300;
        color: #ffffff;
        letter-spacing: 8px;
        padding: 40px 0;
        font-family: 'Times New Roman', Times, serif;
    }

    /* 하단 공조장치 바 디자인 */
    .volvo-bottom-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #111418;
        padding: 15px 20px;
        border-radius: 10px;
        margin-top: 40px;
        border: 1px solid #232830;
    }

    .bottom-item {
        font-size: 15px;
        font-weight: 500;
        color: #ffffff;
        text-align: center;
    }
    
    .bottom-sub-label {
        font-size: 10px;
        color: #8e959e;
        display: block;
        margin-top: 2px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 세션 상태 초기화
if "current_tab" not in st.session_state:
    st.session_state.current_tab = "퀵 컨트롤"

# --- 1. 최상단 상태바 ---
st.markdown(
    '''
    <div class="volvo-status-bar">
        <span>오전 08:46</span>
        <span>📶 LTE</span>
    </div>
    ''', 
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

# 구분선
st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: -10px; margin-bottom: 20px;"></div>', unsafe_allow_html=True)


# --- 3. 화면 분기 처리 ---

if st.session_state.current_tab == "설정":
    st.subheader("⚙️ 볼보 시스템 설정")
    st.write("다양한 차량 옵션을 설정할 수 있는 페이지입니다.")
    if st.button("⬅️ 메인 화면(퀵 컨트롤)으로 돌아가기"):
        st.session_state.current_tab = "퀵 컨트롤"
        st.rerun()

elif st.session_state.current_tab == "상태":
    st.subheader("📊 차량 상태")
    st.write("차량의 현재 상태 및 진단 정보를 확인합니다.")

else:
    # 밝기 조절 슬라이더
    st.slider("☀️ 밝기 조절", min_value=0, max_value=100, value=85)

    # 중앙 레이아웃 (그림 없이 글자만 남김)
    main_col1, main_col2, main_col3 = st.columns([1, 1.2, 1])

    # 좌측 영역 (그림 지우고 깔끔한 원과 글자만)
    with main_col1:
        st.markdown(
            '''
            <div class="volvo-btn-container">
                <div class="icon-circle-blue"></div>
                <div class="btn-label">차선유지 보조</div>
            </div>
            <div class="volvo-btn-container">
                <div class="icon-circle-blue"></div>
                <div class="btn-label">Start/Stop</div>
            </div>
            ''', unsafe_allow_html=True
        )

    # 중앙 영역 (차량 그림 지우고 정갈한 폰트의 VOLVO 문구 배치)
    with main_col2:
        st.markdown(
            '''
            <div class="center-volvo-text">
                VOLVO
            </div>
            ''', unsafe_allow_html=True
        )

    # 우측 영역 (그림 지우고 깔끔한 원과 글자만)
    with main_col3:
        st.markdown(
            '''
            <div class="volvo-btn-container">
                <div class="icon-circle-grey"></div>
                <div class="btn-label">알람 줄이기</div>
            </div>
            <div class="volvo-btn-container">
                <div class="icon-circle-grey"></div>
                <div class="btn-label">헤드레스트 접기</div>
            </div>
            ''', unsafe_allow_html=True
        )

    # --- 4. 하단 공조 장치 바 (우측 하단 차량모양 -> '설정' 텍스트로 변경) ---
    st.markdown(
        '''
        <div class="volvo-bottom-bar">
            <div class="bottom-item" style="color: #8e959e; font-size: 18px;">㗊</div>
            <div class="bottom-item">💺 LO</div>
            <div class="bottom-item">
                🌀
                <span class="bottom-sub-label">공기 재순환</span>
            </div>
            <div class="bottom-item">LO 💺</div>
            <div class="bottom-item" style="color: #ffffff; font-size: 14px; font-weight: bold; cursor: pointer;">설정</div>
        </div>
        ''', 
        unsafe_allow_html=True
    )
