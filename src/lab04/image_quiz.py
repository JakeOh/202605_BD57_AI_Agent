import base64
from glob import glob


def base64_encode_image(image_path):
    """이미지 파일을 읽고 base64 방식으로 인코딩된 문자열을 utf-8로 변환해서 리턴."""
    with open(image_path, mode='rb') as f:
        data = f.read()

    return base64.b64encode(data).decode(encoding='utf-8')


def generate_image_quiz(image_path):
    """이미지 파일에 대해서 퀴즈 문제를 생성하도록 GPT에게 요청하고 답변을 받음.
    GPT가 생성한 문제/정답/설명(str)을 리턴."""
    pass


def write_markdown_file(md_file, content):
    """컨텐트(문자열)을 markdown 형식의 파일에 씀."""
    pass


def main():
    # 이미지 파일들이 저장된 경로
    image_dir = 'C:/workspaces/lab_llm/data/images/*.jpg'
    # glob(): 패턴이 일치하는 파일 경로들을 찾아줌.
    for path in glob(image_dir):
        print(path)
        encoded = base64_encode_image(path)
        print(encoded[:200])
        break


if __name__ == '__main__':
    main()
