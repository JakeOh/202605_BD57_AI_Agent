import streamlit as st

from src.utils import openai_client


def main():
    st.title('🍕 My GPT Chatbot')
    st.write('GPT API를 사용한 챗봇')

    # 대화 내용을 저장하는 리스트를 session_state에 생성.
    # 앱이 실행되는 동안 대화 내용 리스트가 리셋되면 안되기 때문에. 내용을 계속 유지해야 하기 때문에.
    if 'messages' not in st.session_state:
        # session_state에 messages가 없으면
        # 앱이 처음 실행됐을 때만 실행.
        st.session_state.messages = [
            {
                'role': 'system',
                'content': '너는 사용자의 질문에 정확한 답변을 친절하게 제공하는 유능한 AI 비서야.',
            },
            {
                'role': 'assistant',
                'content': '무엇을 도와드릴까요?',
            },
        ]

    # messages 리스트에서 아이템(dict)을 하나씩 꺼내서 반복
    for msg in st.session_state.messages:
        # 딕셔너리 키가 assistant 또는 user인 경우에
        if msg['role'] in ('assistant', 'user'):
            # 채팅 메시지(아이콘/내용)를 출력
            st.chat_message(msg['role']).write(msg['content'])

    # 사용자가 질문을 입력할 수 있는 입력창을 보여줌.
    # user_input = st.chat_input('질문을 입력하세요.')
    # if user_input:
    #     pass
    if user_input := st.chat_input('질문을 입력하세요.'):
        # 사용자가 질문을 입력(enter)했을 때
        # 사용자가 입력한 내용을 화면에 채팅 메시지 형식(아이콘/내용)으로 출력
        st.chat_message('user').write(user_input)

        # session_state의 message 리스트에 사용자의 질문을 딕셔너리로 추가.
        st.session_state.messages.append(
            {'role': 'user', 'content': user_input,}
        )

        # AI에게 메시지(질문)를 보내고 응답을 받음
        response = openai_client.responses.create(
            model='gpt-5.6-luna',
            input=st.session_state.messages
        )
        # AI가 보내준 답변을 화면에 출력
        st.chat_message('assistant').write(response.output_text)

        # AI가 보내준 답변을 messages 리스트에 추가(그 다음 대화를 이어갈 때 대화 이력을 기억하기 위해서)
        st.session_state.messages.append(
            {'role': 'assistant', 'content': response.output_text,}
        )


if __name__ == '__main__':
    main()
