from openai import OpenAI
from src.utils.api_keys import get_openai_api_key

openai_client = OpenAI(api_key=get_openai_api_key())
print('OpenAI client 생성됨.\n')
