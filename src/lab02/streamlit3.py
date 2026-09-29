import streamlit as st

def main():
    # 지역 변수 선언
    count = 0

    # streamlit의 session_state 객체:
    # Streamlit App이 동작 중에 계속 유지해야 할 데이터를 저장하기 위한 객체.
    # 파이썬 dict와 비슷하게 key-value 쌍으로 아이템 저장, 사용할 수 있음.
    if 'count' not in st.session_state:
        # count(키)가 session_state에 없으면
        # count(키)에 정수 0(값)을 저장.
        st.session_state.count = 0  # st.session_state['count'] = 0

    # 화면에 버튼을 생성
    if st.button('count 1 증가'):  # 버튼이 클릭됐을 때
        count += 1  # 지역변수 count의 값을 1 증가시킴.
        st.session_state.count += 1  # session_state가 가지고 있는 count 값을 1 증가.

    # 지역 변수 count 값을 출력
    st.write('count =', count)
    # session_state의 count 값을 출력
    st.write('session_state.count =', st.session_state.count)


if __name__ == '__main__':
    main()
