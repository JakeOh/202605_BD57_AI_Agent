from src.utils import openai_client


def main():
    # no prompting: AI 에이전트에게 전달하는 메시지에 assistant 프롬프트를 제공하지 않는 것.
    no_prompt_msg = [
        {
            'role': 'system', 'content': '유치원생처럼 대답해줘.',
        },
        {
            'role': 'user', 'content': '오리',
        },
    ]

    response = openai_client.responses.create(
        model='gpt-5.6-luna',
        input=no_prompt_msg
    )
    # print(response)  # 에이전트의 응답(Response) 객체
    # print(response.to_json())  # Response 객체를 읽기 쉽게 JSON 형식으로 출력
    print(response.output_text)  # 에이전트가 생성한 답변만 출력

    print('-' * 50)

    # One-Shot Prompting: user-assistant 프롬프트를 한 개를 작성하고 질문을 작성.
    # AI 에이전트가 사용자가 원하는 답변의 패턴에 맞춰서 텍스트를 생성하도록 예시를 한 번만 제시하고 답변을 유도.
    one_shot_prompt_msg = [
        {
            'role': 'system', 'content': '유치원생처럼 대답해줘.',
        },
        {
            'role': 'user', 'content': '참새',
        },
        {
            'role': 'assistant', 'content': '짹짹',
        },
        {
            'role': 'user', 'content': '오리',
        },
    ]
    response = openai_client.responses.create(
        model='gpt-5.6-luna',
        input=one_shot_prompt_msg
    )
    print(response.output_text)

    print('-' * 50)

    # Few-Shot Prompting: 원하는 형식의 답변을 유도하기 위해서 user-assistant 프롬프트 예시를 여러 개 전달하는 방식.
    few_shot_prompt_msg = [
        {'role': 'system', 'content': '유치원생처럼 대답해줘.',},
        {'role': 'user', 'content': '참새',},
        {'role': 'assistant', 'content': '짹짹',},
        {'role': 'user', 'content': '개구리',},
        {'role': 'assistant', 'content': '개굴개굴',},
        {'role': 'user', 'content': '강아지',},
        {'role': 'assistant', 'content': '멍멍',},
        {'role': 'user', 'content': '오리'},
    ]
    response = openai_client.responses.create(
        model='gpt-5.6-luna',
        input=few_shot_prompt_msg
    )
    print(response.output_text)


if __name__ == '__main__':
    main()
