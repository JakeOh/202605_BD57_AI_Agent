import json

import streamlit as st

from src.lab05.gpt_functions import tools
from src.utils import openai_client


def main():
    st.title('💬 My GPT 챗봇')

    # 대화 이력은 앱이 실행하는 동안에 계속 유지, 추가되어야 하기 때문에
    # st.session_state에 저장해야 함.
    if 'messages' not in st.session_state:
        # session_state에 messages 속성이 없으면 초기화를 진행.
        st.session_state.messages = [
            {
                'role': 'system',
                'content': '너는 사용자의 질문에 정확하고 친절하게 답변할 수 있는 AI 비서야.',
            }
        ]

    # session_state에 저장돼 있었던 user 또는 assistant 메시지(기존 대화 이력)을 화면에 다시 출력.
    for item in st.session_state.messages:
        # messages에 저장되는 아이템들은 dict 또는 OpenAI의 ResponseOutputMessages 객체일 수 있음.
        # OpenAI 응답 클래스는 파이썬 dict로 변환하는 메서드(model_dump)를 가지고 있음.
        # msg 변수는 dict를 저장하도록.
        msg = item if isinstance(item, dict) else item.model_dump()
        role = msg.get('role')  # 변수 msg는 딕셔너리이기 때문에 get 메서드를 안전하게 호출할 수 있음.
        if role == 'user':
            with st.chat_message(role):
                st.markdown(msg.get('content'))
        elif role == 'assistant':
            with st.chat_message(role):
                st.markdown(msg.get('content')[0].get('text'))
        else:
            continue

    # user_input = st.chat_input()  # 입력창을 보여줌
    # if user_input:  # 입력 이벤트가 발생하면
    if user_input := st.chat_input(placeholder='무엇을 도와드릴까요?'):
        # messages에 사용자의 입력을 추가
        st.session_state.messages.append(
            {'role': 'user', 'content': user_input}
        )
        # 사용자가 입력한 내용을 채팅 메시지 형식으로 화면에 출력
        with st.chat_message('user'):
            st.markdown(user_input)

        for _ in range(5):
            # GPT에 요청(사용자 질문 또는 function_call_output)을 보냄.
            response = openai_client.responses.create(
                model='gpt-6-luna',
                input=st.session_state.messages,
                tools=tools
            )

            # GPT의 응답을 대화 이력에 저장.
            st.session_state.messages.extend(response.output)

            # GPT의 최종답변을 출력
            with st.chat_message('assistant'):
                st.markdown(response.output_text)
            break  # for _ in range(5) 종료
        else:
            print('최대 함수 호출 횟수(5번) 초과!')


if __name__ == '__main__':
    main()