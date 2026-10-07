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


def get_yf_history(ticker, period):
    """
    ticker(종목코드) 종목의 특정 기간동안의 주가 변화를 마크다운(markdown) 형식의 문자열로 리턴.

    :param ticker: str. 주가를 조회하기 위한 종목 코드. (예) AAPL, 005930.KS.
    :param period: str. 주가 정보를 조회할 기간. (예) 1d, 5d, 1mo, 1y.
    :return: 시가, 고가, 저가, 종가, 거래량, 배당금, 주식분할 정보들을 마크다운 형식의 문자열로 리턴.
    """
    stock = yf.Ticker(ticker)
    history = stock.history(period=period)  #> 리턴 타입: DataFrame

    # pandas.DataFrame.to_markdown() 메서드를 호출하려면 tabulate 패키지가 설치되어 있어야 함.
    return history.to_markdown()  # DataFrame을 마크다운 형식의 문자열로 변환해서 리턴.


def get_yf_recommendations(ticker):
    """
    ticker(종목 코드)에 대한 애널리스트들의 추천 정보(매수, 매도, 유지, ...)를 마크다운 형식의 문자열로 리턴.

    :param ticker: str. 애널리스트의 추천 정보를 구하기 위한 종목 코드. (예) AAPL, 005930.KS.
    :return: 추천 정보(매수, 매도, 유지 등)를 마크다운 형식으로 작성한 문자열.
    """
    stock = yf.Ticker(ticker)
    recommendations = stock.recommendations  # DataFrame
    return recommendations.to_markdown()  # DataFrame을 마크다운 형식의 문자열로 변환해서 리턴.


# 도구 목록에서 사용 가능한 함수 객체들을 찾기 위한 딕셔너리(key: 함수 이름, value: 함수 객체)
available_functions = {
    'get_current_time': get_current_time,
    'get_yf_info': get_yf_info,
    'get_yf_history': get_yf_history,
    'get_yf_recommendations': get_yf_recommendations,
}


# available_functions의 함수를 대신 호출해 주는 편의 함수
def invoke_function(function_name, arguments):
    """
    사용가능한 함수를 찾고, 아규먼트를 전달해서 그 리터값을 반환.

    :param function_name: str. 호출하기 위한 함수 이름.
    함수 이름은 available_functions 딕셔너리에 있어야 함.

    :param arguments: dict. 호출하는 함수에 전달하는 아규먼트들.

    :return: 호출한 함수의 리턴값.
    만약 함수 이름이 available_functions에 없으면 ValueError를 발생시킴.
    """
    fn = available_functions.get(function_name)
    if fn is None:  # 딕셔너리에서 이름으로 함수를 찾을 수 없을 때
        raise ValueError(f'사용할 수 없는 함수 이름: {function_name}')

    # 찾은 함수를 호출하고, 그 리턴값을 반환.
    return fn(**arguments)  # fn(key1=value1, key2=value2, ...)


# GPT에게 질문을 보낼 때 함께 전송할 도구 목록
tools = [
    {'type': 'web_search'},
    {
        'type': 'function',
        'name': 'get_current_time',
        'description': '해당 timezone의 현재 날짜와 시간을 %Y-%m-%d %H:%M:%S 형식의 문자열로 리턴.',
        'parameters': {
            'type': 'object',
            'properties': {
                'timezone': {
                    'type': 'string',
                    'description': '현재 날짜와 시간을 리턴하기 위한 타임존 명칭. (예) "Asia/Seoul". pytz.all_timezones에서 정의된 문자열을 사용.',
                },
            },
            'required': [ 'timezone' ],
        },
    },
    {
        'type': 'function',
        'name': 'get_yf_info',
        'description': 'ticker 문자열(종목 코드)를 아규먼트로 전달받아서, 그 기업의 정보를 문자열로 리턴.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'Yahoo Finance에서 기업 정보를 반환하기 위해서 필요한 종목 문자열. (예) "AAPL", "MSFT", "005930.KS".'
                },
            },
            'required': [ 'ticker' ],
        },
    },
    {
        'type': 'function',
        'name': 'get_yf_history',
        'description': 'ticker(종목코드) 종목의 특정 기간동안의 주가 변화를 마크다운(markdown) 형식의 문자열로 리턴. 시가, 고가, 저가, 종가, 거래량, 배당금, 주식분할 정보들을 마크다운 형식의 문자열로 리턴.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': '주가를 조회하기 위한 종목 코드. (예) "AAPL", "005930.KS".',
                },
                'period': {
                    'type': 'string',
                    'description': '주가 정보를 조회할 기간. (예) "1d", "5d", "1mo", "1y".',
                },
            },
            'required': [ 'ticker', 'period', ],
        },
    },
    {
        'type': 'function',
        'name': 'get_yf_recommendations',
        'description': 'ticker(종목 코드)에 대한 애널리스트들의 추천 정보(매수, 매도, 유지, ...)를 마크다운 형식의 문자열로 리턴.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': '애널리스트의 추천 정보를 구하기 위한 종목 코드. (예) "AAPL", "005930.KS".',
                },
            },
            'required': [ 'ticker' ],
        },
    },
]


if __name__ == '__main__':
    # print(pytz.all_timezones)

    # print(get_current_time('Asia/Seoul'))
    # print(get_current_time('Europe/London'))

    # print(get_yf_info('AAPL'))  # 애플
    # print(type(get_yf_info('AAPL')))
    # print((get_yf_info('005930.KS')))  # 삼성전자

    # print(get_yf_history(ticker='005930.KS', period='5d'))

    # print(get_yf_recommendations('005930.KS'))

    # # 딕셔너리에서 키(함수 이름)로 값(함수 객체)를 찾음
    # fn = available_functions.get('get_current_time')
    # print(fn)
    # # 함수 호출
    # result = fn('Asia/Seoul')
    # print(result)

    result = invoke_function('get_current_time', {'timezone': 'Asia/Seoul'})
    print(result)

    result = invoke_function('get_yf_history', {'ticker': 'MSFT', 'period': '5d'})
    print(result)
