from src.utils import openai_client


def main():
    # 텍스트 파일이 저장된 경로(절대 경로, absolute path)
    article_path = 'C:/workspaces/lab_llm/data/sample_text.txt'
    with open(article_path, encoding='utf-8') as f:
        txt = f.read()  # 파일 전체를 읽음.
        # print(txt)

    prompt = f'''
    너는 문서를 읽고 요약을 해 줄 수 있는 AI 비서야.
    아래의 글을 읽고 저자의 문제 인식과 주장을 파악하고, 주요 내용을 요약해줘.
    요약하는 내용의 포맷은 다음과 같이 해줘.
    # 제목
    ## 저자의 주장(20문장 이내)
    1. 내용
    2. 내용
    ...
    ## 저자 소개
    
    === 이하 텍스트 ===
    
    {txt}
    '''

    messages = [
        {'role': 'user', 'content': prompt,},
    ]
    response = openai_client.responses.create(
        model='gpt-6-luna',
        input=messages
    )
    print(response.output_text)


if __name__ == '__main__':
    main()
