# 필요한 라이브러리를 임포트합니다.
import streamlit as st
import numpy as np

# 이력서 정보를 설정합니다.
resume = {
    "이름": "홍길동",
    "나이": 30,
    "거주지": "서울",
    "전화번호": "010-1234-5678",
    "이메일": "hong@example.com",
    "학력": [
        {"학교": "서울대학교", "전공": "컴퓨터공학과", "학년": "4", "학점": "4.3"},
    ],
    "경력": [
        {"회사": "ABC Company", "직위": "Software Engineer", "기간": "2021 - 현재"},
    ],
    "스킬": ["Python", "Streamlit", "Numpy"]
}

# Streamlit 앱 구성
st.title("나의 이력서")

# 이력서 섹션
for section, items in resume.items():
    st.header(section)
    if section in ["이름", "나이", "거주지", "전화번호", "이메일"]:
        st.subheader(items)
    elif section in ["학력", "경력"]:
        for item in items:
            for key, value in item.items():
                st.subheader(f"{key}: {value}")
    elif section == "스킬":
        for skill in items:
            st.subheader(skill)
