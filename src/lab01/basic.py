import os

from dotenv import load_dotenv
from openai import OpenAI


def main():
    # 프로젝트 폴더(lab_llm) 아래에 있는 .env 파일의 내용을 읽어서 OS 환경 변수로 저장.
    load_dotenv()

    # OS 환경 변수(key-value)에 저장된 값을 읽음.
    api_key = os.getenv('OPENAI_API_KEY')

    # OpenAI 클라이언트를 생성(AI 에이전트를 생성)
    client = OpenAI(api_key=api_key)

    # OpenAI 클라이언트를 사용해서 GPT에게 요청을 보내고, 응답을 받음.
    response = client.responses.create(
        model='gpt-5.6-luna',
        input='넌 누구니?'
    )
    # print(response.to_json())
    print(response.output_text)  # GPT가 생성한 답변(텍스트)만 출력.


if __name__ == '__main__':
    main()