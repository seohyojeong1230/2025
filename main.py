import streamlit as st

# 🎨 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천 🌟", page_icon="🌈", layout="centered")

# 🌟 타이틀
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🔮 MBTI 기반 진로 추천 🌈</h1>", unsafe_allow_html=True)
st.write("당신의 성격 유형에 따라 잘 맞는 진로를 찾아보세요! ✨")

# 💡 MBTI별 진로 데이터
career_dict = {
    "INTJ": ["🧪 과학자", "📊 전략가", "⚙️ 공학자"],
    "INTP": ["💻 프로그래머", "🔬 연구원", "📚 철학자"],
    "ENTJ": ["🏢 경영자", "🚀 창업가", "📈 컨설턴트"],
    "ENTP": ["🎤 방송인", "📣 마케터", "🧩 기획자"],
    "INFJ": ["🧘 심리상담가", "✍️ 작가", "👩‍🏫 교육자"],
    "INFP": ["🎨 예술가", "🌱 사회운동가", "📖 소설가"],
    "ENFJ": ["🎓 교사", "🗣️ 코치", "🤝 리더"],
    "ENFP": ["🎭 배우", "📺 크리에이터", "🌍 여행 작가"],
    "ISTJ": ["📑 회계사", "⚖️ 판사", "🛠️ 관리자"],
    "ISFJ": ["👩‍⚕️ 간호사", "📚 사서", "🏫 교직원"],
    "ESTJ": ["🕴️ 관리자", "📦 운영 책임자", "🚓 경찰관"],
    "ESFJ": ["💬 상담사", "👩‍🍳 요리사", "🏥 사회복지사"],
    "ISTP": ["🔧 기술자", "🚗 자동차 전문가", "🕹️ 게임 개발자"],
    "ISFP": ["🎶 음악가", "🎨 디자이너", "🌿 환경운동가"],
    "ESTP": ["🏅 운동선수", "💼 세일즈맨", "🎲 모험가"],
    "ESFP": ["🎤 가수", "🎉 이벤트 플래너", "📸 사진작가"]
}

# 🎯 MBTI 선택
st.markdown("### 👉 나의 MBTI를 선택하세요!")
mbti = st.selectbox("🌍 MBTI 유형", list(career_dict.keys()))

# 📌 결과 출력
if mbti:
    st.markdown(f"<h2 style='color: #6A5ACD;'>✨ {mbti} 유형 추천 진로 ✨</h2>", unsafe_allow_html=True)
    for job in career_dict[mbti]:
        st.markdown(f"- {job}")

    # 🎨 멋진 강조 박스
    st.success("🌟 당신의 성격에 딱 맞는 진로예요! 새로운 가능성을 탐험해보세요 🚀")

# 📘 추가 안내
st.info("👉 이 결과는 참고용이며, 실제 진로 선택은 흥미와 가치관에 따라 달라질 수 있어요 💖")

# 🎉 푸터
st.markdown("---")
st.markdown("<p style='text-align: center;'>💡 만든이: <b>MBTI 진로 추천 AI</b> 🌸</p>", unsafe_allow_html=True)
