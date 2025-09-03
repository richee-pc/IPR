import streamlit as st
import streamlit.components.v1 as components
import os

# --- 페이지 설정 ---
st.set_page_config(
    page_title="정보과제연구 온라인 교실",
    page_icon="🚀",
    layout="wide" # 'centered' 또는 'wide'
)

# --- 현재 파일의 절대 경로를 기준으로 HTML 폴더 경로 설정 ---
# 이 스크립트 파일(app.py)이 있는 디렉토리를 기준으로 경로를 설정하여
# 어디서 실행하든지 'html' 폴더를 정확히 찾을 수 있도록 합니다.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(BASE_DIR, 'html')


# --- HTML 파일 로드 함수 ---
# HTML 파일의 내용을 읽어서 반환하는 함수입니다.
def load_html(file_path):
    """지정된 경로의 HTML 파일을 읽어옵니다."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"<h1 style='text-align: center; color: red;'>😢 파일을 찾을 수 없습니다.</h1><p style='text-align: center;'>'{file_path}' 경로에 파일이 있는지 확인해주세요.</p>"


# --- 사이드바 네비게이션 ---
st.sidebar.title("📚 학습 목차")

# st.sidebar.radio를 사용하여 메뉴를 만듭니다.
# 3차시 수업을 추가했습니다.
page_options = {
    "OT / 시작하기": "ot.html",
    "1차시: HTML 기초": "class1.html",
    "2차시: 정보과제연구 수업 자료": "class2.html",
    "3차시: 조 추첨 알고리즘 프로젝트": "class3.html"
}
selection = st.sidebar.radio("이동할 페이지를 선택하세요:", list(page_options.keys()))


# --- 메인 페이지 콘텐츠 ---
st.title(f"✨ {selection}")
st.markdown("---") # 구분선 추가

# 선택된 페이지에 해당하는 HTML 파일의 전체 경로를 설정합니다.
html_file_name = page_options[selection]
html_file_path = os.path.join(HTML_DIR, html_file_name)


# HTML 파일을 로드하고 화면에 표시합니다.
html_content = load_html(html_file_path)
# height를 넉넉하게 주어 스크롤이 생기도록 합니다.
components.html(html_content, height=8000, scrolling=True)


# --- 푸터 ---
st.sidebar.markdown("---")
st.sidebar.info("이 웹앱은 Streamlit으로 만들어졌습니다.")

