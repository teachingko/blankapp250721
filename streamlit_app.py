import streamlit as st

st.title("🎈 My new app")  # 페이지의 제목

st.header("헤더 예시")  # 큰 제목(섹션 구분)

st.subheader("서브헤더 예시")  # 작은 제목(섹션 내 소제목)

st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)  # 일반 텍스트 및 링크

st.markdown("**마크다운 텍스트**: *이탤릭*, ~~취소선~~, `코드`")  # 마크다운 지원

st.code("print('Hello, Streamlit!')", language="python")  # 코드 블록

st.text("텍스트 블록 예시")  # 단순 텍스트

st.latex(r"\int_0^1 x^2 dx")  # LaTeX 수식

st.success("성공 메시지 예시")  # 녹색 알림

st.info("정보 메시지 예시")  # 파란색 알림

st.warning("경고 메시지 예시")  # 노란색 알림

st.error("에러 메시지 예시")  # 빨간색 알림

st.image(
    "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",
    caption="Streamlit 로고",
    width=200,
)  # 이미지 표시

st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")  # 오디오 재생

st.video("https://www.youtube.com/watch?v=B2iAodr0fOo")  # 비디오 재생

st.checkbox("체크박스 예시")  # 체크박스

st.radio("라디오 버튼 예시", ["옵션 1", "옵션 2", "옵션 3"])  # 라디오 버튼

st.selectbox("셀렉트박스 예시", ["선택 1", "선택 2", "선택 3"])  # 드롭다운 셀렉트박스

st.multiselect("멀티셀렉트 예시", ["A", "B", "C", "D"])  # 다중 선택

st.slider("슬라이더 예시", 0, 100, 50)  # 슬라이더

st.number_input("숫자 입력 예시", min_value=0, max_value=100, value=10)  # 숫자 입력

st.text_input("텍스트 입력 예시", value="기본값")  # 텍스트 입력

st.text_area("텍스트 영역 예시", value="여러 줄 입력 가능")  # 여러 줄 텍스트 입력

st.date_input("날짜 입력 예시")  # 날짜 입력

st.time_input("시간 입력 예시")  # 시간 입력

st.file_uploader("파일 업로드 예시")  # 파일 업로더

st.button("버튼 예시")  # 버튼

st.sidebar.title("사이드바 제목")  # 사이드바에 제목 추가

st.sidebar.write("사이드바에 텍스트 추가")  # 사이드바에 텍스트 추가

import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["컬럼 1", "컬럼 2", "컬럼 3"]
)
st.dataframe(df)  # 데이터프레임 표시

st.table(df.head())  # 테이블 형태로 표시

st.metric(label="매출", value="₩1,000,000", delta="+5%")  # 메트릭(지표) 표시



import altair as alt

chart = alt.Chart(df).mark_bar().encode(
    x="컬럼 1",
    y="컬럼 2"
)
st.altair_chart(chart)  # Altair 차트 표시

st.progress(70)  # 진행률 바

st.spinner("로딩 중...")  # 스피너(로딩 표시)

st.caption("캡션 예시")  # 작은 설명글

st.divider()  # 구분선

# 각 요소는 streamlit 페이지에서 다양한 UI/UX를 구현할 때
