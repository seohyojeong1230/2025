import streamlit as st
import random

st.set_page_config(page_title="공부 스타일 테스트 🧩", page_icon="📚", layout="centered")

# 제목
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🧩 나의 공부 스타일 테스트 🎓</h1>", unsafe_allow_html=True)
st.write("몇 가지 질문에 답해보면, 너만의 공부 스타일과 맞춤형 공부법을 알려줄게요! ✨")

# 질문들
q1 = st.radio("1️⃣ 공부할 때 나는?", ["아침에 집중 잘됨 🌅", "밤에 집중 잘됨 🌙"])
q2 = st.radio("2️⃣ 수업 정리 방식은?", ["노트 필기 ✏️", "머릿속으로 이해 🧠"])
q3 = st.radio("3️⃣ 공부할 때 더 좋은 건?", ["혼자 조용히 🧘", "같이 토론하며 💬"])
q4 = st.radio("4️⃣ 시험 준비는?", ["계획 세워서 차근차근 📅", "벼락치기 파워 ⚡"])

if st.button("👉 결과 보기"):
    # 결과 판별 로직 (간단히 if 조합)
    style = ""
    if q1 == "아침에 집중 잘됨 🌅": style += "아침형 "
    else: style += "야행성 "
    
    if q2 == "노트 필기 ✏️": style += "정리왕 "
    else: style += "직관형 "
    
    if q3 == "혼자 조용히 🧘": style += "개인학습형 "
    else: style += "토론형 "
    
    if q4 == "계획 세워서 차근차근 📅": style += "계획러"
    else: style += "즉흥러"

    st.subheader(f"✨ 너의 공부 스타일은: **{style}** ✨")

    # 맞춤형 공부법 추천
    tips = {
        "아침형": "📅 아침 시간을 활용해 중요한 공부를 먼저 해보세요!",
        "야행성": "🌙 밤에 집중 잘 되니, 복습 위주로 활용해보세요!",
        "정리왕": "✏️ 컬러펜, 마인드맵을 활용하면 효과 만점!",
        "직관형": "⚡ 개념을 빠르게 이해하고 문제풀이로 확인하세요!",
        "개인학습형": "📚 혼자 문제집 풀고 스스로 점검하는 방식이 잘 맞아요!",
        "토론형": "💬 스터디 그룹을 만들어 서로 설명해보세요!",
        "계획러": "📅 공부계획표를 만들고 체크하면서 성취감을 느껴보세요!",
        "즉흥러": "🎲 짧게 집중하고 자주 휴식! 게임처럼 공부하면 효과적이에요!"
    }

    st.markdown("### 📌 맞춤형 공부법 추천")
    for keyword in style.split():
        if keyword in tips:
            st.markdown(f"- {tips[keyword]}")

    # 랜덤 응원 메시지
    quotes = [
        "🌱 오늘의 작은 성취가 내일의 큰 변화를 만든다!",
        "🚀 지금의 노력이 미래의 너를 만든다!",
        "💡 포기하지 않는 한, 실패는 없다!"
    ]
    st.success(f"오늘의 응원 한마디: {random.choice(quotes)}")
