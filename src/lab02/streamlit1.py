import streamlit as st


def main():
    st.title("Hello Streamlit-er 👋")
    st.markdown(
        """ 
        *:rainbow[안녕하세요... 저는 오쌤입니다!]*
        
        This is a playground for you to try Streamlit and have fun. 
    
        **There's :rainbow[so much] you can build!**
    
        We prepared a few examples for you to get started. Just 
        click on the buttons above and discover what you can do 
        with Streamlit. 
        """
    )

    if st.button("풍선 날려주세요!"):
        st.balloons()


if __name__ == '__main__':
    main()
