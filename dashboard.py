import streamlit as st
import requests
from datetime import datetime
import pandas as pd


def dashboard():


    with open("dashboard.css") as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)



    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Solicitações", "Clientes", "Licenças Activas","Licenças Expiradas","Alertas","Feedback"])



    with tab1:
        st.image("candgest.png", width=200)
        st.header("Solicitações")
        

        try:

            requisicao=requests.get("https://candgestlicense-default-rtdb.firebaseio.com/Licensa/.json")
            print(requisicao)
            dados=requisicao.json()
            print(dados)
            if dados==None:
                st.warning('Sem Solicitações de Licença de momento')
            else:
                n=0
                for dicionario in dados:
                    requisicao=requests.get(f"https://candgestlicense-default-rtdb.firebaseio.com/Licensa/{dicionario}/.json")
                    print(requisicao)
                    dados=requisicao.json()
                    dicionario=[dados]
                    for item in dicionario:
                        with st.expander(item['cliente']):
                            st.write('NIF: '+item['Nif'])
                            st.write("LICENÇA: ",item['licensa'])
                            st.write("CÓDIGO: ",item['license_key'])
                button=st.button(label="Limpar",type='primary')
                if button:
                    requisicao=requests.delete("https://candgestlicense-default-rtdb.firebaseio.com/Licensa/.json")
                    st.success('Os Dados foram limpos')
                    st.rerun()

        except:
            st.error("Sem Conexão a Internet")

    with tab2:
        st.image("candgest.png", width=200)
        st.header("Clientes")
        try:
            requisicao=requests.get("https://candgestlicense-default-rtdb.firebaseio.com/Ativo/.json")
            print(requisicao)
            dados=requisicao.json()
            print(dados)
            data_atual = datetime.now().date()
            if dados==None:
                st.warning('O CandGest Mobile não Possui nenhum cliente')
            else:
                n=0
                lista = []
                for dicionario in dados:
                    requisicao=requests.get(f"https://candgestlicense-default-rtdb.firebaseio.com/Ativo/{dicionario}/.json")
                    print(requisicao)
                    dados=requisicao.json()
                    dicionario=[dados]
                    for item in dicionario:
                        lista.append(item)
                df = pd.DataFrame(lista)
                print("Este é o dicionário",dicionario)
                st.write('Vê a Lista de Clientes que usam o CandGest Mobile')
                st.table(df)

        except :
            st.error("Sem Conexão a Internet")


    with tab3:
        st.image("candgest.png", width=200)
        st.header("Licenças Activas")
        try:
            requisicao=requests.get("https://candgestlicense-default-rtdb.firebaseio.com/Ativo/.json")
            print(requisicao)
            dados=requisicao.json()
            print(dados)
            data_atual = datetime.now().date()
            if dados==None:
                st.warning('De momento não há nenhuma Solicitação de Licença')
            else:
                n=0
                for dicionario in dados:
                    requisicao=requests.get(f"https://candgestlicense-default-rtdb.firebaseio.com/Ativo/{dicionario}/.json")
                    print(requisicao)
                    dados=requisicao.json()
                    dicionario=[dados]
                    for item in dicionario:
                        data = datetime.strptime(item['Data_Final'], '%Y-%m-%d').date()
                        if data >= data_atual:
                            with st.expander(item['cliente']):
                                st.write("LICENÇA: ",item['licensa'])
                                st.write("DATA INICIO: ",item['Data_Inicial'])
                                st.write('DATA FINAL: ',item['Data_Final'])

        except:
            st.error("Sem Conexão a Internet")

    with tab4:
        st.image("candgest.png", width=200)
        st.header("Licenças Expiradas")

        try:
            requisicao=requests.get("https://candgestlicense-default-rtdb.firebaseio.com/Ativo/.json")
            print(requisicao)
            dados=requisicao.json()
            print(dados)
            data_atual = datetime.now().date()
            if dados==None:
                st.warning('De momento não há nenhuma Solicitação de Licença')
            else:
                n=0
                for dicionario in dados:
                    requisicao=requests.get(f"https://candgestlicense-default-rtdb.firebaseio.com/Ativo/{dicionario}/.json")
                    print(requisicao)
                    dados=requisicao.json()
                    dicionario=[dados]
                    for item in dicionario:
                        data = datetime.strptime(item['Data_Final'], '%Y-%m-%d').date()
                        if data < data_atual:
                            with st.expander(item['cliente']):
                                st.write("LICENÇA: ",item['licensa'])
                                st.write("DATA INICIO: ",item['Data_Inicial'])
                                st.write('DATA FINAL: ',item['Data_Final'])

        except:
            st.error("Sem Conexão a Internet")

    with tab5:
        st.image("candgest.png", width=200)
        st.header("Alertas")

        try:
            requisicao=requests.get("https://candgestlicense-default-rtdb.firebaseio.com/Ativo/.json")
            print(requisicao)
            dados=requisicao.json()
            print(dados)
            data_atual = datetime.now().date()
            if dados==None:
                st.warning('Sem Nenhum Alerta Por enquanto')
            else:
                n=0
                for dicionario in dados:
                    requisicao=requests.get(f"https://candgestlicense-default-rtdb.firebaseio.com/Ativo/{dicionario}/.json")
                    print(requisicao)
                    dados=requisicao.json()
                    dicionario=[dados]
                    for item in dicionario:
                        data = datetime.strptime(item['Data_Final'], '%Y-%m-%d').date()
                        diferenca_dias = abs((data - data_atual).days)
                        if 0 < diferenca_dias < 5:
                            with st.expander(item['cliente']):
                                st.write("LICENÇA: ",item['licensa'])
                                st.write("DATA INICIO: ",item['Data_Inicial'])
                                st.write('DATA FINAL: ',item['Data_Final'])
                                st.warning(f"Dias Restantes: {diferenca_dias}")

        except:
            st.error("Sem Conexão a Internet")

    with tab6:
        st.image("candgest.png", width=200)
        st.header("FeedbacK")    
        try:
            requisicao=requests.get("https://candgestlicense-default-rtdb.firebaseio.com/Feedback.json")
            print(requisicao)
            dados=requisicao.json()
            print(dados)
            data_atual = datetime.now().date()
            if dados==None:
                st.warning('Sem nenhum Feedback')
            else:
                n=0
                for dicionario in dados:
                    requisicao=requests.get(f"https://candgestlicense-default-rtdb.firebaseio.com/Feedback/{dicionario}/.json")
                    print(requisicao)
                    dados=requisicao.json()
                    dicionario=[dados]
                    for item in dicionario:
                        with st.container():
                            st.write(item['Empresa'])
                            st.write("Email: ",item['E-mail'])
                            st.write("Sugestão: ",item['Sugestão'])
                            st.divider()
                button1=st.button("Limpar",type="primary")
                if button1:
                    requisicao=requests.delete("https://candgestlicense-default-rtdb.firebaseio.com/Feedback/.json")
                    st.success('Os Dados foram limpos')
                    st.rerun()                    
        except :
            st.error("Sem Conexão a Internet")


