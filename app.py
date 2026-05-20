import streamlit as st
import pandas as pd
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🚀",
    layout="wide"
)

# 제목
st.title("🚀 Streamlit 웹앱")
st.write("첫 번째 웹앱입니다!")

# 사이드바
st.sidebar.header("메뉴")

menu = st.sidebar.selectbox(
    "기능 선택",
    ["홈", "데이터", "차트", "입력폼"]
)

# 홈
if menu == "홈":
    st.header("홈 화면")

    st.success("웹앱 실행 성공!")

    if st.button("클릭"):
        st.balloons()

# 데이터
elif menu == "데이터":
    st.header("데이터 테이블")

    df = pd.DataFrame({
        "이름": ["김", "이", "박", "최"],
        "점수": [95, 88, 76, 100]
    })

    st.dataframe(df)

# 차트
elif menu == "차트":
    st.header("랜덤 차트")

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["A", "B", "C"]
    )

    st.line_chart(chart_data)

# 입력폼
elif menu == "입력폼":
    st.header("사용자 입력")

    name = st.text_input("이름")

    age = st.slider("나이", 1, 100, 20)

    hobby = st.selectbox(
        "취미",
        ["게임", "운동", "음악", "코딩"]
    )

    if st.button("제출"):
        st.write(f"이름: {name}")
        st.write(f"나이: {age}")
        st.write(f"취미: {hobby}")

        st.success("제출 완료!")
