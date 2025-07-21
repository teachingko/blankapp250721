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

    # 성적 컬럼 지정
    score_cols = ["수학", "영어", "과학"]

    # 학생별 합계 및 평균 계산
    df["합계"] = df[score_cols].sum(axis=1)
    df["평균"] = df[score_cols].mean(axis=1)

    # 등급 계산 함수 (평균 기준)
    def get_grade(avg):
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    df["등급"] = df["평균"].apply(get_grade)

    # 과목별 석차 계산
    for col in score_cols:
        df[f"{col}_석차"] = df[col].rank(ascending=False, method="min").astype(int)

    # 결과 데이터프레임 구성
    result_cols = (
        ["이름", "수학", "영어", "과학", "합계", "평균"] +
        [f"{col}_석차" for col in score_cols] +
        ["등급"]
    )
    st.write("학생별 성적 분석 결과:")
    st.dataframe(df[result_cols])

    # 평균 성적 막대 그래프 및 등급 표시
    fig, ax = plt.subplots()
    bars = ax.bar(df["이름"], df["평균"], color="skyblue")
    ax.set_xlabel("이름")
    ax.set_ylabel("평균 점수")
    ax.set_title("학생별 평균 성적 및 등급")

    # 막대 위에 등급 표시
    for bar, grade in zip(bars, df["등급"]):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            grade,
            ha='center',
            va='bottom',
            fontsize=12,
            color='black'
        )

    st.pyplot(fig)  # 그래프 표시
else:
    st.info("CSV 파일을 업로드하면 성적 분석 결과와 그래프가 표시됩니다.")

# 이 코드는 학생 성적 데이터(CSV)를 업로드하면
# 학생별 합계, 평균, 등급, 과목별 석차, 그리고 평균 성적 막대 그래프(등급 표시)를