import streamlit as st
from home import run_home
from eda import run_eda


def main() :
    
    st.title('미디어 성지순례 포인트 찾기')
    st.sidebar.image('./data/image2.gif')   
    menu = ['Home','어디에 있나요?']
    choice = st.sidebar.selectbox('메뉴', menu)

    
    if choice == menu[0]:
        run_home()
    if choice == menu[1]:
        run_eda()


if __name__ == '__main__':
    main()