import streamlit as st

# MBTI별 진로 데이터 (간단 예시)
career_dict = {
    "INTJ": ["과학자", "전략가", "공학자"],
    "ENTP": ["기업가", "마케터", "기획자"],
    "INFJ": ["심리상담가", "작가", "교육자"],
    "ESFP": ["배우", "디자이너", "이벤트 플래너"]
}

# 앱 제목
st.title("🔮 MBTI 기반 진로 추천 사이트")
st.subheader("나의 성격 유형으로 적합한 진로를 알아보자!")

# MBTI 선택
mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(career_dict.keys()))

# 결과 출력
if mbti:
    st.write(f"**{mbti} 유형 추천 진로**")
    for job in career_dict[mbti]:
        st.markdown(f"- {job}")

# 추가 설명
st.info("👉 이 결과는 참고용이며, 실제 진로는 본인의 흥미와 가치관에 따라 달라질 수 있습니다.")

