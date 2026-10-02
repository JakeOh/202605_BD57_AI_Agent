from src.utils import openai_client, my_logger


def main():
    response = openai_client.responses.create(
        model='gpt-6-luna',
        # input='2026 아시안게임 1위 국가는?'
        input='서울과 런던의 현재 시간은?',

        # AI가 사용할 수 있는 도구 목록을 제공
        tools=[
            {'type': 'web_search'}
        ]
    )
    my_logger(response)

    print(response.output_text)


if __name__ == '__main__':
    main()
