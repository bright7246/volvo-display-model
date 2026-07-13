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
    st.session_state.current_tab = "설정"
if "sub_page" not in st.session_state:
    st.session_state.sub_page = "main"

# [주행 설정 데이터]
if "pilot_assist" not in st.session_state: st.session_state.pilot_assist = True
if "drive_mode" not in st.session_state: st.session_state.drive_mode = "Standard"
if "steering_feel" not in st.session_state: st.session_state.steering_feel = "부드러움"
if "start_stop" not in st.session_state: st.session_state.start_stop = True
if "lane_keeping" not in st.session_state: st.session_state.lane_keeping = True
if "ready_to_drive" not in st.session_state: st.session_state.ready_to_drive = True

# [컨트롤 설정 데이터]
if "interior_brightness" not in st.session_state: st.session_state.interior_brightness = 80
if "interior_light_dim" not in st.session_state: st.session_state.interior_light_dim = "높음"
if "reduce_alarm_sensitivity" not in st.session_state: st.session_state.reduce_alarm_sensitivity = False
if "welcome_light" not in st.session_state: st.session_state.welcome_light = True
if "wireless_charging" not in st.session_state: st.session_state.wireless_charging = True

# [시스템 상세 설정 데이터]
if "sys_time_auto" not in st.session_state: st.session_state.sys_time_auto = True
if "sys_timezone_auto" not in st.session_state: st.session_state.sys_timezone_auto = True
if "sys_time_24h" not in st.session_state: st.session_state.sys_time_24h = True
if "selected_language" not in st.session_state: st.session_state.selected_language = "한국어(대한민국)"

# [NUGU Auto 전용 상태 데이터]
if "nugu_enabled" not in st.session_state: st.session_state.nugu_enabled = True
if "nugu_alarm" not in st.session_state: st.session_state.nugu_alarm = True
if "nugu_perf" not in st.session_state: st.session_state.nugu_perf = False
if "nugu_permission_clear" not in st.session_state: st.session_state.nugu_permission_clear = True

# 볼보 순정 다크 톤 배색 지정
bg_color = "rgb(18, 22, 28)"
card_color = "rgb(28, 34, 44)"
border_color = "rgb(42, 49, 61)"

# 내부 밝기 쿼리 파라미터 연동
if "brightness_slider" in st.query_params:
    st.session_state.interior_brightness = int(st.query_params["brightness_slider"])

