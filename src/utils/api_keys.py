import os

from dotenv import load_dotenv


def get_openai_api_key():
    # 프로젝트 폴더(lab_llm) 아래에 있는 .env 파일의 내용을 읽어서 OS 환경 변수로 저장.
    load_dotenv()

    # OS 환경 변수(key-value)에 저장된 값을 읽음.
    api_key = os.getenv('OPENAI_API_KEY')

    return api_key