from src.utils import openai_client


def main():
    print('===== MyGPT =====')
    print('종료하려면 "/exit" 입력하세요.')

    messages = []  # 대화 내용 이력을 저장하기 위한 리스트

    while True:
        user_input = input('사용자>> ').strip()
        if user_input == '/exit':
            print('대화를 종료합니다...')
            break

        # 사용자가 입력한 내용을 대화 이력에 추가.
        messages.append(
            {'role': 'user', 'content': user_input,}
        )

        stream = openai_client.responses.create(
            model='gpt-5.6-luna',
            input=messages,
            stream=True  # 스트리밍 방식으로 답변을 받기 위해서.
        )
        for event in stream:
            if event.type == 'response.output_text.delta':
                print(event.delta, end='')

            # print(event)  # 이벤트 내용을 읽기가 힘듦.
            # print(event.__class__.__name__, event.to_json())  # 이벤트 내용을 읽기 쉽게 하기 위해서
            # print('-' * 50)
            # ResponseCreatedEvent
            # -> ResponseInProgressEvent
            # -> ResponseOutputItemAddedEvent
            # -> ResponseContentPartAddedEvent
            # -> ResponseTextDeltaEvent
            # -> ResponseTextDeltaEvent
            # -> ...
            # -> ResponseTextDoneEvent
            # -> ResponseContentPartDoneEvent
            # -> ResponseOutputItemDoneEvent
            # -> ResponseCompletedEvent

        print()  # 답변의 조각들을 모두 출력한 다음에 줄바꿈을 넣기 위해서


if __name__ == '__main__':
    main()
