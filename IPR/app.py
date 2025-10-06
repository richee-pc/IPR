import streamlit as st
import streamlit.components.v1 as components
import os

# --- 페이지 설정 ---
st.set_page_config(
    page_title="정보과제연구 온라인 교실",
    page_icon="🚀",
    layout="wide"
)

# --- 커스텀 CSS ---
# 앱의 디자인을 귀엽고 깔끔하게 꾸미는 CSS 코드입니다.
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# CSS를 문자열로 직접 정의합니다.
custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700&family=Sunflower:wght@500;700&display=swap');

/* 전체 폰트 설정 */
html, body, [class*="st-"] {
    font-family: 'Nanum Gothic', sans-serif;
}

/* 제목 폰트 설정 */
h1, h2, h3 {
    font-family: 'Sunflower', sans-serif !important;
}

/* 사이드바 디자인 */
[data-testid="stSidebar"] {
    background-color: #f0f9ff;
    border-right: 2px solid #e0f2fe;
}
[data-testid="stSidebar"] .stRadio > label {
    font-size: 16px;
    padding: 10px 15px;
    border-radius: 10px;
    margin-bottom: 5px;
    transition: all 0.2s;
    font-weight: 500;
}
/* 라디오 버튼 호버 효과 */
[data-testid="stSidebar"] .stRadio > label:hover {
    background-color: #e0f2fe;
    color: #0c4a6e;
}
/* 선택된 라디오 버튼 스타일 */
[data-testid="stSidebar"] .stRadio [aria-checked="true"] {
    background-color: #bae6fd;
    color: #082f49;
    font-weight: 700;
}

/* 메인 타이틀 디자인 */
[data-testid="stAppViewContainer"] > .main > div > div > div > div > h1 {
    color: #0c4a6e;
    padding: 1rem;
    background-color: #f0f9ff;
    border-radius: 1rem;
    border: 2px solid #e0f2fe;
    text-align: center;
}
"""

# CSS 적용
st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)


# --- 현재 파일의 절대 경로를 기준으로 HTML 폴더 경로 설정 ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(BASE_DIR, 'htmls') # 사용자님이 말씀하신 'htmls' 폴더로 수정


# --- HTML 파일 로드 함수 ---
def load_html(file_path):
    """지정된 경로의 HTML 파일을 읽어옵니다."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"<h1 style='text-align: center; color: red;'>😢 파일을 찾을 수 없습니다.</h1><p style='text-align: center;'>'{file_path}' 경로에 파일이 있는지 확인해주세요.</p>"


# --- 사이드바 네비게이션 ---
st.sidebar.markdown("## 🚀 정보과제연구 교실")
st.sidebar.markdown("---")
st.sidebar.markdown("### 📚 학습 목차")

# 각 페이지에 어울리는 이모티콘과 파일명을 딕셔너리로 관리합니다.
page_options = {
    "👋 OT / 시작하기": "ot.html",
    "🎨 1차시: HTML 기초": "class1.html",
    "📖 2차시: 정보과제연구 수업 자료": "class2.html",
    "🧪 3차시: 정보과제연구 실제": "class3.html",
    "🗺️ 4차시: 최단 경로 탐구": "class4.html", # 새로 추가된 페이지
    "🏆 수행평가: 연구 계획서": "pa1.html"
}
selection = st.sidebar.radio(
    "이동할 페이지를 선택하세요:", 
    list(page_options.keys()),
    label_visibility="collapsed" # 라디오 버튼의 기본 라벨을 숨깁니다.
)


# --- 메인 페이지 콘텐츠 ---
# 페이지 제목에서 이모티콘을 분리하여 표시합니다.
selected_title = selection.split(" ", 1)[1]
st.title(selected_title)


# 선택된 페이지에 해당하는 HTML 파일의 전체 경로를 설정합니다.
html_file_name = page_options[selection]
html_file_path = os.path.join(HTML_DIR, html_file_name)


# HTML 파일을 로드하고 화면에 표시합니다.
html_content = load_html(html_file_path)
components.html(html_content, height=1000, scrolling=True)


# --- 푸터 ---
st.sidebar.markdown("---")
st.sidebar.info("이 웹앱은 Streamlit으로 만들어졌습니다. ✨")
