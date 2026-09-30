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
            model='gpt-6-luna',
            input=messages,
            stream=True  # 스트리밍 방식으로 답변을 받기 위해서.
        )
        for event in stream:  # 답변이 조금씩 잘려서 올 때마다 반복
            if event.type == 'response.output_text.delta':
                # 답변 내용이 조금씩 잘려서 오는 이벤트일 때
                print(event.delta, end='')
            elif event.type == 'response.completed':  # 응답(답변) 종료 이벤트일 때
                # 대화 내용(user 질문 -> assistant 답변 -> user 질문 -> assistant 답변 -> ...)을 리스트에 추가
                messages.append(
                    {'role': 'assistant', 'content': event.response.output_text, }
                )

            # print(event)  # 이벤트 내용을 읽기가 힘듦.
            # print(event.__class__.__name__, event.to_json())  # 이벤트 내용을 읽기 쉽게 하기 위해서
            # print('-' * 50)
            # if event.type == 'response.completed':  # 스트리밍 방식에서 가장 마지막 이벤트
            #     print(event.response.output_text)  # 완성된 최종 답변
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
