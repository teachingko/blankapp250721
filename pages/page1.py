import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

st.title("Matplotlib 한글 그래프 예시")  # 페이지 제목

# NanumGothic 폰트 파일 경로 지정 및 등록
font_path = "./fonts/NanumGothic-Regular.ttf"
font_manager.fontManager.addfont(font_path)
plt.rcParams['font.family'] = 'NanumGothic'  # 한글 폰트 적용
plt.rcParams['axes.unicode_minus'] = False   # 마이너스 깨짐 방지

# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y, label="사인 곡선")
ax.set_title("한글 제목: 사인 그래프")
ax.set_xlabel("X축 (시간)")
ax.set_ylabel("Y축 (진폭)")
ax.legend()

st.pyplot(fig)  # Streamlit에 그래프 표시

st.write("위 그래프는 NanumGothic 폰트를 직접 등록하여 그린 사인 곡선이며, 제목과 축에 한글이 정상적으로 표시됩니다.")