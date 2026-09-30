import pymupdf


def main():
    # PDF 파일이 저장된 경로
    pdf_path = 'C:/workspaces/lab_llm/data/sample.pdf'

    # PDF 파일 열기
    with pymupdf.open(filename=pdf_path) as document:
        # PDF 파일에서 한 페이지씩 추출한 텍스트를 저장하기 위한 변수
        full_text = ''
        # Document 타입 객체는 iterable 타입(for-in 구문에서 사용 가능)
        # Document 객체를 iteration하면(for-in 반복문에서 사용하면) Page 객체를 줌.
        for page in document:
            full_text += page.get_text()  # 한 페이지에서 텍스트를 추출
            full_text += '\n' + '-' * 80 + '\n'  # 페이지 구분을 위한 구분자 문자열

        print(full_text)


if __name__ == '__main__':
    main()