# 2. 볼보 헤리티지 UI 스타일 정의
st.markdown(
    f"""
    <style>
    .stApp {{ background-color: {bg_color} !important; color: #ffffff !important; }}
    
    div[data-testid="stMainBlockContainer"] {{
        max-width: 510px !important;
        padding-top: 2.5rem !important;
        padding-bottom: 2rem !important;
        background-color: {card_color} !important;
        border-radius: 16px;
        box-shadow: 0 0 40px rgba(0, 0, 0, 0.6);
        margin: 0 auto;
    }}
    
    /* 상단 상태바 */
    .volvo-status-bar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 14px;
        color: #ffffff !important;
        font-weight: 500;
        margin-bottom: 25px;
        padding: 0 10px;
    }}
    
    /* 상단 메인 탭 */
    div.tab-zone button {{
        background-color: transparent !important;
        color: #8e959e !important;
        border: none !important;
        font-size: 16px !important;
        font-weight: 500 !important;
        padding: 8px 0 !important;
        width: 100% !important;
        box-shadow: none !important;
    }}
    div.tab-zone button[kind="primary"] {{
        color: #ffffff !important;
        font-weight: bold !important;
        border-bottom: 2px solid #ffffff !important;
        border-radius: 0px !important;
    }}
    
    /* 📱 퀵 컨트롤 카드 */
    .volvo-card-content {{
        background-color: rgb(22, 27, 35) !important;
        border: 1px solid {border_color} !important;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: #ffffff !important;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        width: 100%;
    }}
    .side-btn {{ height: 185px; font-size: 15px; line-height: 1.5; }}
    .center-box {{ height: 400px; font-size: 24px; letter-spacing: 5px; font-family: 'Times New Roman', Times, serif; font-weight: 400; }}

    /* ⚙️ 설정 메인 격자 카드 */
    div.volvo-grid-card div.stButton > button {{
        background-color: rgb(22, 27, 35) !important;
        color: #ffffff !important;
        border: 1px solid {border_color} !important;
        border-radius: 14px !important;
        height: 135px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
        width: 100% !important;
        white-space: pre-line !important;
    }}
    
    /* 🛠️ 세팅 박스 타이틀 */
    .volvo-title-row {{ font-size: 14px; color: #8e959e; font-weight: bold; margin-top: 22px; margin-bottom: 12px; padding-left: 5px; }}
    
    div.subpage-content-zone div[data-testid="stVerticalBlockBorderWrapper"] {{
        background-color: rgba(18, 22, 28, 0.4) !important;
        border: 1px solid {border_color} !important;
        border-radius: 14px !important;
        padding: 18px !important;
        margin-bottom: 5px !important;
    }}
    
    .setting-title {{ font-size: 15px; font-weight: bold; color: #ffffff; margin-bottom: 4px; }}
    .setting-title-align-btn {{ font-size: 15px; font-weight: bold; color: #ffffff; padding-top: 6px; }}
    .setting-title-align-tgl {{ font-size: 15px; font-weight: bold; color: #ffffff; padding-top: 2px; }}
    .setting-desc {{ font-size: 12px; color: #8e959e; line-height: 1.4; }}
    
    /* 📋 리스트 통합 레이아웃 정렬 */
    .system-list-zone {{ display: flex; flex-direction: column; width: 100%; }}
    
    /* 텍스트 컬럼 상하 정렬 보정 */
    .text-container-fix {{
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 48px;
    }}
    .system-item-main {{ font-size: 15px; font-weight: 500; color: #ffffff; line-height: 1.2; }}
    .system-item-sub {{ font-size: 12px; color: #8e959e; margin-top: 4px; line-height: 1.3; }}
    
    /* NUGU AUTO 밑 안내 문구 스타일 */
    .app-notice-desc {{
        font-size: 13px;
        color: #8e959e; 
        margin-top: 6px;
        font-weight: normal;
        line-height: 1.3;
    }}
    
    /* 🎯 우측 화살표 버튼 크기 균일화 공통 스타일 */
    div.system-list-zone div.stButton > button {{
        background-color: transparent !important;
        color: #8e959e !important;
        border: none !important;
        font-size: 20px !important;
        font-weight: bold !important;
        height: 48px !important;
        width: 100% !important;
        text-align: right !important;
        padding: 0px 8px 0px 0px !important;
        box-shadow: none !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-end !important;
    }}
    div.system-list-zone div.stButton > button:hover {{ color: #ffffff !important; }}
    
    /* NUGU AUTO 처럼 밑에 서브문구가 있어 칸이 커진 항목용 화살표 세로정렬 강제 보정 */
    div.align-arrow-center div.stButton > button {{
        height: 68px !important;
    }}
    
    /* 🔳 순정형 앱 관리 상단 버튼 스타일 */
    div.app-action-zone div.stButton > button {{
        background-color: rgb(38, 45, 56) !important;
        color: #ffffff !important;
        border: 1px solid #4a5464 !important;
        border-radius: 8px !important;
        height: 50px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        box-shadow: none !important;
    }}
    
    /* 🛡️ 권한 설정 화면 전용 커스텀 스타일 */
    .right-top-text {{
        font-size: 14px;
        color: #8e959e;
        text-align: right;
        line-height: 38px;
        font-weight: 500;
        padding-right: 8px;
    }}
    .app-header-row {{
        display: flex;
        align-items: center;
        padding: 10px 4px;
        margin-bottom: 12px;
        gap: 14px;
    }}
    .app-header-icon-custom {{
        background-color: #00A3E0;
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 15px;
        font-weight: bold;
        color: white;
    }}
    .app-header-title-custom {{
        font-size: 18px;
        font-weight: bold;
        color: #ffffff;
    }}
    
    /* 슬라이더 스타일 */
    .slider-container-custom {{ display: flex; align-items: center; justify-content: space-between; width: 100%; padding: 5px 0; background: transparent !important; }}
    .slider-wrapper {{ position: relative; flex-grow: 1; display: flex; align-items: center; margin-right: 15px; }}
    .slider-custom {{ -webkit-appearance: none; width: 100%; height: 4px; border-radius: 2px; background: #4a525d !important; outline: none; margin: 0; }}
    .slider-custom::-webkit-slider-thumb {{ -webkit-appearance: none; appearance: none; width: 16px; height: 16px; border-radius: 50%; background: #ffffff !important; cursor: pointer; }}
    .slider-val-box {{ font-size: 16px; font-weight: bold; color: #ffffff; min-width: 35px; text-align: right; font-family: 'Helvetica Neue', sans-serif; }}

    /* 알약형 세그먼트 바 */
    div.volvo-segment-row div[data-testid="stHorizontalBlock"] {{ gap: 0px !important; background-color: #1a1f27 !important; border-radius: 25px !important; padding: 4px !important; border: 1px solid #333b46 !important; margin-top: 12px !important; }}
    div.volvo-segment-row div.stButton > button[kind="primary"] {{ background-color: #00A3E0 !important; color: #ffffff !important; border: none !important; border-radius: 22px !important; font-weight: bold !important; height: 40px !important; }}
    div.volvo-segment-row div.stButton > button[kind="secondary"] {{ background-color: transparent !important; color: #727a85 !important; border: none !important; border-radius: 22px !important; height: 40px !important; box-shadow: none !important; }}
    div.volvo-fold-btn-zone div.stButton > button {{ background-color: #383e48 !important; color: #ffffff !important; border: none !important; border-radius: 8px !important; height: 38px !important; font-size: 14px !important; font-weight: bold !important; width: 100% !important; box-shadow: none !important; }}

    .card-divider {{ border-top: 1px solid #333b46; margin-top: 20px; margin-bottom: 0px; }}
    .more-link {{ display: flex; justify-content: space-between; font-size: 14px; font-weight: bold; color: #ffffff; cursor: pointer; padding-top: 14px; padding-bottom: 12px; }}

    /* 뒤로가기 버튼 박스 */
    .back-btn-box {{ display: flex; align-items: center; justify-content: space-between; width: 100%; }}
    .back-btn-box button {{ background-color: transparent !important; color: #ffffff !important; border: none !important; font-size: 18px !important; font-weight: bold !important; padding: 0 !important; box-shadow: none !important; }}
    div[data-testid="stCheckboxToggleHoverTarget"] div[aria-checked="true"] {{ background-color: #00A3E0 !important; }}

    /* 공조 장치 하단 고정 바 */
    .volvo-bottom-bar {{ display: flex; justify-content: space-between; align-items: center; background-color: #111418; padding: 14px 18px; border-radius: 12px; margin-top: 40px; border: 1px solid #232830; }}
    .bottom-item {{ font-size: 14px; font-weight: 500; color: #ffffff !important; text-align: center; }}
    .bottom-sub-label {{ font-size: 9px; color: #8e959e !important; display: block; margin-top: 2px; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- 1. 최상단 상태바 상시 표시 ---
st.markdown('<div class="volvo-status-bar"><span>오전 08:49</span><span>📶 LTE</span></div>', unsafe_allow_html=True)

# --- 2. 상단 메뉴 탭 (서브 메인 화면에서만 노출) ---
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


# 🎛️ [설정 -> 컨트롤] 서브 페이지
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
        slider_html = f"""
        <div class="slider-container-custom" style="padding: 0; margin: 0;">
            <div class="slider-wrapper">
                <input type="range" min="0" max="100" value="{st.session_state.interior_brightness}" 
                       class="slider-custom" id="brightnessRange"
                       style="width: 100%;"
                       oninput="document.getElementById('sliderVal').innerText = this.value">
            </div>
            <div class="slider-val-box" id="sliderVal">{st.session_state.interior_brightness}</div>
        </div>
        <script>
        var slider = document.getElementById("brightnessRange");
        slider.addEventListener("change", function() {{
            window.parent.postMessage({{
                type: "streamlit:set_query_params",
                queryParams: {{"brightness_slider": this.value}}
            }}, "*");
        }});
        </script>
        """
        st.components.v1.html(slider_html, height=35)
        st.write("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
        
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
        
        st.markdown('<div class="card-divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="more-link"><span>모두 보기</span><span>〉</span></div>', unsafe_allow_html=True)

    st.markdown('<div class="volvo-title-row">🔒 잠금</div>', unsafe_allow_html=True)
    with st.container(border=True):
        alarm_col1, alarm_col2 = st.columns([3.6, 1])
        with alarm_col1:
            st.markdown('<div class="setting-title">알람 감도 낮추기</div><div class="setting-desc">페리 또는 다른 교통수단 이용 시</div>', unsafe_allow_html=True)
        with alarm_col2:
            st.write("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
            st.session_state.reduce_alarm_sensitivity = st.toggle("Alarm_tgl", value=st.session_state.reduce_alarm_sensitivity, label_visibility="collapsed")
            
        st.write("<div style='margin-top:18px;'></div>", unsafe_allow_html=True)
        
        welcome_col1, welcome_col2 = st.columns([3.6, 1])
        with welcome_col1:
            st.markdown('<div class="setting-title">웰컴 라이트</div><div class="setting-desc">차량에 접근하고 차량에서 내릴 때 조명을 켭니다</div>', unsafe_allow_html=True)
        with welcome_col2:
            st.write("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
            st.session_state.welcome_light = st.toggle("Welcome_ctrl_tgl", value=st.session_state.welcome_light, label_visibility="collapsed")
            
        st.markdown('<div class="card-divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="more-link"><span>모두 보기</span><span>〉</span></div>', unsafe_allow_html=True)

    st.markdown('<div class="volvo-title-row">더 보기</div>', unsafe_allow_html=True)
    with st.container(border=True):
        hr_col1, hr_col2 = st.columns([2.8, 1.8])
        with hr_col1:
            st.markdown('<div class="setting-title-align-btn">헤드레스트 접기</div>', unsafe_allow_html=True)
        with hr_col2:
            st.markdown('<div class="volvo-fold-btn-zone">', unsafe_allow_html=True)
            st.button("접기", key="btn_headrest_fold", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        st.write("<div style='margin-top:16px;'></div>", unsafe_allow_html=True)
        
        wire_col1, wire_col2 = st.columns([3.6, 1])
        with wire_col1:
            st.markdown('<div class="setting-title-align-tgl">무선 장치 충전</div>', unsafe_allow_html=True)
        with wire_col2:
            st.session_state.wireless_charging = st.toggle("Wireless_tgl", value=st.session_state.wireless_charging, label_visibility="collapsed")
            
        st.markdown('<div class="card-divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="more-link"><span>모두 보기</span><span>〉</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# 💻 [설정 -> 시스템] 메인 리스트 탭
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "system":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈  시스템", key="back_to_settings_sys"):
        st.session_state.sub_page = "main"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="volvo-title-row">보안 상태</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin-bottom: 15px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="volvo-title-row">일반</div>', unsafe_allow_html=True)
    st.markdown('<div class="system-list-zone">', unsafe_allow_html=True)
    
    c1, c2 = st.columns([4.2, 0.8])
    with c1: st.markdown(f'<div class="text-container-fix"><div class="system-item-main">언어 및 입력</div><div class="system-item-sub">{st.session_state.selected_language}</div></div>', unsafe_allow_html=True)
    with c2: 
        if st.button("〉", key="main_sys_lang", use_container_width=True):
            st.session_state.sub_page = "sys_language"; st.rerun()
    st.markdown('<div style="border-bottom: 1px solid #232830; margin: 8px 0;"></div>', unsafe_allow_html=True)

    c3, c4 = st.columns([4.2, 0.8])
    with c3: st.markdown(f'<div class="text-container-fix"><div class="system-item-main">날짜 및 시간</div><div class="system-item-sub">2026년 7월 13일, {"24시간 시계" if st.session_state.sys_time_24h else "12시간 시계"}</div></div>', unsafe_allow_html=True)
    with c4:
        if st.button("〉", key="main_sys_time", use_container_width=True):
            st.session_state.sub_page = "sys_datetime"; st.rerun()
    st.markdown('<div style="border-bottom: 1px solid #232830; margin: 8px 0;"></div>', unsafe_allow_html=True)

    c5, c6 = st.columns([4.2, 0.8])
    with c5: st.markdown('<div class="text-container-fix"><div class="system-item-main">단위</div></div>', unsafe_allow_html=True)
    with c6: st.button("〉", key="main_sys_unit", use_container_width=True)
    st.markdown('<div style="border-bottom: 1px solid #232830; margin: 8px 0;"></div>', unsafe_allow_html=True)

    c7, c8 = st.columns([4.2, 0.8])
    with c7: st.markdown('<div class="text-container-fix"><div class="system-item-main">애플리케이션</div><div class="system-item-sub">앱 권한</div></div>', unsafe_allow_html=True)
    with c8:
        if st.button("〉", key="main_sys_apps", use_container_width=True):
            st.session_state.sub_page = "sys_apps"; st.rerun()
    st.markdown('<div style="border-bottom: 1px solid #232830; margin: 8px 0;"></div>', unsafe_allow_html=True)

    c9, c10 = st.columns([4.2, 0.8])
    with c9: st.markdown('<div class="text-container-fix"><div class="system-item-main">계정</div><div class="system-item-sub">연결된 계정</div></div>', unsafe_allow_html=True)
    with c10: st.button("〉", key="main_sys_account", use_container_width=True)
    st.markdown('<div style="border-bottom: 1px solid #232830; margin: 8px 0;"></div>', unsafe_allow_html=True)

    c11, c12 = st.columns([4.2, 0.8])
    with c11: st.markdown('<div class="text-container-fix"><div class="system-item-main">알림</div><div class="system-item-sub">애플리케이션 알림</div></div>', unsafe_allow_html=True)
    with c12: st.button("〉", key="main_sys_alarm", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="volvo-title-row" style="margin-top: 30px;">시스템 정보</div>', unsafe_allow_html=True)
    st.markdown('<div class="system-list-zone">', unsafe_allow_html=True)
    
    c13, c14 = st.columns([4.2, 0.8])
    with c13: st.markdown('<div class="text-container-fix"><div class="system-item-main">정보</div><div class="system-item-sub">Android 13</div></div>', unsafe_allow_html=True)
    with c14: st.button("〉", key="main_sys_info", use_container_width=True)
    st.markdown('<div style="border-bottom: 1px solid #232830; margin: 8px 0;"></div>', unsafe_allow_html=True)

    c15, c16 = st.columns([4.2, 0.8])
    with c15: st.markdown('<div class="text-container-fix"><div class="system-item-main">접근성</div><div class="system-item-sub">자막 환경설정</div></div>', unsafe_allow_html=True)
    with c16: st.button("〉", key="main_sys_access", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


# 🌐 [시스템 -> 상세 1. 언어 및 입력] 상세페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "sys_language":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈  언어 및 입력", key="back_to_sys_main_1"):
        st.session_state.sub_page = "system"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="system-list-zone">', unsafe_allow_html=True)
    col1, col2 = st.columns([4.2, 0.8])
    with col1: st.markdown(f'<div class="text-container-fix"><div class="system-item-main">🌐 언어</div><div class="system-item-sub">{st.session_state.selected_language}</div></div>', unsafe_allow_html=True)
    with col2:
        if st.button("〉", key="btn_lang_pop", use_container_width=True):
            st.session_state.selected_language = "English (United States)" if st.session_state.selected_language == "한국어(대한민국)" else "한국어(대한민국)"
            st.rerun()
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin: 8px 0;"></div>', unsafe_allow_html=True)
    
    col3, col4 = st.columns([4.2, 0.8])
    with col3: st.markdown('<div class="text-container-fix"><div class="system-item-main">자동완성 서비스</div><div class="system-item-sub">없음</div></div>', unsafe_allow_html=True)
    with col4: st.button("〉", key="btn_autofill", use_container_width=True)
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin: 8px 0;"></div>', unsafe_allow_html=True)
    
    col5, col6 = st.columns([4.2, 0.8])
    with col5: st.markdown('<div class="text-container-fix"><div class="system-item-main">⌨️ 키보드</div><div class="system-item-sub">키보드(IME)</div></div>', unsafe_allow_html=True)
    with col6: st.button("〉", key="btn_keyboard", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ⏰ [시스템 -> 상세 2. 날짜 및 시간] 상세페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "sys_datetime":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈  날짜 및 시간", key="back_to_sys_main_2"):
        st.session_state.sub_page = "system"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="system-list-zone">', unsafe_allow_html=True)
    col1, col2 = st.columns([4.2, 0.8])
    with col1: st.markdown('<div class="text-container-fix"><div class="system-item-main">자동으로 시간 설정</div></div>', unsafe_allow_html=True)
    with col2: st.session_state.sys_time_auto = st.toggle("sys_time_auto_tgl", value=st.session_state.sys_time_auto, label_visibility="collapsed")
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin: 8px 0;"></div>', unsafe_allow_html=True)

    col3, col4 = st.columns([4.2, 0.8])
    with col3: st.markdown('<div class="text-container-fix"><div class="system-item-main">자동으로 시간대 설정</div></div>', unsafe_allow_html=True)
    with col4: st.session_state.sys_timezone_auto = st.toggle("sys_tz_auto_tgl", value=st.session_state.sys_timezone_auto, label_visibility="collapsed")
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin: 8px 0;"></div>', unsafe_allow_html=True)

    col5, col6 = st.columns([4.2, 0.8])
    with col5: st.markdown('<div class="text-container-fix"><div class="system-item-main">날짜 설정</div><div class="system-item-sub">2026년 7월 13일</div></div>', unsafe_allow_html=True)
    with col6: st.button("〉", key="btn_date_set", use_container_width=True)
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin: 8px 0;"></div>', unsafe_allow_html=True)

    col7, col8 = st.columns([4.2, 0.8])
    with col7: st.markdown('<div class="text-container-fix"><div class="system-item-main">시간 설정</div><div class="system-item-sub">08:49</div></div>', unsafe_allow_html=True)
    with col8: st.button("〉", key="btn_time_set", use_container_width=True)
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin: 8px 0;"></div>', unsafe_allow_html=True)

    col9, col10 = st.columns([4.2, 0.8])
    with col9: st.markdown('<div class="text-container-fix"><div class="system-item-main">시간대 선택</div><div class="system-item-sub">GMT+09:00 한국 표준시</div></div>', unsafe_allow_html=True)
    with col10: st.button("〉", key="btn_timezone_set", use_container_width=True)
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin: 8px 0;"></div>', unsafe_allow_html=True)

    col11, col12 = st.columns([4.2, 0.8])
    with col11: st.markdown('<div class="text-container-fix"><div class="system-item-main">24시간 형식 사용</div><div class="system-item-sub">13:00</div></div>', unsafe_allow_html=True)
    with col12: st.session_state.sys_time_24h = st.toggle("sys_t24_tgl", value=st.session_state.sys_time_24h, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)


# 📱 [시스템 -> 상세 3. 애플리케이션 (기본 앱 목록)] 상세페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "sys_apps":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈  애플리케이션", key="back_to_sys_main_3"):
        st.session_state.sub_page = "system"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="volvo-title-row">기본 앱</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="system-list-zone align-arrow-center">', unsafe_allow_html=True)
    col1, col2 = st.columns([4.2, 0.8])
    with col1: 
        st.markdown(
            '<div class="text-container-fix">'
            '<div class="system-item-main">🔍 NUGU AUTO</div>'
            '<div class="app-notice-desc">( 현재 이 버튼만 활성화 가능 )</div>'
            '</div>', 
            unsafe_allow_html=True
        )
    with col2: 
        if st.button("〉", key="btn_nugu_auto", use_container_width=True):
            st.session_state.sub_page = "sys_nugu_info"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="system-list-zone">', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin: 8px 0;"></div>', unsafe_allow_html=True)
    
    col3, col4 = st.columns([4.2, 0.8])
    with col3: st.markdown('<div class="text-container-fix"><div class="system-item-main">🗺️ TMAP AUTO</div></div>', unsafe_allow_html=True)
    with col4: st.button("〉", key="btn_sub_tmap", use_container_width=True)
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin: 8px 0;"></div>', unsafe_allow_html=True)

    col5, col6 = st.columns([4.2, 0.8])
    with col5: st.markdown('<div class="text-container-fix"><div class="system-item-main">🎵 FLO</div></div>', unsafe_allow_html=True)
    with col6: st.button("〉", key="btn_sub_flo", use_container_width=True)
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin: 8px 0;"></div>', unsafe_allow_html=True)

    col7, col8 = st.columns([4.2, 0.8])
    with col7: st.markdown('<div class="text-container-fix"><div class="system-item-main">🍈 Melon</div></div>', unsafe_allow_html=True)
    with col8: st.button("〉", key="btn_sub_melon", use_container_width=True)
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin: 8px 0;"></div>', unsafe_allow_html=True)

    col9, col10 = st.columns([4.2, 0.8])
    with col9: st.markdown('<div class="text-container-fix"><div class="system-item-main">📞 전화</div></div>', unsafe_allow_html=True)
    with col10: st.button("〉", key="btn_sub_phone", use_container_width=True)
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin: 8px 0;"></div>', unsafe_allow_html=True)

    col11, col12 = st.columns([4.2, 0.8])
    with col11: st.markdown('<div class="text-container-fix"><div class="system-item-main">💬 메시지</div></div>', unsafe_allow_html=True)
    with col12: st.button("〉", key="btn_sub_msg", use_container_width=True)
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin: 8px 0;"></div>', unsafe_allow_html=True)

    col13, col14 = st.columns([4.2, 0.8])
    with col13: st.markdown('<div class="text-container-fix"><div class="system-item-main">🌐 오디오 및 비디오 앱 오버레이</div></div>', unsafe_allow_html=True)
    with col14: st.button("〉", key="btn_sub_overlay", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


# 🔍 [시스템 -> 애플리케이션 -> NUGU Auto 앱 정보] 세부 페이지
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "sys_nugu_info":
    st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
    if st.button("〈  앱 정보", key="back_to_sys_apps"):
        st.session_state.sub_page = "sys_apps"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)

    st.markdown('<div style="text-align: center; font-size: 16px; font-weight: bold; color: #ffffff; margin-bottom: 25px;">NUGU Auto</div>', unsafe_allow_html=True)

    st.markdown('<div class="app-action-zone">', unsafe_allow_html=True)
    act_col1, act_col2 = st.columns(2)
    with act_col1:
        btn_label = "사용" if not st.session_state.nugu_enabled else "사용 중지"
        if st.button(btn_label, key="btn_nugu_toggle_action", use_container_width=True):
            st.session_state.nugu_enabled = not st.session_state.nugu_enabled
            st.rerun()
    with act_col2:
        st.button("강제 종료", key="btn_nugu_force_stop", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div style="margin-top: 20px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="system-list-zone">', unsafe_allow_html=True)
    
    col_al1, col_al2 = st.columns([4.2, 0.8])
    with col_al1: st.markdown('<div class="text-container-fix"><div class="system-item-main" style="margin-top: 6px;">알림</div></div>', unsafe_allow_html=True)
    with col_al2: st.session_state.nugu_alarm = st.toggle("tgl_nugu_alarm", value=st.session_state.nugu_alarm, label_visibility="collapsed")
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin: 8px 0;"></div>', unsafe_allow_html=True)

    col_pr1, col_pr2 = st.columns([4.2, 0.8])
    with col_pr1: st.markdown('<div class="text-container-fix"><div class="system-item-main">권한</div><div class="system-item-sub">근처 기기, 마이크, 알림, 연락처, 위치, 전화, 통화 기록, SMS 및 추가 권한 1개</div></div>', unsafe_allow_html=True)
    with col_pr2: 
        if st.button("〉", key="btn_nugu_permission", use_container_width=True):
            st.session_state.sub_page = "sys_nugu_permissions"; st.rerun()
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin: 8px 0;"></div>', unsafe_allow_html=True)

    col_st1, col_st2 = st.columns([4.2, 0.8])
    with col_st1: st.markdown('<div class="text-container-fix"><div class="system-item-main">저장용량 및 캐시</div><div class="system-item-sub">내부 저장소의 94.87MB</div></div>', unsafe_allow_html=True)
    with col_st2: st.button("〉", key="btn_nugu_storage", use_container_width=True)
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin: 8px 0;"></div>', unsafe_allow_html=True)

    col_pf1, col_pf2 = st.columns([4.2, 0.8])
    with col_pf1: st.markdown('<div class="text-container-fix"><div class="system-item-main">앱 성능 우선순위 지정</div><div class="system-item-sub">시스템 리소스를 사용하여 앱 성능 우선순위를 지정합니다.</div></div>', unsafe_allow_html=True)
    with col_pf2: st.session_state.nugu_perf = st.toggle("tgl_nugu_perf", value=st.session_state.nugu_perf, label_visibility="collapsed")
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin: 8px 0;"></div>', unsafe_allow_html=True)

    col_cl1, col_cl2 = st.columns([4.2, 0.8])
    with col_cl1: st.markdown('<div class="text-container-fix"><div class="system-item-main" style="margin-top: 6px;">권한을 삭제하고 여유 공간 확보</div></div>', unsafe_allow_html=True)
    with col_cl2: st.session_state.nugu_permission_clear = st.toggle("tgl_nugu_clear", value=st.session_state.nugu_permission_clear, label_visibility="collapsed")
    st.markdown('<div style="border-bottom: 1px solid #333b46; margin: 8px 0;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="text-container-fix" style="padding-left: 4px;"><div class="system-item-sub" style="font-size: 14px;">버전: 2.0.133</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# 🛡️ [시스템 -> 애플리케이션 -> NUGU Auto -> 앱 권한] 세부 설정 뷰
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "sys_nugu_permissions":
    col_top_l, col_top_r = st.columns([3.5, 1.5])
    with col_top_l:
        st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
        if st.button("〈  앱 권한", key="back_to_nugu_info"):
            st.session_state.sub_page = "sys_nugu_info"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col_top_r:
        st.markdown('<div class="right-top-text">모든 권한</div>', unsafe_allow_html=True)
        
    st.markdown('<div style="border-bottom: 1px solid #2d333c; margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="app-header-row">'
        '<div class="app-header-icon-custom">N</div>'
        '<div class="app-header-title-custom">NUGU Auto</div>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown('<div style="border-bottom: 1px solid #232830; margin-top: -10px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="volvo-title-row" style="margin-top: 10px; margin-bottom: 10px;">허용됨</div>', unsafe_allow_html=True)
    
    # 🎯 [버그 수정 핵심] 마크다운 문자열 인젝션 대신 컴포넌트 객체로 격리하여 안전하게 출력
    allowed_permissions_html = """
    <style>
    .perm-wrap { font-family: 'Helvetica Neue', sans-serif; background-color: transparent; color: #ffffff; padding: 0; margin: 0; }
    .item-row { display: flex; align-items: center; padding: 12px 4px; width: 100%; box-sizing: border-box; }
    .item-icon { font-size: 20px; margin-right: 16px; color: #8e959e; width: 24px; text-align: center; }
    .item-title { font-size: 15px; font-weight: 500; color: #ffffff; }
    .item-sub { font-size: 12px; color: #8e959e; margin-top: 3px; }
    .divider { border-bottom: 1px solid #232830; margin: 4px 0; }
    </style>
    <div class="perm-wrap">
        <div class="item-row">
            <div class="item-icon">💠</div>
            <div>
                <div class="item-title">근처 기기</div>
                <div class="item-sub">지난 24시간 이내에 액세스함</div>
            </div>
        </div>
        <div class="divider"></div>
        <div class="item-row">
            <div class="item-icon">🎤</div>
            <div class="item-title">마이크</div>
        </div>
        <div class="divider"></div>
        <div class="item-row">
            <div class="item-icon">🔔</div>
            <div class="item-title">알림</div>
        </div>
        <div class="divider"></div>
        <div class="item-row">
            <div class="item-icon">👤</div>
            <div class="item-title">연락처</div>
        </div>
        <div class="divider"></div>
        <div class="item-row">
            <div class="item-icon">📍</div>
            <div>
                <div class="item-title">위치</div>
                <div class="item-sub">08:48에 마지막으로 액세스함 • 항상 허용됨</div>
            </div>
        </div>
        <div class="divider"></div>
        <div class="item-row">
            <div class="item-icon">📞</div>
            <div>
                <div class="item-title">전화</div>
                <div class="item-sub">지난 24시간 이내에 액세스함</div>
            </div>
        </div>
        <div class="divider"></div>
        <div class="item-row">
            <div class="item-icon">🕒</div>
            <div class="item-title">통화 기록</div>
        </div>
        <div class="divider"></div>
        <div class="item-row">
            <div class="item-icon">💬</div>
            <div class="item-title">SMS</div>
        </div>
        <div class="divider"></div>
        <div class="item-row">
            <div class="item-icon">⚙️</div>
            <div>
                <div class="item-title">추가 권한</div>
                <div class="item-sub">1개 더보기</div>
            </div>
        </div>
    </div>
    """
    st.components.v1.html(allowed_permissions_html, height=500, scrolling=True)
    
    st.markdown('<div class="volvo-title-row" style="margin-top: 5px; margin-bottom: 10px;">허용되지 않음</div>', unsafe_allow_html=True)
    
    denied_permissions_html = """
    <style>
    .denied-wrap { font-family: 'Helvetica Neue', sans-serif; background-color: transparent; }
    .item-row { display: flex; align-items: center; padding: 12px 4px; }
    .item-icon { font-size: 20px; margin-right: 16px; opacity: 0.4; width: 24px; text-align: center; }
    .item-title { font-size: 15px; font-weight: 500; color: #8e959e; }
    </style>
    <div class="denied-wrap">
        <div class="item-row">
            <div class="item-icon">🚫</div>
            <div class="item-title">거부된 권한 없음</div>
        </div>
    </div>
    """
    st.components.v1.html(denied_permissions_html, height=60)


# ⚙️ [설정] 메인 격자 맵 화면
elif st.session_state.current_tab == "설정" and st.session_state.sub_page == "main":
    st.write("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
        if st.button("주행", key="btn_drive_go", use_container_width=True):
            st.session_state.sub_page = "driving"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with row1_col2:
        st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
        if st.button("컨트롤", key="btn_control_go", use_container_width=True):
            st.session_state.sub_page = "control"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
        st.button("사운드", key="btn_sound_go", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with row2_col2:
        st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
        st.button("연결", key="btn_connect_go", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    row3_col1, row3_col2, row3_col3 = st.columns(3)
    with row3_col1:
        st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
        st.button("프로필", key="btn_profile_go", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with row3_col2:
        st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
        st.button("개인정보\n보호", key="btn_privacy_go", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with row3_col3:
        st.markdown('<div class="volvo-grid-card">', unsafe_allow_html=True)
        if st.button("시스템", key="btn_system_go", use_container_width=True):
            st.session_state.sub_page = "system"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)


# 📊 [상태] 및 📱 [퀵 컨트롤] 탭 구조 보존
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
