# fitness_diet_app.py
import streamlit as st

st.title("🏃 개인별 운동 & 식단 추천 앱")

# 입력값
age = st.number_input("나이", min_value=10, max_value=90, value=25)
sex = st.selectbox("성별", ["남성", "여성"])
weight = st.number_input("현재 체중(kg)", min_value=30.0, max_value=200.0, value=70.0)
target_weight = st.number_input("목표 체중(kg)", min_value=30.0, max_value=200.0, value=65.0)
activity_level = st.selectbox("현재 활동 수준", ["저활동", "보통", "활동적"])

if st.button("추천 받기"):
    # 목표 분류
    if target_weight < weight:
        goal = "체중 감량"
    elif target_weight > weight:
        goal = "체중 증량"
    else:
        goal = "체중 유지"

    # 운동 추천
    if goal == "체중 감량":
        exercise = "빠르게 걷기, 가벼운 조깅, 자전거 타기 (주 4~5회, 30분 이상)"
    elif goal == "체중 증량":
        exercise = "근력운동(스쿼트, 푸시업, 덤벨 운동 등) (주 3~4회, 40분 이상)"
    else:
        exercise = "걷기, 가벼운 근력운동, 스트레칭 (주 3회 이상, 20~30분)"

    # 활동 수준 보정
    if activity_level == "저활동":
        tip = "👉 지금보다 활동량을 조금 늘려보세요!"
    elif activity_level == "보통":
        tip = "👉 현재 활동량을 유지하면서 꾸준히 실천하세요!"
    else:
        tip = "👉 아주 좋아요! 근력운동을 추가해도 좋아요!"

    # 식단 추천
    if goal == "체중 감량":
        diet = """
        - 🍚 탄수화물: 현미밥, 고구마, 귀리 (적당량)  
        - 🍗 단백질: 닭가슴살, 두부, 달걀, 생선  
        - 🥦 채소: 샐러드, 나물, 제철 채소 충분히 섭취  
        - ❌ 피해야 할 것: 음료수, 과자, 튀김류
        """
    elif goal == "체중 증량":
        diet = """
        - 🍚 탄수화물: 현미밥, 감자, 파스타 (충분히)  
        - 🍗 단백질: 소고기, 연어, 두부, 달걀  
        - 🥜 건강한 지방: 아보카도, 견과류, 올리브유  
        - 🥛 간식: 그릭요거트, 단백질 쉐이크
        """
    else:
        diet = """
        - 🍚 탄수화물: 밥, 고구마, 통곡물 (균형 있게)  
        - 🍗 단백질: 생선, 닭가슴살, 두부  
        - 🥦 채소 & 과일: 매 끼니 채소 포함, 과일 하루 1~2회  
        - 💧 수분: 물 하루 1.5~2L
        """

    # 결과 출력
    st.subheader(f"🎯 목표: {goal}")
    st.write(f"✅ 운동 추천: {exercise}")
    st.info(tip)

    st.subheader("🥗 식단 추천")
    st.markdown(diet)
