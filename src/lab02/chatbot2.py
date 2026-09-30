import streamlit as st

from src.utils import openai_client


def main():
    st.title('💬 GPT 흉내내기')

    # session_state에 'messages' 키가 없을 때(messages 속성이 생성되지 않았을 때)
    # 대화 내용(user-assistant)을 저장하기 위한 리스트를 초기화
    if 'messages' not in st.session_state:
        st.session_state.messages = [
            {'role': 'assistant', 'content': '무엇을 도와드릴까요?',}
        ]

    # session_state.messages 리스트에 저장된 대화 이력을 화면에 보여줌.
    for msg in st.session_state.messages:
        if msg['role'] in ('assistant', 'user'):
            # st.chat_message(msg['role']).markdown(msg['content'])
            with st.chat_message(msg['role']):
                st.markdown(msg['content'])

    # 사용자 채팅 입력창을 보여줌
    if user_input := st.chat_input(placeholder='질문을 입력하세요.'):
        # 사용자 입력 이벤트가 발생했을 때(사용자가 질문을 작성하고 엔터를 입력했을 때)
        # 사용자가 입력한 내용을 화면에 출력
        # st.chat_message('user').markdown(user_input)
        with st.chat_message('user'):
            st.markdown(user_input)

        # messages 리스트에 사용자 role의 메시지를 추가
        st.session_state.messages.append(
            {'role': 'user', 'content': user_input,}
        )

        # GPT에게 요청을 보내고 답변을 스트리밍 방식으로 받음
        stream = openai_client.responses.create(
            model='gpt-6-luna',
            input=st.session_state.messages,
            stream=True
        )

        with st.chat_message('assistant').empty():
            ai_answer = ''  # 조각난 답변(delta)들을 합쳐서 하나의 문자열로 만들기 위해서
            for event in stream:
                if event.type == 'response.output_text.delta':
                    # 이벤트가 답변 조각들 보내주는 이벤트일 때
                    ai_answer += event.delta
                    st.markdown(ai_answer)
                elif event.type == 'response.completed':
                    # 이벤트가 답변이 끝났다는 이벤트일 때
                    # 대화 내용을 기억하기 위해서 messages 리스트에 추가.
                    st.session_state.messages.append(
                        {'role': 'assistant', 'content': event.response.output_text,}
                    )


if __name__ == '__main__':
    main()
