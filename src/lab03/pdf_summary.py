import pymupdf

from src.utils import openai_client


def pdf_to_text(pdf_file, header_height=80, footer_height=80):
    """
    PDF 파일을 오픈해서, 헤더/푸터를 제외한 영역에서 텍스트만 추출. 추출한 텍스트를 리턴.

    Args:
        pdf_file: str. 오픈할 PDF 파일의 경로.
        header_height: int. PDF 파일에서 헤더의 높이. 기본값은 80.
        footer_height: int. PDF 파일에서 푸터의 높이. 기본값은 80.
    Returns:
        PDF에서 헤더/푸터를 제외한 클립 영역에서 추축한 텍스트(str)를 리턴.
    """

    full_text = ''  # 추출한 텍스트를 append하고 리턴하기 위해서.
    with pymupdf.open(pdf_file) as document:  # pdf 파일 열기
        for page in document:  # pdf 문서에서 페이지 별로 반복
            rect = page.rect  # 문서의 크기(width, height), (좌상단, 우하단) 좌표 정보
            # clip: PDF에서 잘라낼 영역(헤더와 푸터를 제외한 영역) -> 텍스트 추출할 영역
            clip = (0, header_height, rect.width, rect.height - footer_height)
            txt = page.get_text(clip=clip)  # clip 영역에서만 텍스트를 추출
            full_text += txt  # 추출한 텍스트를 이어붙임.
            full_text += '\n' + '-' * 80 + '\n\n'  # 페이지 구분자

    return full_text


def summarize_text(txt_file):
    """
    텍스트 파일을 읽고, OpenAI API를 사용해서 텍스트 요약 작업을 수행. GPT의 답변을 리턴.

    Args:
        txt_file: str. 읽을 텍스트 파일의 경로.
    Returns:
        GPT의 답변(str).
    """

    with open(txt_file, encoding='utf-8') as f:  # 텍스트 파일 오픈.
        txt = f.read()  # 텍스트 파일 전체를 읽음.

    # GPT를 사용하기 위한 프롬프트 작성
    prompt = f'''
    너는 문서을 읽고, 주제, 내용, 목적 등을 파악하고 요약할 수 있는 AI 비서야.
    아래의 텍스트를 읽고, 저자의 목적과 주장을 파악해서 요약해줘.
    출력 포맷은 다음과 같이 해줘.
    # 논문 제목
    # 논문의 목적(5문장 이내)
    # 논문 요약(20문장 이내)
    # 저자 소개
    # 참고 문헌
    
    ===== 아래 텍스트 =====
    {txt}
    '''

    # GPT에게 질문하고 답변을 받음
    response = openai_client.responses.create(
        model='gpt-6-luna',
        input=[{'role': 'user', 'content': prompt}]
    )

    return response.output_text


def write_text_file(file_name, text):
    """텍스트를 파일에 저장.

    Args:
        file_name: str. 저장할 파일 경로.
        text: str. 파일에 쓸 내용.
    """

    with open(file_name, mode='w', encoding='utf-8') as f:
        f.write(text)


def main():
    # 원본 PDF 파일 경로
    pdf_file = 'C:/workspaces/lab_llm/data/sample.pdf'
    # PDF 파일에서 추출한 텍스트를 저장할 파일 경로
    pdf_txt_file = 'C:/workspaces/lab_llm/output/pdf_to_text.txt'
    # GPT가 요약한 텍스트를 저장할 파일 경로
    pdf_summary_file = 'C:/workspaces/lab_llm/output/pdf_summary.txt'

    # PDF 파일 오픈 -> 헤더/푸터를 제외한 영역에서 텍스트 추출
    pdf_text = pdf_to_text(pdf_file)
    # print(pdf_text)
    # PDF에서 추출된 텍스트를 파일에 씀.
    write_text_file(pdf_txt_file, pdf_text)

    # PDF에서 추출한 텍스트를 GPT에게 요약하라고 요청, 결과 출력
    answer = summarize_text(pdf_txt_file)
    print(answer)

    # GPT의 답변(문서 요약 결과)를 텍스트 파일로 저장
    write_text_file(pdf_summary_file, answer)


if __name__ == '__main__':
    main()
