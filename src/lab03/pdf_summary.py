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
    pass


def summarize_text(txt_file):
    """
    텍스트 파일을 읽고, OpenAI API를 사용해서 텍스트 요약 작업을 수행. GPT의 답변을 리턴.

    Args:
        txt_file: str. 읽을 텍스트 파일의 경로.
    Returns:
        GPT의 답변.
    """
    pass


def write_text_file(file_name, text):
    with open(file_name, mode='w', encoding='utf-8') as f:
        f.write(text)


def main():
    # PDF 파일 오픈 -> 헤더/푸터를 제외한 영역에서 텍스트 추출
    # PDF에서 추출한 텍스트를 GPT에게 요약하라고 요청, 결과 출력
    # GPT가 요청한 결과를 텍스트 파일로 저장
    pass


if __name__ == '__main__':
    main()
