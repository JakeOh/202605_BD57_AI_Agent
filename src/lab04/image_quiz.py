import base64
from glob import glob
from pathlib import Path

from src.utils import openai_client


def base64_encode_image(image_path):
    """이미지 파일을 읽고 base64 방식으로 인코딩된 문자열을 utf-8로 변환해서 리턴."""

    with open(image_path, mode='rb') as f:
        data = f.read()

    return base64.b64encode(data).decode(encoding='utf-8')


def generate_image_quiz(image_path):
    """이미지 파일에 대해서 퀴즈 문제를 생성하도록 GPT에게 요청하고 답변을 받음.
    GPT가 생성한 문제/정답/설명(str)을 리턴."""

    # 이미지 바이너리 데이터를 base64 인코딩된 문자열로 변환
    encoded = base64_encode_image(image_path)

    # 퀴즈 문제, 답변, 설명을 생성하도록 하는 프롬프트를 작성.
    quiz_prompt = '''
    제공된 이미지를 바탕으로 다음과 같은 형식으로 퀴즈를 작성해줘.
    (1) ~ (4) 4개의 보기들 중에서 하나만 정답이 되도록 문제를 출제해줘.
    문제 정답 번호들은 랜덤하게 배치되어야 해.
    문제와 함께 정답 번호와 정답인 이유를 설명해야 해.
    문제 출력 형식은 아래와 같이 작성해줘.
    
    ===== 출력 예시 =====
    **Q. 다음 이미지에 대한 설명으로 옳지 않은 것은?**
    (1) 보기 1
    (2) 보기 2
    (3) 보기 3
    (4) 보기 4
    
    **A. (1)**
    **설명:** (1)이 정답인 이유 설명
    '''

    messages = [
        {
            'role': 'user',
            'content': [
                {
                    'type': 'input_text',
                    'text': quiz_prompt,
                },
                {
                    'type': 'input_image',
                    'image_url': f'data:image/jpg;base64,{encoded}',
                },
            ],
        },
    ]

    # GPT에게 퀴즈 문제 생성을 요청
    response = openai_client.responses.create(
        model='gpt-6-luna',
        input=messages
    )

    return response.output_text


def write_markdown_file(md_file, content):
    """컨텐트(문자열)을 markdown 형식의 파일에 씀."""

    with open(md_file, mode='at', encoding='utf-8') as f:
        f.write(content)


def main():
    # 이미지 파일들이 저장된 경로
    image_paths = 'C:/workspaces/lab_llm/data/images/*.jpg'

    # 마크다운 파일 경로
    md_file_path = 'C:/workspaces/lab_llm/output/quiz.md'

    # glob(): 패턴이 일치하는 파일 경로들을 찾아줌.
    for i, path in enumerate(glob(image_paths)):
        print(path)
        answer = generate_image_quiz(path)
        print(answer)
        # md 파일의 위치에서부터 이미지 파일의 상대경로
        relative_path = "../data/images/" + Path(path).name
        content = f'# 문제 {i+1}\n\n![문제에 사용된 이미지]({relative_path})\n\n{answer}\n\n'
        write_markdown_file(md_file_path, content)


if __name__ == '__main__':
    main()
