import streamlit as st
from pages_functions import *


st.set_page_config(page_title="PhoneSpot", layout="centered")
st.markdown("""
    <style>
    .stApp {
        background-color: #1C282E;  /* Altere para a cor desejada */
        color: white;  /* Cor do texto */
    }
        div[data-testid="stSelectbox"] > div {
        background-color: #ADD8E6;  
        color: #000000;  
    }

    div[data-testid="stSelectbox"] > div > div > div {
        color: #ffffff;
        background-color: #6A8595; /
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)



def go_to_standard_page():
    st.session_state.page = 'second_page'


def go_to_initial_page():
    st.session_state.page = 'first_page'




if 'page' not in st.session_state:
    st.session_state.page = 'first_page'


if st.session_state.page == 'first_page':
    initial_page()
    
    if st.session_state.page == 'second_page':
        go_to_standard_page()


elif st.session_state.page == 'second_page':
    
    if st.button('Voltar para página inicial') and st.session_state.page == 'second_page':
        go_to_initial_page()

    st.title("PhoneSpot")

    funcao_opcoes = ['Exibição Padrão', 'Ordenar por preço', 'Filtrar valor mínimo e máximo', 'Exibir marcas disponíveis', 'Buscar por marca específica', 'Busca por palavra chave']
    funcao_escolhida = st.selectbox('Escolha uma função para exibir os dados:', funcao_opcoes)
    
    if funcao_escolhida == 'Ordenar por preço':
        ordered_by_price_page()  
    elif funcao_escolhida == 'Filtrar valor mínimo e máximo':
        filter_by_price() 
    elif funcao_escolhida == 'Exibir marcas disponíveis':
        available_brands_page()
    elif funcao_escolhida == 'Buscar por marca específica':
        filter_by_brand_page()
    elif funcao_escolhida == 'Busca por palavra chave':
        filter_by_keyword_page()
    else:
        standard_page()  