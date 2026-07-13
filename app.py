import streamlit as st
from datetime import datetime, timedelta

# 1. 페이지 설정
st.set_page_config(page_title="Volvo Main Display", layout="centered", initial_sidebar_state="collapsed")

# 세션 상태 초기화
if "current_tab" not in st.session_state: st.session_state.current_tab = "설정"
if "sub_page" not in st.session_state: st.session_state.sub_page = "main"

# 볼보 순정 다크 톤 배색 지정
bg_color = "rgb(18, 22, 28)"
card_color = "rgb(28, 34, 44)"
border_color = "rgb(42, 49, 61)"

st.markdown(
    f"""
    <style>
    .stApp {{ background-color: {bg_color} !important; }}
    .block-container {{ max-width: 480px !important; padding: 2rem !important; margin: 0 auto; }}

    /* 핵심 디자인 고정: 모든 버튼을 감싸는 컨테이너에 스타일 강제 부여 */
    .volvo-grid-btn {{
        background-color: {card_color};
        border: 1px solid {border_color};
        border-radius: 14px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        height: 135px;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 10px;
    }}
    /* 버튼 자체 배경은 투명하게 하여 컨테이너 스타일만 노출되게 함 */
    .volvo-grid-btn button {{
        background-color: transparent !important;
        border: none !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 16px !important;
        width: 100%;
        height: 100%;
    }}
    </style>
    """, unsafe_allow_html=True
)

# 2. '주행' 상세 페이지로 들어가는 버튼 로직 (레이아웃 보호)
if st.session_state.sub_page == "main":
    st.header("설정")
    
    # 2x2 그리드 강제 유지
    col1, col2 = st.columns(2)
    
    with col1:
        # 버튼을 div 컨테이너 안에 가두는 방식
        st.markdown('<div class="volvo-grid-btn">', unsafe_allow_html=True)
        if st.button("주행", key="btn_drive"):
            st.session_state.sub_page = "driving"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="volvo-grid-btn">', unsafe_allow_html=True)
        st.button("컨트롤", key="btn_control")
        st.markdown('</div>', unsafe_allow_html=True)

# 3. 주행 페이지 전환 처리
elif st.session_state.sub_page == "driving":
    if st.button("〈 뒤로가기"):
        st.session_state.sub_page = "main"
        st.rerun()
    st.subheader("주행 설정")
    st.write("여기에 주행 관련 메뉴들을 배치하세요.")
