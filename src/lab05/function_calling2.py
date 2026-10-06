import json

from src.lab05.gpt_functions import tools, available_functions, invoke_function
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

        # GPT가 최종 답변을 생성하기 위해서 도구 호출을 여러번 할 수 있기 때문에,
        # 도구 호출(함수 호출)이 무한 반복되는 것을 방지하기 위해서 함수 호출 횟수는 5번으로 제한.
        for _ in range(5):
            # GPT에게 사용자 질문 또는 함수 호출 결과를 보내고 답변을 받음
            response = openai_client.responses.create(
                model='gpt-6-luna',
                input=messages,
                tools=tools
            )

            # 대화 이력을 기억하기 위해서 GPT의 답변을 messages에 추가.
            # response.output은 리스트(list). 리스트의 원소를 한개씩 추가해야 하기 때문에
            # append가 아니라 extend 메서드를 사용해야 함!
            messages.extend(response.output)
            for msg in messages:
                my_logger(msg)

            # 함수 호출이 있는 경우 처리하기 위해서
            function_calls = [
                item for item in response.output
                if item.type == 'function_call'
            ]

            # 함수 호출이 없는 경우(GPT가 최종 답변을 보내준 경우), 최종 답변을 출력, for 반복문을 종료.
            if not function_calls:
                print('AI>>', response.output_text)
                break  # for _ in range(5) 반복문 종료

            # 함수 호출이 있는 경우, 도구 목록(tools)에 명시된 함수들을 호출하고 다시 요청을 보냄.
            for call in function_calls:
                fn = available_functions.get(call.name)
                if fn is None:  # tools에서 제공되지 않은 함수 이름인 경우
                    my_logger(f'*** 알 수 없는 함수 이름: {call.name}')
                else:  # tools에서 제공된 함수 이름인 경우
                    # 함수를 호출할 때 전달할 아규먼트를 찾음
                    args = json.loads(call.arguments)
                    # 함수를 호출하고 결과를 반환받음
                    # fn_result = fn(**args)
                    fn_result = invoke_function(call.name, args)
                    # 함수 호출 결과를 대화 이력에 추가
                    messages.append({
                        'type': 'function_call_output',
                        'call_id': call.call_id,
                        'output': str(fn_result),
                    })
        else:
            my_logger('*** 최대 함수 호출 횟수(5번)을 초과!!')


if __name__ == '__main__':
    main()
