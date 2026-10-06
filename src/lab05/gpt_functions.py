import pytz  # 타임존
from datetime import datetime  # 날짜/시간
import yfinance as yf  # Yahoo Finance


def get_current_time(timezone):
    """
    해당 timezone의 현재 날짜와 시간을 %Y-%m-%d %H:%M:%S 형식의 문자열로 리턴.

    :param timezone: 타임존을 표시하는 문자열. (예) Asia/Seoul, Europe/Londone.
    pytz.all_timezones에서 정의된 문자열을 사용.

    :return: %Y-%m-%d %H:%M:%S 형식의 문자열
    """
    tz = pytz.timezone(timezone)  # 문자열을 타임존 객체로 변환
    now = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')  # 해당 타임존의 현재 날짜/시간
    return now


def get_yf_info(ticker):
    """
    ticker 문자열(종목 코드)를 아규먼트로 전달받아서, 그 기업의 정보를 문자열로 리턴.

    :param ticker: Yahoo Finance에서 기업 정보를 반환하기 위해서 필요한 종목 문자열.
    (예) AAPL, MSFT, 005930.KS

    :return: 기업 정보 문자열.
    """
    stock = yf.Ticker(ticker)  # Ticker 객체 생성
    info = stock.info  # Python dict 객체
    return str(info)  # dict를 문자열로 변환해서 리턴.


if __name__ == '__main__':
    # print(pytz.all_timezones)

    # print(get_current_time('Asia/Seoul'))
    # print(get_current_time('Europe/London'))

    # print(get_yf_info('AAPL'))  # 애플
    # print(type(get_yf_info('AAPL')))
    print((get_yf_info('005930.KS')))  # 삼성전자
