import streamlit as st
import random

st.set_page_config(page_title="오늘의 공부 추천 🌱", page_icon="📚", layout="centered")

# 제목
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌱 오늘의 컨디션 기반 공부 추천 🎓</h1>", unsafe_allow_html=True)
st.write("오늘 기분에 맞는 맞춤형 공부법을 추천해드릴게요! ✨")

# 컨디션 선택
mood = st.radio("👉 오늘 너의 상태는 어때?", 
                ["😀 에너지가 넘쳐!", "😐 평범해", "😴 피곤해"])

# 추천 공부법
if st.button("🔍 추천 받기"):
    if mood == "😀 에너지가 넘쳐!":
        st.success("🚀 오늘은 집중력이 최고예요! 어려운 과목 심화 문제를 풀어보세요 ✏️")
        st.info("추천 활동: 수학 심화, 영어 말하기, 과학 탐구 프로젝트")
    elif mood == "😐 평범해":
        st.success("📚 오늘은 무난한 날이에요. 계획한 공부를 차근차근 진행해봐요!")
        st.info("추천 활동: 교과서 복습, 단어 암기, 문제집 풀기")
    elif mood == "😴 피곤해":
        st.warning("🌙 오늘은 컨디션이 별로네요. 무리하지 말고 가볍게 복습만 해요!")
        st.info("추천 활동: 노트 정리, 오답노트, 플래시카드 학습")

    # 랜덤 응원 메시지
    quotes = [
        "🌱 오늘의 작은 성취가 내일의 큰 변화를 만든다!",
        "🚀 지금의 노력이 미래의 너를 만든다!",
        "💡 포기하지 않는 한, 실패는 없다!",
        "✨ 네가 하는 모든 공부는 쌓이고 있어!"
    ]
    st.markdown(f"**오늘의 응원 한마디:** {random.choice(quotes)}")
