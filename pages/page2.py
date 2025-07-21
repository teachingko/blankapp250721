import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("학생 성적 분석 및 시각화")  # 페이지 제목

# 파일 업로드 위젯
uploaded_file = st.file_uploader("학생 성적 CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    # CSV 파일을 데이터프레임으로 읽기
    df = pd.read_csv(uploaded_file)
    st.write("업로드된 데이터:")
    st.dataframe(df)  # 데이터프레임 표시

    # 학생별 평균 점수 계산
    score_cols = ["수학", "영어", "과학"]
    df["평균"] = df[score_cols].mean(axis=1)
    st.write("학생별 평균 점수:")
    st.dataframe(df[["이름", "평균"]])

    # 과목별 석차 계산
    for col in score_cols:
        df[f"{col}_석차"] = df[col].rank(ascending=False, method="min").astype(int)
    st.write("과목별 석차:")
    st.dataframe(df[["이름"] + [f"{col}_석차" for col in score_cols]])

    # 평균 점수 기준 상위 5명 바 차트
    top5 = df.sort_values("평균", ascending=False).head(5)
    fig, ax = plt.subplots()
    ax.bar(top5["이름"], top5["평균"], color="skyblue")
    ax.set_xlabel("이름")
    ax.set_ylabel("평균 점수")
    ax.set_title("평균 점수 상위 5명")
    st.pyplot(fig)  # 그래프 표시
else:
    st.info("CSV 파일을 업로드하면 성적 분석 결과와 그래프가 표시됩니다.")

# 이 코드는 학생 성적 데이터(CSV)를 업로드하면
# 학생별 평균, 과목별 석차, 평균 상위 5명 바 차트를
# 계산 및 시각화해주는 Streamlit 앱입니다.