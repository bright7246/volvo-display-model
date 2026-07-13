import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="Volvo Main Display", layout="centered", initial_sidebar_state="collapsed")

# 세션 상태 초기화
if "current_tab" not in st.session_state: st.session_state.current_tab = "설정"
if "sub_page" not in st.session_state: st.session_state.sub_page = "main"

# 볼보 배색 및 스타일 (핵심: 버튼 크기 강제 CSS)
bg_color = "rgb(18, 22, 28)"
card_color = "rgb(28, 34, 44)"

st.markdown(f"""
    <style>
    .stApp {{ background-color: {bg_color} !important; }}
    
    /* 버튼 크기 강제 고정 */
    div.stButton > button {{
        height: 92px !important; 
        font-size: 18px !important;
        font-weight: bold !important;
        background-color: rgb(22, 27, 35) !important;
        border: 1px solid rgb(42, 49, 61) !important;
        border-radius: 14px !important;
        color: white !important;
        width: 100% !important;
    }}
    
    /* 텍스트 정중앙 정렬 */
    div.stButton > button div[data-testid="stMarkdownContainer"] p {{
        margin: 0 !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# 탭 로직
if st.session_state.sub_page == "main":
    c1, c2, c3 = st.columns(3)
    with c1: 
        if st.button("퀵 컨트롤"): st.session_state.current_tab = "퀵 컨트롤"
    with c2: 
        if st.button("설정"): st.session_state.current_tab = "설정"
    with c3: 
        if st.button("상태"): st.session_state.current_tab = "상태"

# [설정] 탭 화면
if st.session_state.current_tab == "설정" and st.session_state.sub_page == "main":
    st.write("### 설정 메뉴")
    # 1행
    col1, col2 = st.columns(2)
    with col1: st.button("주행 설정")
    with col2: st.button("컨트롤")
    st.write("<br>", unsafe_allow_html=True)
    # 2행
    col3, col4 = st.columns(2)
    with col3: st.button("사운드")
    with col4: st.button("시스템")

# [상태] 탭 및 공기압/진단 뷰는 기존 로직 유지
elif st.session_state.current_tab == "상태":
    st.write("### 상태 정보")
    sc1, sc2 = st.columns(2)
    with sc1:
        if st.button("타이어 공기압"): st.session_state.sub_page = "tire"
    with sc2:
        if st.button("진단 결과"): st.session_state.sub_page = "diag"

# 상세 뷰 로직
if st.session_state.sub_page == "tire":
    st.info("타이어 공기압: 정상 (모든 타이어 35 PSI)")
    if st.button("뒤로가기"): st.session_state.sub_page = "main"; st.rerun()
elif st.session_state.sub_page == "diag":
    st.success("진단: 이상 없음")
    if st.button("뒤로가기"): st.session_state.sub_page = "main"; st.rerun()
