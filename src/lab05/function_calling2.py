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

        print('TODO: GPT 답변을 받음')


if __name__ == '__main__':
    main()
