import streamlit as st



def login():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)


    st.header("Login")
    with st.form(key='login'):
        st.image("candgest.png", width=200)
        input_name =st.text_input(label='Usuário')
        input_senha = st.text_input(label='Senha',type='password')
        input_button = st.form_submit_button('Entrar')


    if input_button:
        if input_name=='Candimba Tecnologia' and input_senha=="Norbyana":
            st.success('Login realizado com sucesso!')
            st.session_state['logged_in'] = True
            st.rerun()
            
        else:
            st.error('Usuário ou senha incorretas')
