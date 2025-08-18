import streamlit as st
import random

st.set_page_config(page_title="동물 랜덤 도감 🐾", page_icon="🐼", layout="centered")

st.title("🐾 랜덤 동물 도감")
st.write("버튼을 눌러 오늘의 동물을 만나보세요! 🐶🐱🦊")

# 동물 데이터 (이름 + 설명 + 이미지 URL 교체)
animals = [
    {
        "name": "레서판다 🐼",
        "desc": "세상에서 가장 귀여운 동물 중 하나! 대나무와 과일을 좋아해요 🍎",
        "img": "https://cdn.pixabay.com/photo/2017/04/04/22/29/panda-2202686_1280.jpg"
    },
    {
        "name": "고슴도치 🦔",
        "desc": "작은 몸에 가시를 가진 귀여운 친구! 겁먹으면 몸을 웅크려요 🌰",
        "img": "https://cdn.pixabay.com/photo/2016/04/13/07/18/hedgehog-1323882_1280.jpg"
    },
    {
        "name": "수달 🦦",
        "desc": "장난꾸러기 수영왕! 물에서 노는 걸 제일 좋아해요 🌊",
        "img": "https://cdn.pixabay.com/photo/2016/02/23/17/46/otter-1212010_1280.jpg"
    },
    {
        "name": "펭귄 🐧",
        "desc": "차가운 남극의 귀염둥이! 친구들과 함께 모여 다녀요 ❄️",
        "img": "https://cdn.pixabay.com/photo/2017/03/27/14/56/penguin-2181926_1280.jpg"
    },
    {
        "name": "알파카 🦙",
        "desc": "포근포근 털을 가진 순둥이 동물! 사람들과 잘 어울려요 ☁️",
        "img": "https://cdn.pixabay.com/photo/2017/07/31/11/22/alpaca-2558470_1280.jpg"
    }
]

# 버튼 클릭 시 랜덤 동물 선택
if st.button("🎲 오늘의 동물 보기"):
    animal = random.choice(animals)
    st.subheader(animal["name"])
    st.image(animal["img"], use_column_width=True)
    st.write(animal["desc"])

    # 랜덤 메시지
    messages = [
        "🌟 오늘은 이 동물처럼 귀엽게 살아봐요!",
        "💡 작은 즐거움이 행복을 만든답니다!",
        "🐾 당신도 특별한 존재예요!",
        "✨ 오늘 하루도 반짝이길!"
    ]
    st.success(random.choice(messages))
