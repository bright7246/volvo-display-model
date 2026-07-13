import streamlit as st

# 1. 페이지 기본 설정 (다크 모드 및 반응형 레이아웃 스타일 적용)
st.set_page_config(
    page_title="Volvo Main Display",
    page_icon="🚗",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 볼보 UI 스타일을 맞추기 위한 CSS 커스텀
st.markdown(
    """
    <style>
    /* 전체 배경을 어둡게 조절 */
    .stApp {
        background-color: #121314;
        color: #ffffff;
    }
    /* 상단 상태바 및 탭 스타일 */
    .top-status {
        display: flex;
        justify-content: space-between;
        font-size: 14px;
        color: #8a8d90;
        padding: 5px 10px;
    }
    /* 텍스트 정렬 가이드 */
    .center-text {
        text-align: center;
        color: #ffffff;
        font-weight: bold;
    }
    .sub-text {
        text-align: center;
        font-size: 13px;
        color: #a0a5aa;
        margin-top: 5px;
    }
    /* 하단 바 고정 스타일 예시 */
    .bottom-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #18191a;
        padding: 15px;
        text-align: center;
        border-top: 1px solid #2c2d30;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 세션 상태 초기화 (현재 탭 저장용)
if "current_tab" not in st.session_state:
    st.session_state.current_tab = "퀵 컨트롤"

# --- [최상단 상태바] ---
st.markdown(
    '<div class="top-status"><span>오전 08:46</span><span>📶 LTE</span></div>',
    unsafe_allow_html=True,
)
st.write("---")

# --- [상단 메인 메뉴 탭] ---
# 가로로 3개의 버튼을 배치하여 탭 구현
top_col1, top_col2, top_col3 = st.columns(3)

with top_col1:
    if st.button("퀵 컨트롤", use_container_width=True):
        st.session_state.current_tab = "퀵 컨트롤"

with top_col2:
    # 활성화 가능한 '설정' 버튼
    if st.button("⚙️ 설정", use_container_width=True, type="primary"):
        st.session_state.current_tab = "설정"

with top_col3:
    if st.button("상태", use_container_width=True):
        st.session_state.current_tab = "상태"

st.write("---")

# --- [화면 분기 처리] ---

# 1. 설정 탭을 눌렀을 때 나오는 화면
if st.session_state.current_tab == "설정":
    st.title("⚙️ 설정 메뉴")
    st.write("여기에 설정과 관련된 세부 옵션들을 구현할 수 있습니다.")

    if st.button("⬅️ 메인(퀵 컨트롤)으로 돌아가기"):
        st.session_state.current_tab = "퀵 컨트롤"
        st.rerun()

# 2. 기본 메인 화면 (퀵 컨트롤)
else:
    # [밝기 조절 슬라이더]
    st.slider("💡 화면 밝기 조절", min_value=0, max_value=100, value=85)
    st.write("")

    # [중앙 레이아웃] - 왼쪽 기능 / 가운데 차량 이미지 / 오른쪽 기능
    main_col1, main_col2, main_col3 = st.columns([1, 1.2, 1])

    with main_col1:
        st.write("")
        st.write("")
        # 차선유지 보조
        st.button("🌐\n\n차선유지 보조", use_container_width=True)
        st.write("")
        st.write("")
        # Start/Stop
        st.button("🅰️\n\nStart/Stop", use_container_width=True)

    with main_col2:
        # 중앙 차량 탑뷰 이미지 (볼보 차량을 연상시키는 이모지나 가상 그래픽 대체)
        st.markdown(
            "<h1 style='text-align: center; font-size: 80px; margin: 0;'>🚘</h1>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p class='center-text'>VOLVO MODEL</p>", unsafe_allow_html=True
        )

    with main_col3:
        st.write("")
        st.write("")
        # 알람 줄이기
        st.button("🚗💨\n\n알람 줄이기", use_container_width=True)
        st.write("")
        st.write("")
        # 헤드레스트 접기
        st.button("💺\n\n헤드레스트 접기", use_container_width=True)

    # 공백 확보 및 하단바 구분
    st.write("\n" * 5)
    st.write("---")

    # [하단 공조 장치 / 공기재순환 바]
    bot_col1, bot_col2, bot_col3, bot_col4, bot_col5 = st.columns(5)
    with bot_col1:
        st.markdown("<p class='center-text'>🔳</p>", unsafe_allow_html=True)
    with bot_col2:
        st.markdown("<p class='center-text'>🌡️ LO</p>", unsafe_allow_html=True)
    with bot_col3:
        st.markdown(
            "<p class='center-text'>🌀<br><span style='font-size:10px;'>공기재순환</span></p>",
            unsafe_allow_html=True,
        )
    with bot_col4:
        st.markdown("<p class='center-text'>🌡️ LO</p>", unsafe_allow_html=True)
    with bot_col5:
        st.markdown("<p class='center-text'>🚗</p>", unsafe_allow_html=True)
