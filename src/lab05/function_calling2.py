from src.lab05.gpt_functions import tools
from src.utils import openai_client, my_logger


def main():
    messages = [
        {
            'role': 'system',
            'content': '너는 사용자의 질문에 대한 답변을 정확하고 친절하게 생성하는 AI 비서야.',
        }
    ]

    print('===== My GPT APP =====')
    print('종료하려면 "/exit"을 입력하세요.')

    while True:
        user_input = input('사용자>> ').strip()
        if user_input == '/exit':
            print('대화를 종료합니다...')
            break  # while 반복문을 종료
        elif user_input == '':  # 사용자가 공백 이외의 문자는 입력하지 않은 경우.
            continue  # while 반복문을 다시 처음부터 시작.

        # 사용자의 입력(질문)을 대화 이력에 추가
        messages.append({
            'role': 'user',
            'content': user_input,
        })

        # GPT에게 질문을 보내고 답변을 받음
        response = openai_client.responses.create(
            model='gpt-6-luna',
            input=messages,
            tools=tools  # GPT에게 제공할 도구 목록
        )

        # 대화 내용을 기억하기 위해서 GPT 답변 내용을 대화 이력에 추가
        messages.extend(response.output)
        for msg in messages:
            my_logger(msg)

        print('AI>>', response.output_text)


if __name__ == '__main__':
    main()
