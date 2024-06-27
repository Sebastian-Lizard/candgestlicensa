import streamlit as st
from login import login
from dashboard import dashboard

def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.session_state['logged_in']:
        dashboard()
    else:
        login()

if __name__ == '__main__':
    main()
