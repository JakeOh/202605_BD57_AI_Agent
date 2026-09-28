from src.utils import openai_client


def main():
    print('===== MyGPT 에이전트 =====')
    print('종료하려면 "/exit"을 입력하세요.\n')

    # 사용자 질문과 AI의 답변을 순서대로 저장하기 위한 리스트
    messages = [
        {
            'role': 'system',
            'content': '너는 사용자의 질문에 정확하고 친절한 답변을 만들어 주는 AI 비서야.',
        },
    ]

    while True:
        # 콘솔에서 사용자 입력(질문)을 받음.
        user_input = input('사용자>> ').strip()
        if user_input == '/exit':
            print('MyGPT 에이전트를 종료합니다...')
            break

        # prompt 딕셔너리(role=user, content=입력)를 만들어서 messages 리스트에 추가.
        messages.append({
            'role': 'user',
            'content': user_input,
        })

        # AI에게 messages를 보내고 응답을 받음.
        response = openai_client.responses.create(
            model='gpt-5.6-luna',
            input=messages
        )

        # 응답을 출력
        print('AI비서>>', response.output_text)

        # AI가 이전의 대화 내용을 기억하도록 하기 위해서
        # messages 리스트에 prompt 딕셔너리(role=assistant, content=답변)를 추가.
        messages.append({
            'role': 'assistant',
            'content': response.output_text,
        })


if __name__ == '__main__':
    main()
