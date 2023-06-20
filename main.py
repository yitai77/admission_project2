# 필요한 라이브러리를 임포트합니다.
import streamlit as st

# 이력서 초기 정보를 설정합니다.
resume = {
    "이름": "홍길동",
    "나이": "30",
    "거주지": "서울",
    "전화번호": "010-1234-5678",
    "이메일": "hong@example.com",
    "학력": "서울대학교, 컴퓨터공학과",
    "경력": "ABC Company, Software Engineer, 2021 - 현재",
    "스킬": "Python, Streamlit, Numpy"
}

# Streamlit 앱 구성
st.title("나의 이력서")

# 이력서 수정 섹션
st.sidebar.header("이력서 수정")
selected_key = st.sidebar.selectbox("수정할 항목을 선택하세요.", list(resume.keys()))
user_input = st.sidebar.text_input(f"{selected_key} 정보를 입력하세요.", value=resume[selected_key])

# 입력이 변경될 때마다 이력서 정보를 업데이트합니다.
resume[selected_key] = user_input

# 이력서 섹션
for key, value in resume.items():
    st.header(key)
    st.write(value)
