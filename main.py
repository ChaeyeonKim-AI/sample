## dotenv 사용 X
# from dotenv import load_dotenv

# load_dotenv()

##1 OPENAI Playground 에서 Complete 버전 구현
# from langchain.llms import OpenAI  # llm 모델(Complete 버전)

# llm = OpenAI()
# result = llm.predict("내가 좋아하는 동물은")
# print(result)

##2 OPENAI Playground 에서 Chat 버전 구현
# from langchain.chat_models import ChatOpenAI  # chat 버전

# chat_model = ChatOpenAI()
# chat_model.predict("hi!")

##3 인공지능 시인 구현

import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.title("인공지능 시인")

content = st.text_input("시의 주제를 제시해주세요.")

if st.button("시 작성 요청하기"):
    with st.spinner("시 작성 중..."):
        result = chat_model.predict(content + "에 대한 시를 써줘")
        st.write(result)
