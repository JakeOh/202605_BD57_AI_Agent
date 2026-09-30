# PDF 파일에서 헤더(header)와 푸터(footer) 정보를 제거하고 본문 텍스트만 추출하기

import pymupdf


def main():
    # 원본 PDF 파일 경로
    pdf_file = 'C:/workspaces/lab_llm/data/sample.pdf'
    # 헤더와 푸터를 제외하고 추출한 텍스트를 저장할 파일 경로
    summary_file = 'C:/workspaces/lab_llm/output/pdf_summary_2.txt'
    # PDF 파일의 헤더 높이(세로 길이)
    header_height = 80
    # PDF 파일의 푸터 높이(세로 길이)
    footer_height = 80
    # 추출한 텍스트들을 저장하기 위한 문자열
    full_text = ''

    # PDF 파일 열기
    with pymupdf.open(pdf_file) as document:
        for page in document:
            rect = page.rect
            # print(rect, rect.width, rect.height)
            # clip: PDF 파일에서 헤더와 푸터를 제외하고 잘라낼 영역
            # clip = (좌상단 x좌표, 좌상단 y좌표, 우하단 x좌표, 우하단 y좌표)
            clip = (0, header_height, rect.width, rect.height - footer_height)
            # 잘려진 영역(clip) 안에서만 텍스트를 추출
            txt = page.get_text(clip=clip)
            full_text += txt
            full_text += '\n' + '-' * 80 + '\n\n'

    # 추출한 텍스트를 txt 파일로 저장.
    with open(summary_file, mode='w', encoding='utf-8') as f:
        f.write(full_text)
        print('텍스트 추출 성공')


if __name__ == '__main__':
    main()
