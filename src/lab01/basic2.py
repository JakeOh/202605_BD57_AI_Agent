from src.utils import openai_client


def main():
    response = openai_client.responses.create(
        model='gpt-5.6-luna',
        input='너에 대해서 소개해줘.'
    )
    print(response.output_text)


if __name__ == '__main__':
    main()
