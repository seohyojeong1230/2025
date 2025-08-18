import streamlit as st

# 🎨 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천 🌟", page_icon="🌈", layout="centered")

# 🌟 타이틀
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🔮 MBTI 기반 진로 추천 🌈</h1>", unsafe_allow_html=True)
st.write("당신의 성격 유형에 따라 잘 맞는 진로를 찾아보세요! ✨")

# 💡 MBTI별 진로 데이터
career_dict = {
    "INTJ": ["🧪 과학자", "📊 전략가", "⚙️ 공학자"],
    "ENTP": ["🚀 기업가", "📣 마케터", "🧩 기획자"],
    "INFJ": ["🧘 심리상담가", "✍️ 작가", "👩‍🏫 교육자"],
    "ESFP": ["🎭 배우", "🎨 디자이너", "🎉 이벤트 플래너"]
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
