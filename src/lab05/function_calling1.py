from datetime import datetime

from src.utils import openai_client, my_logger


def get_current_time():
    """현재 날짜와 시간을 '2026-10-02 13:34:30' 형식의 문자열로 만들어서 리턴."""
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return now


def main():
    # AI에게 제공할 도구(함수) 목록을 작성
    tools = [
        {
            'type': 'function',
            'name': 'get_current_time',
            'description': '현재 날짜와 시간을 "%Y-%m-%d %H:%M:%S" 형식의 문자열로 만들어서 리턴.',
        },
    ]

    # AI에게 보낼 메시지(프롬프트)
    messages = [
        {
            'role': 'system',
            'content': '너는 사용자의 질문에 대해서 정확한 답변을 친절하게 작성할 수 있는 AI 비서야.',
        },
        {
            'role': 'user',
            'content': '지금 현재 시간을 알려줘.',
        },
    ]

    response = openai_client.responses.create(
        model='gpt-6-luna',
        input=messages,
        tools=tools  # 우리가 작성한 함수를 AI에게 제공
    )

    # response.output 리스트의 원소들을 한 개씩 추가하기 위해서.
    messages += response.output  # messages.extend(response.output)

    # response.output: list
    for item in response.output:
        my_logger(item)
        if item.type == 'function_call':
            call_id = item.call_id  # 함수 호출 아이디
            fn_name = item.name  # 호출해야 할 함수 이름
            fn_result = get_current_time()  # AI가 호출을 요청한 함수의 리턴값
            # 대화 이력에 함수 호출 결과를 추가
            messages.append(
                {
                    'type': 'function_call_output',
                    'call_id': call_id,
                    'output': fn_result,
                }
            )
            response = openai_client.responses.create(
                model='gpt-6-luna',
                input=messages,
                tools=tools
            )

            my_logger(response.output)


if __name__ == '__main__':
    main()