# from dotenv import load_dotenv
# load_dotenv()

# from langchain.llms import OpenAI
# llm = OpenAI()
# reulst = llm.predict("내가 좋아하는 동물은")
# print(reulst)

import streamlit as st

from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()

st.title('인공지능 시인')

content = st.text_input('시의 주제를 제시해주세요.')


if st.button('작성요청'):    
    with st.spinner('Wait for it...'):
        result = chat_model.predict(content + "에 대한 시를 써줘")
        st.write(result)

