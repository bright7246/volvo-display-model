import streamlit as st
from datetime import datetime, timedelta

# 1. 페이지 설정 (황금 규격 철저히 고정)
st.set_page_config(
    page_title="Volvo Main Display",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 세션 상태 초기화
if "current_tab" not in st.session_state:
    st.session_state.current_tab = "설정"
if "sub_page" not in st.session_state:
    st.session_state.sub_page = "main"

# [기존 주행 설정 데이터]
if "pilot_assist" not in st.session_state: st.session_state.pilot_assist = True
if "drive_mode" not in st.session_state: st.session_state.drive_mode = "Standard"
if "steering_feel" not in st.session_state: st.session_state.steering_feel = "부드러움"
if "start_stop" not in st.session_state: st.session_state.start_stop = True
if "lane_keeping" not in st.session_state: st.session_state.lane_keeping = True
if "ready_to_drive" not in st.session_state: st.session_state.ready_to_drive = True

# [컨트롤 설정 데이터]
if "interior_brightness" not in st.session_state: st.session_state.interior_brightness = 80
if "interior_light_dim" not in st.session_state: st.session_state.interior_light_dim = "높음"

# 볼보 순정 다크 톤 배색 지정
bg_color = "rgb(18, 22, 28)"
card_color = "rgb(28, 34, 44)"
border_color = "rgb(42, 49, 61)"

# Query Parameter를 활용한 커스텀 슬라이더 값 실시간 동기화 처리
if "brightness_slider" in st.query_params:
    st.session_state.interior_brightness = int(st.query_params["brightness_slider"])

# 2. [골든 룰] 스타일 정의
st.markdown(
    f"""
    <style>
    /* 전체 앱 배경 */
    .stApp {{
        background-color: {bg_color} !important;
        color: #ffffff !important;
    }}
    
    /* 상단 여백 보정 컨테이너 */
    .block-container {{
        max-width: 480px !important;
        padding-top: 4rem !important; 
        padding-bottom: 2rem !important;
        margin: 0 auto;
        min-height: 850px; 
    }}
    
    /* 상단 시계 및 상태바 */
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
    
    /* 상단 메인 탭 메뉴 */
    div.tab-zone button {{
        background-color: transparent !important;
        color: #8e959e !important;
        border: none !important;
        font-size: 16px !important;
        font-weight: 500 !important;
        padding: 8px 0 !important;
        width: 100% !important;
        box-shadow: none !important;
        border-radius: 0px !important;
    }}
    div.tab-zone button[kind="primary"] {{
        color: #ffffff !important;
        font-weight: bold !important;
        border-bottom: 2px solid #ffffff !important;
    }}
    
    /* 📱 퀵 컨트롤 전용 카드 스타일 */
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
    .side-btn {{ height: 185px; font-size: 15px; line-height: 1.5; }}
    .center-box {{ height: 400px; font-size: 24px; letter-spacing: 5px; font-family: 'Times New Roman', Times, serif; font-weight: 400; }}
    
    /* ⚙️ 설정 메인 카드 버튼 스타일 */
    div.volvo-grid-card div.stButton > button {{
        background-color: {card_color} !important;
        color: #ffffff !important;
        border: 1px solid {border_color} !important;
        border-radius: 14px !important;
        height: 135px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4) !important;
        width: 100% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        white-space: pre-line !important;
    }}
    
    /* 🛠️ [A 세팅] 제목줄 스타일 */
    .volvo-title-row {{
        font-size: 14px;
        color: #8e959e;
        font-weight: bold;
        margin-top: 25px;
        margin-bottom: 12px;
        padding-left: 5px;
    }}
    
    /* 🛠️ [B 세팅] 서브페이지 내부 st.container 상자 강제 제어 */
    div.subpage-content-zone div[data-testid="stVerticalBlockBorderWrapper"] {{
        background-color: {card_color} !important;
        border: 1px solid {border_color} !important;
        border-radius: 14px !important;
        padding: 18px !important;
        margin-bottom: 5px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
    }}
    
    .setting-title {{ font-size: 15px; font-weight: bold; color: #ffffff; margin-bottom: 4px; }}
    .setting-desc {{ font-size: 12px; color: #8e959e; line-height: 1.4; }}
    
    /* 🎚️ [요구사항 반영] 슬라이더 바 최대값(가로 길이)을 아래 버튼의 '높음' 영역 끝까지 확장 */
    .slider-container-custom {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
        padding: 10px 0;
        background: transparent !important;
    }}
    .slider-wrapper {{
        position: relative;
        flex-grow: 1;
        display: flex;
        align-items: center;
        margin-right: 8px; /* 숫자가 레이아웃 우측 끝에 붙도록 마진 최소화 */
    }}
    .slider-custom {{
        -webkit-appearance: none;
        width: 100%;
        height: 4px;
        border-radius: 2px;
        background: #4a525d !important;
        outline: none;
        margin: 0;
    }}
    .slider-custom::-webkit-slider-thumb {{
        -webkit-appearance: none;
        appearance: none;
        width: 16px;
        height: 16px;
        border-radius: 50%;
        background: #ffffff !important;
        cursor: pointer;
    }}
    .slider-val-box {{
        font-size: 16px;
        font-weight: bold;
        color: #ffffff;
        min-width: 35px;
        text-align: right;
        font-family: 'Helvetica Neue', sans-serif;
    }}
    
    /* 🔗 알약형 통합 세그먼트 가로 정렬 바 */
    div.volvo-segment-row div[data-testid="stHorizontalBlock"] {{
        gap: 0px !important;
        background-color: #1a1f27 !important;
        border-radius: 25px !important;
        padding: 4px !important;
        border: 1px solid #333b46 !important;
        margin-top: 12px !important;
    }}
    
    div.volvo-segment-row div.stButton > button[kind="primary"] {{
        background-color: #00A3E0 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 22px !important;
        font-weight: bold !important;
        height: 40px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.4) !important;
    }}
    
    div.volvo-segment-row div.stButton > button[kind="secondary"] {{
        background-color: transparent !important;
        color: #727a85 !important;
        border: none !important;
        border-radius: 22px !important;
        height: 40px !important;
        box-shadow: none !important;
    }}
    
    /* 카드 내부 구분선 및 모두보기 */
    .card-divider {{
        border-top: 1px solid #333b46;
        margin-top: 20px;
        margin-bottom: 0px;
    }}
    /* 💡 [요구사항 반영] 모두 보기 아래쪽 공백을 직전 상태의 딱 절반인 12px로 완벽 튜닝 */
    .more-link {{
        display: flex;
        justify-content: space-between;
        font-size: 14px;
        font-weight: bold;
        color: #ffffff;
        cursor: pointer;
        padding-top: 14px;
        padding-bottom: 12px; 
    }}
    
    /* 뒤로가기 링크 박스 */
    .back-btn-box button {{
        background-color: transparent !important;
        color: #ffffff !important;
        border: none !important;
        font-size: 18px !important;
        font-weight: bold !important;
        padding: 0 !important;
        box-shadow: none !important;
    }}
    
    /* 하단 공조 바 */
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
    .bottom-item {{ font-size: 14px; font-weight: 500; color: #ffffff !important; text-align: center; }}
    .bottom-sub-label {{ font-size: 9px; color: #8e959e !important; display: block; margin-top: 2px; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- 1. 최상단 상태바 상시 표시 ---
utc_now = datetime.utcnow()
kor_now = utc_now + timedelta(hours=9)
ampm = "오전" if kor_now.hour < 12 else "오후"
display_hour = kor_now.hour % 12
display_hour = 12 if display_hour == 0 else display_hour
time_string = f"{ampm} {display_hour:02d}:{kor_now.minute:02d}"

st.markdown(
    f'<div class="volvo-status-bar"><span>{time_string}</span><span>📶 LTE</span></div>', 
    unsafe_allow_html=True
)

# --- 2. 상단 메뉴 탭 ---
if st.session_state.sub_page == "main":
    st.markdown('<div class="tab-zone">', unsafe_allow_html=True)
    top_col1, top_col2, top_col3 = st.columns(3)
    with top_col1:
        is_active = "primary" if st.session_state.current_tab == "퀵 컨트롤" else "secondary"
        if st.button("퀵 컨트롤", key="tab_quick", type=is_active, use_container_width=True):
            st.session_state.current_tab = "퀵 컨트롤"; st.rerun()
    with top_col2:
        is_active = "primary" if st.session_state.current_tab == "설정" else "secondary"
        if st.button("설정", key="tab_settings", type=is_active, use_container_width=True):
            st.session_state.current_tab = "설정"; st.rerun()
    with top_col3:
        is_active = "primary" if st.session_state.current_tab == "상태" else "secondary"
        if st.button("상태", key="tab_status", type=is_active, use_container_width=True):
            st.session_state.current_tab = "상태"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: -10px; margin-bottom: 25px;"></div>', unsafe_allow_html=True)


# --- 3. 화면 분기 처리 ---

# 🚗 [설정 -> 주행] 서브 페이지
if st.session_state.current_tab == "설정" and st.session_state.sub_page == "driving":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈  주행", key="back_to_settings"):
        st.session_state.sub_page = "main"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="subpage-content-zone">', unsafe_allow_html=True)
    st.markdown('<div class="volvo-title-row">운전자 지원 시스템</div>', unsafe_allow_html=True)
    with st.container(border=True):
        pa_col1, pa_col2 = st.columns([3.6, 1])
        with pa_col1:
            st.markdown('<div class="setting-title">Pilot Assist 기본 설정</div><div class="setting-desc">스티어링 휠에서 ▶을 눌러 어댑티브 크루즈 컨트롤과 Pilot Assist를 전환합니다.</div>', unsafe_allow_html=True)
        with pa_col2:
            st.write("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
            st.session_state.pilot_assist = st.toggle("PA_tgl", value=st.session_state.pilot_assist, label_visibility="collapsed")

    st.markdown('<div class="volvo-title-row">주행 역학</div>', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown('<div class="setting-title">주행 모드</div><div class="setting-desc">모든 종류의 일상 주행 시 효율성을 위해 가속, 주행 역학 및 조향이 최적화됩니다.</div>', unsafe_allow_html=True)
        st.markdown('<div class="volvo-segment-row">', unsafe_allow_html=True)
        dm_col1, dm_col2 = st.columns(2)
        with dm_col1:
            dm_type = "primary" if st.session_state.drive_mode == "Standard" else "secondary"
            if st.button("Standard", key="btn_seg_std", type=dm_type, use_container_width=True):
                st.session_state.drive_mode = "Standard"; st.rerun()
        with dm_col2:
            dm_type = "primary" if st.session_state.drive_mode == "Off-road" else "secondary"
            if st.button("Off-road", key="btn_seg_off", type=dm_type, use_container_width=True):
                st.session_state.drive_mode = "Off-road"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown('<div class="setting-title">스티어링 감도</div>', unsafe_allow_html=True)
        st.markdown('<div class="volvo-segment-row">', unsafe_allow_html=True)
        sf_col1, sf_col2 = st.columns(2)
        with sf_col1:
            sf_type = "primary" if st.session_state.steering_feel == "부드러움" else "secondary"
            if st.button("부드러움", key="btn_seg_sf1", type=sf_type, use_container_width=True):
                st.session_state.steering_feel = "부드러움"; st.rerun()
        with sf_col2:
            sf_type = "primary" if st.session_state.steering_feel == "단단함" else "secondary"
            if st.button("단단함", key="btn_seg_sf2", type=sf_type, use_container_width=True):
                st.session_state.steering_feel = "단단함"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with st.container(border=True):
        ss_col1, ss_col2 = st.columns([3.6, 1])
        with ss_col1:
            st.markdown('<div class="setting-title">Start/Stop</div><div class="setting-desc">정지 시 일시적으로 엔진을 끕니다. 새로 주행할 때마다 켜짐으로 재설정됩니다.</div>', unsafe_allow_html=True)
        with ss_col2:
            st.write("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
            st.session_state.start_stop = st.toggle("SS_tgl", value=st.session_state.start_stop, label_visibility="collapsed")

    st.markdown('<div class="volvo-title-row">안전 어시스트</div>', unsafe_allow_html=True)
    with st.container(border=True):
        lk_col1, lk_col2 = st.columns([3.6, 1])
        with lk_col1:
            st.markdown('<div class="setting-title">차선유지 보조 시스템</div><div class="setting-desc">갑작스런 차선 이탈을 방지하도록 도와줍니다.</div>', unsafe_allow_html=True)
        with lk_col2:
            st.write("<div style='margin-top:5px;'></div>", unsafe_allow_html=True)
            st.session_state.lane_keeping = st.toggle("LK_tgl", value=st.session_state.lane_keeping, label_visibility="collapsed")

    with st.container(border=True):
        rd_col1, rd_col2 = st.columns([3.6, 1])
        with rd_col1:
            st.markdown('<div class="setting-title">주행 준비 알림</div><div class="setting-desc">전방 차량이 주행을 시작한 후 알림을 제공합니다.</div>', unsafe_allow_html=True)
        with rd_col2:
            st.write("<div style='margin-top:5px;'></div>", unsafe_allow_html=True)
            st.session_state.ready_to_drive = st.toggle("RD_tgl", value=st.session_state.ready_to_drive, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)


# 🎛️ [설정 -> 컨트롤] 서브 페이지 (가로 길이 극대화 및 하단 여백 반절 축소 완료)
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "control":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈  컨트롤", key="back_to_settings_ctrl"):
        st.session_state.sub_page = "main"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="subpage-content-zone">', unsafe_allow_html=True)
    st.markdown('<div class="volvo-title-row">조명 및 디스플레이</div>', unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown('<div class="setting-title">내부 밝기</div>', unsafe_allow_html=True)
        
        # 💡 버튼 크기 마감과 동일한 핏으로 와이드하게 작동하는 커스텀 슬라이더
        slider_html = f"""
        <div class="slider-container-custom">
            <div class="slider-wrapper">
                <input type="range" min="0" max="100" value="{st.session_state.interior_brightness}" 
                       class="slider-custom" id="brightnessRange"
                       oninput="document.getElementById('sliderVal').innerText = this.value">
            </div>
            <div class="slider-val-box" id="sliderVal">{st.session_state.interior_brightness}</div>
        </div>
        
        <script>
        var slider = document.getElementById("brightnessRange");
        slider.addEventListener("change", function() {{
            const url = new URL(window.location.href);
            url.searchParams.set("brightness_slider", this.value);
            window.parent.postMessage({{
                type: "streamlit:set_query_params",
                queryParams: {{"brightness_slider": this.value}}
            }}, "*");
        }});
        </script>
        """
        st.components.v1.html(slider_html, height=45)
        
        st.write("<div style='margin-top:5px;'></div>", unsafe_allow_html=True)
        
        st.markdown('<div class="setting-title">내부 조명 감도</div>', unsafe_allow_html=True)
        st.markdown('<div class="volvo-segment-row">', unsafe_allow_html=True)
        dim_col1, dim_col2, dim_col3 = st.columns(3)
        with dim_col1:
            t_type = "primary" if st.session_state.interior_light_dim == "끄기" else "secondary"
            if st.button("끄기", key="btn_dim_off", type=t_type, use_container_width=True):
                st.session_state.interior_light_dim = "끄기"; st.rerun()
        with dim_col2:
            t_type = "primary" if st.session_state.interior_light_dim == "낮음" else "secondary"
            if st.button("낮음", key="btn_dim_low", type=t_type, use_container_width=True):
                st.session_state.interior_light_dim = "낮음"; st.rerun()
        with dim_col3:
            t_type = "primary" if st.session_state.interior_light_dim == "높음" else "secondary"
            if st.button("높음", key="btn_dim_high", type=t_type, use_container_width=True):
                st.session_state.interior_light_dim = "높음"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
        # 구분선 및 12px 간격으로 최적화 마감된 모두 보기 영역
        st.markdown('<div class="card-divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="more-link"><span>모두 보기</span><span>〉</span></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# ⚙️ [설정] 메인 탭 화면 (골든 룰 완전 사수 구역)
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "main":
    st.write("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        with st.container(border=False):
            st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
            if st.button("주행", key="btn_drive_go", use_container_width=True):
                st.session_state.sub_page = "driving"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
    with row1_col2:
        with st.container(border=False):
            st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
            if st.button("컨트롤", key="btn_control_go", use_container_width=True):
                st.session_state.sub_page = "control"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        with st.container(border=False):
            st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
            st.button("사운드", key="btn_sound_go", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    with row2_col2:
        with st.container(border=False):
            st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
            st.button("연결", key="btn_connect_go", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    row3_col1, row3_col2, row3_col3 = st.columns(3)
    with row3_col1:
        with st.container(border=False):
            st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
            st.button("프로필", key="btn_profile_go", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    with row3_col2:
        with st.container(border=False):
            st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
            st.button("개인정보\n보호", key="btn_privacy_go", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    with row3_col3:
        with st.container(border=False):
            st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
            st.button("시스템", key="btn_system_go", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

# 📊 [상태] 탭 화면
elif st.session_state.current_tab == "상태":
    st.subheader("📊 차량 상태")
    st.write("차량 진단 및 정보를 확인합니다.")

# 📱 [퀵 컨트롤] 탭 화면
else:
    st.write("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True) 
    main_col1, main_col2, main_col3 = st.columns([1, 1.3, 1])

    with main_col1:
        st.markdown('<div class="volvo-card-content side-btn">차선<br>유지</div>', unsafe_allow_html=True)
        st.write("<div style='margin-top:25px;'></div>", unsafe_allow_html=True)
        st.markdown('<div class="volvo-card-content side-btn">Start<br>Stop</div>', unsafe_allow_html=True)

    with main_col2:
        st.markdown('<div class="volvo-card-content center-box">VOLVO</div>', unsafe_allow_html=True)

    with main_col3:
        st.markdown('<div class="volvo-card-content side-btn">알람<br>줄이기</div>', unsafe_allow_html=True)
        st.write("<div style='margin-top:25px;'></div>", unsafe_allow_html=True)
        st.markdown('<div class="volvo-card-content side-btn">헤드<br>레스트</div>', unsafe_allow_html=True)

# --- 4. 하단 공조 장치 바 ---
bottom_html = (
    '<div class="volvo-bottom-bar">'
    '<div class="bottom-item" style="color: #8e959e; font-size: 16px;">㗊</div>'
    '<div class="bottom-item">💺 LO</div>'
    '<div class="bottom-item"><span style="font-size: 16px;">🌀</span><span class="bottom-sub-label">공기 재순환</span></div>'
    '<div class="bottom-item">LO 💺</div>'
    '<div class="bottom-item" style="font-size: 16px; opacity: 0.9;">🚗</div>'
    '</div>'
)
st.markdown(bottom_html, unsafe_allow_html=True)
