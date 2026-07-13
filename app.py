import streamlit as st

# 1. 페이지 설정 (최대한 디스플레이 화면처럼 보이도록 너비 조정)
st.set_page_config(
    page_title="Volvo Main Display",
    page_icon="🚗",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. 디자인을 볼보 UI와 100% 똑같이 만들기 위한 통합 CSS 스타일 설정
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
    }

    /* 상단 메뉴 탭 컨테이너 */
    .volvo-tabs {
        display: flex;
        justify-content: space-between;
        border-bottom: 1px solid #2d333c;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }

    /* 탭 메뉴 글자 스타일 */
    .tab-item {
        flex: 1;
        text-align: center;
        font-size: 16px;
        font-weight: 500;
        color: #8e959e;
        padding: 10px 0;
    }
    
    /* 활성화된 탭 하단 흰색 바 */
    .tab-item.active {
        color: #ffffff;
        font-weight: bold;
        border-bottom: 3px solid #ffffff;
    }

    /* 슬라이더 커스텀 (볼보 슬라이더 스타일) */
    div[data-testid="stSlider"] {
        padding-top: 10px;
        padding-bottom: 20px;
    }

    /* 중앙 아이콘 버튼 디자인 (원형 배경 + 밑에 글씨) */
    .volvo-btn-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin: 25px 0;
        text-align: center;
    }

    /* 파란색 활성화 원형 아이콘 (차선유지보조, 스타트스톱 등) */
    .icon-circle-blue {
        width: 60px;
        height: 60px;
        background-color: #00a0e9;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        box-shadow: 0 4px 10px rgba(0,160,233,0.3);
        margin-bottom: 8px;
    }

    /* 회색 비활성화 원형 아이콘 (알람줄이기, 헤드레스트 등) */
    .icon-circle-grey {
        width: 60px;
        height: 60px;
        background-color: #383e47;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        margin-bottom: 8px;
    }

    .btn-label {
        font-size: 14px;
        color: #e1e2e3;
        font-weight: 500;
        margin-top: 4px;
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
        font-size: 16px;
        font-weight: bold;
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

# 세션 상태 초기화 (현재 탭 저장용)
if "current_tab" not in st.session_state:
    st.session_state.current_tab = "퀵 컨트롤"

# --- 1. 최상단 상태바 (오전 08:46 | LTE) ---
st.markdown(
    '''
    <div class="volvo-status-bar">
        <span>오전 08:46</span>
        <span>📶 LTE</span>
    </div>
    ''', 
    unsafe_allow_html=True
)

# --- 2. 상단 메인 메뉴 탭 (퀵 컨트롤 / 설정 / 상태) ---
# 실제 차량 화면처럼 버튼을 누르면 밑줄(Active)이 이동하고 화면이 전환되게 구성
top_col1, top_col2, top_col3 = st.columns(3)

with top_col1:
    if st.button("퀵 컨트롤", use_container_width=True):
        st.session_state.current_tab = "퀵 컨트롤"

with top_col2:
    # 💡 요구사항 반영: '설정' 버튼을 누르면 설정 페이지로 진입
    if st.button("⚙️ 설정 진입", use_container_width=True, type="primary"):
        st.session_state.current_tab = "설정"

with top_col3:
    if st.button("상태", use_container_width=True):
        st.session_state.current_tab = "상태"

# 현재 어떤 탭이 선택되었는지 시각적 가이드 표시
if st.session_state.current_tab == "퀵 컨트롤":
    st.markdown('<div class="volvo-tabs"><div class="tab-item active">퀵 컨트롤</div><div class="tab-item">설정</div><div class="tab-item">상태</div></div>', unsafe_allow_html=True)
elif st.session_state.current_tab == "설정":
    st.markdown('<div class="volvo-tabs"><div class="tab-item">퀵 컨트롤</div><div class="tab-item active">설정</div><div class="tab-item">상태</div></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="volvo-tabs"><div class="tab-item">퀵 컨트롤</div><div class="tab-item">설정</div><div class="tab-item active">상태</div></div>', unsafe_allow_html=True)


# --- 3. 화면 분기 처리 ---

# [분기 A] 사용자가 상단에서 '설정'을 눌렀을 때 나오는 페이지
if st.session_state.current_tab == "설정":
    st.subheader("⚙️ 볼보 시스템 설정")
    st.write("임시 모델의 설정 화면입니다. 다양한 차량 옵션을 여기에 추가할 수 있습니다.")
    
    if st.button("⬅️ 메인 화면(퀵 컨트롤)으로 돌아가기"):
        st.session_state.current_tab = "퀵 컨트롤"
        st.rerun()

# [분기 B] 첫 페이지 메인 화면 (퀵 컨트롤)
else:
    # 밝기 조절 슬라이더 (사진 1번의 가로 슬라이더 바 재현)
    st.slider("☀️ 밝기 조절", min_value=0, max_value=100, value=85)

    # 중앙 레이아웃 분할 (좌측 버튼 2개 / 중앙 차량 탑뷰 / 우측 버튼 2개)
    main_col1, main_col2, main_col3 = st.columns([1, 1.2, 1])

    # 좌측 영역 (파란색 활성화 버튼들)
    with main_col1:
        # 차선유지 보조
        st.markdown(
            '''
            <div class="volvo-btn-container">
                <div class="icon-circle-blue">🛣️</div>
                <div class="btn-label">차선유지 보조</div>
            </div>
            ''', unsafe_allow_html=True
        )
        # Start/Stop
        st.markdown(
            '''
            <div class="volvo-btn-container">
                <div class="icon-circle-blue">🅰️</div>
                <div class="btn-label">Start/Stop</div>
            </div>
            ''', unsafe_allow_html=True
        )

    # 중앙 영역 (제공해주신 볼보 차량의 은색 탑뷰 이미지 느낌을 재현)
    with main_col2:
        st.write("")
        st.markdown(
            """
            <div style="text-align: center; padding: 10px 0;">
                <span style="font-size: 90px; filter: drop-shadow(0px 10px 20px rgba(0,0,0,0.6));">🚘</span>
                <p style="margin-top: 15px; font-weight: bold; color: #8e959e; letter-spacing: 1px; font-size: 13px;">VOLVO XC60</p>
            </div>
            """, unsafe_allow_html=True
        )

    # 우측 영역 (회색 버튼들)
    with main_col3:
        # 알람 줄이기
        st.markdown(
            '''
            <div class="volvo-btn-container">
                <div class="icon-circle-grey">🚗</div>
                <div class="btn-label">알람 줄이기</div>
            </div>
            ''', unsafe_allow_html=True
        )
        # 헤드레스트 접기
        st.markdown(
            '''
            <div class="volvo-btn-container">
                <div class="icon-circle-grey">💺</div>
                <div class="btn-label">헤드레스트 접기</div>
            </div>
            ''', unsafe_allow_html=True
        )

    # --- 4. 하단 공조 장치 바 (사진 12번 완벽 재현) ---
    st.markdown(
        '''
        <div class="volvo-bottom-bar">
            <div class="bottom-item" style="color: #8e959e; font-size: 20px;">㗊</div>
            <div class="bottom-item">💺 LO</div>
            <div class="bottom-item">
                🌀
                <span class="bottom-sub-label">공기 재순환</span>
            </div>
            <div class="bottom-item">LO 💺</div>
            <div class="bottom-item" style="font-size: 20px;">🚘</div>
        </div>
        ''', 
        unsafe_allow_html=True
    )
