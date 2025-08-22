# fitness_diet_app_detailed.py
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
        exercise = """
        - 🏃 유산소: 빠르게 걷기/조깅/자전거 (주 4\~5회, 30\~40분)  
        - 🏋 근력: 스쿼트, 푸시업, 덤벨 운동 (주 2\~3회, 30분)  
        - 🤸 스트레칭: 운동 후 10분
        """
    elif goal == "체중 증량":
        exercise = """
        - 🏋 근력: 대근육 위주(스쿼트, 벤치프레스, 데드리프트) (주 3\~4회, 40\~60분)  
        - 🏃 가벼운 유산소: 걷기/자전거 (주 2회, 20분)  
        - 🤸 스트레칭: 운동 후 10분
        """
    else:
        exercise = """
        - 🏃 유산소: 가벼운 조깅, 자전거 (주 3회, 20\~30분)  
        - 🏋 근력: 전신 근력운동 (주 2\~3회, 30분)  
        - 🤸 스트레칭: 매일 10분
        """

    # 활동 수준 보정
    if activity_level == "저활동":
        tip = "👉 지금보다 활동량을 조금 늘려보세요! (엘리베이터 대신 계단)"
    elif activity_level == "보통":
        tip = "👉 현재 활동량을 유지하면서 꾸준히 실천하세요!"
    else:
        tip = "👉 아주 좋아요! 근력운동을 조금 더 추가하면 효과적이에요!"

    # 식단 추천
    if goal == "체중 감량":
        diet = """
        - 🍚 탄수화물: 현미밥, 고구마, 귀리 (적당량)  
        - 🍗 단백질: 닭가슴살, 두부, 달걀, 흰살생선  
        - 🥦 채소: 샐러드, 나물, 제철 채소 충분히 섭취  
        - ❌ 피해야 할 것: 음료수, 과자, 튀김류  

        📌 예시 식단
        - 🥣 아침: 오트밀 + 삶은 달걀 2개 + 방울토마토  
        - 🍲 점심: 현미밥 + 닭가슴살 구이 + 시금치나물  
        - 🍛 저녁: 고구마 + 연어구이 + 샐러드
        """
    elif goal == "체중 증량":
        diet = """
        - 🍚 탄수화물: 현미밥, 감자, 파스타 (충분히)  
        - 🍗 단백질: 소고기, 연어, 달걀, 두부  
        - 🥜 건강한 지방: 아보카도, 견과류, 올리브유  
        - 🥛 간식: 그릭요거트, 단백질 쉐이크  

        📌 예시 식단
        - 🥣 아침: 토스트 + 스크램블에그 + 우유  
        - 🍲 점심: 파스타 + 소고기 스테이크 + 샐러드  
        - 🍛 저녁: 현미밥 + 연어 + 아보카도 + 두부조림
        """
    else:  # 유지
        diet = """
        - 🍚 탄수화물: 밥, 고구마, 통곡물 (균형 있게)  
        - 🍗 단백질: 생선, 닭가슴살, 두부  
        - 🥦 채소 & 과일: 매 끼니 채소 포함, 과일 하루 1~2회  
        - 💧 수분: 물 하루 1.5~2L  

        📌 예시 식단
        - 🥣 아침: 현미밥 + 달걀찜 + 나물 + 사과  
        - 🍲 점심: 닭가슴살 샐러드 + 고구마 + 두유  
        - 🍛 저녁: 연어구이 + 현미밥 + 찐 채소 + 방울토마토
        """

    # 결과 출력
    st.subheader(f"🎯 목표: {goal}")
    st.markdown("### ✅ 운동 추천")
    st.markdown(exercise)

    st.info(tip)

    st.markdown("### 🥗 식단 추천")
    st.markdown(diet)
