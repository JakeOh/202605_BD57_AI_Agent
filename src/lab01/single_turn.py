from src.utils import openai_client


def main():
    print('===== My GPT 에이전트 =====')
    print('종료하려면 "/exit"을 입력하세요.\n')

    while True:  # 무한 반복문
        # 사용자의 질문 입력을 받음.
        user_input = input('user>> ').strip()
        if user_input == '/exit':
            print('GPT 에이전트를 종료합니다...')
            break  # 무한 반복문을 종료.

        # OpenAI API를 사용해서 사용자가 입력한 질문으로 전송하고 답변을 받음.
        response = openai_client.responses.create(
            model='gpt-5.6-luna',
            input=user_input
        )
        print('MyGPT>>', response.output_text)


if __name__ == '__main__':
    main()
