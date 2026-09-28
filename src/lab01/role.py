from src.utils import openai_client


def main():
    response = openai_client.responses.create(
        model='gpt-5.6-luna',
        input=[
            {
                'role': 'system',
                # 'content': '너는 백설공주에 나오는 마법거울이야. 마법거울이 얘기하듯 답변해줘.',
                'content': '너는 영화 배트맨의 조커야. 조커 캐릭터처럼 답변해줘.'
            },
            {
                'role': 'user',
                'content': '세상에서 누가 제일 예쁘니?',
            },
        ]
    )
    print(response.output_text)


if __name__ == '__main__':
    main()
