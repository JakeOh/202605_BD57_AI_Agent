import streamlit as st
import pandas as pd
import numpy as np

st.write("Streamlit supports a wide range of data visualizations, including [Plotly, Altair, and Bokeh charts](https://docs.streamlit.io/develop/api-reference/charts). 📊 And with over 20 input widgets, you can easily make your data interactive!")

# 문자열 3개를 저장하고 있는 list
all_users = ["Alice", "Bob", "Charly"]

# container 객체 생성
with st.container(border=True):
    # 컨테이너에 포함시킬 UI 요소들들 생성
    # 다중선택 입력창
    users = st.multiselect("Users", all_users, default=all_users)
    # 토글 버튼
    rolling_average = st.toggle("Rolling average")

np.random.seed(42)

# pandas.DataFrame 생성(20개 행, 다중선택 입력창에서 선택된 아이템 개수만큼 컬럼 생성)
data = pd.DataFrame(np.random.randn(20, len(users)), columns=users)
if rolling_average:  # 토글 버튼이 on 상태일 때(켜져 있을 때)
    data = data.rolling(7).mean().dropna()

# 2개의 탭을 생성
tab1, tab2 = st.tabs(["Chart", "Dataframe"])
# 첫번째 탭에 선그래프를 출력 - plotly를 이용해서 인터랙티브 그래프를 그려줌.
tab1.line_chart(data, height=250)
# 두번째 탭에 데이터프레임을 출력
tab2.dataframe(data, height=250, use_container_width=True)
