import streamlit as st
import requests
import pandas as pd
from request_functions import *



def initial_page():
    st.title('PhoneSpot')
    st.write("")
    st.write("")
    st.write("")

    with st.container():
        col1, col2 = st.columns([5, 6.3], gap="large") 

        with col1:
            st.image("streamlit\logo.jpg", use_column_width=True)

        with col2:
            st.markdown(
            "<h2><b>Bem vindo ao PhoneSpot!</b></h2>"
            "<p style='font-size:20px;'>Aqui você poderá buscar a melhor oferta para o celular dos seus sonhos!</p>",
            unsafe_allow_html=True
            )

            st.write("")
            st.write("")
            if st.button("ﾠﾠﾠﾠﾠﾠﾠIniciar buscasﾠﾠﾠﾠﾠﾠﾠ"):
                st.session_state.page = 'second_page'
            




def standard_page():
    with st.spinner('Carregando dados dos celulares disponíveis...'):
        results = get_all_results()

    if results:
        df = pd.DataFrame(results)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Americanas")
            for index, row in df.iterrows():
                format_response(site='Americanas', row=row)
        with col2:
            st.subheader("Mercado Livre")
            for index, row in df.iterrows():
                format_response(site='Mercado Livre', row=row)




def filter_by_price():
    preco_minimo, preco_maximo = st.slider(
    "Selecione o intervalo de preço",
    0, 10000, (500, 2000) )

    if st.button('Buscar'):
        with st.spinner('Buscando celulares para o intervalo fornecido...'):
            results = get_filtered_by_price_results(min_value=preco_minimo, max_value=preco_maximo)

        if results:
            df = pd.DataFrame(results)

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Americanas")
                for index, row in df.iterrows():
                    format_response(site='Americanas', row=row)
            with col2:
                st.subheader("Mercado Livre")
                for index, row in df.iterrows():
                    format_response(site='Mercado Livre', row=row)
        else:
            st.write("Sem resultados para o intervalo selecionado.")




def ordered_by_price_page():

    s_opcoes = ['Americanas', 'Mercado Livre']
    site = st.selectbox("Ordenar preços para", s_opcoes)

    o_opcoes = ['Ascendente', 'Decrescente']
    ordem = st.selectbox("Escolha a ordem", o_opcoes)

    s_value = True if site == 'Americanas' else False
    o_value = True if ordem == 'Ascendente' else False

    if st.button('Buscar'):
        with st.spinner('Ordenando celulares...'):
            results = get_ordered_by_price_results(asc=o_value, americanas=s_value)

        df = pd.DataFrame(results)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Americanas")
            for index, row in df.iterrows():
                format_response(site='Americanas', row=row)


        with col2:
            st.subheader("Mercado Livre")
            for index, row in df.iterrows():
                format_response(site='Mercado Livre', row=row)




def available_brands_page():
    with st.spinner('Buscando marcas disponíveis...'):
        results = get_available_brands()
    americanas = results['Americanas']
    mercado_livre = results['Mercado Livre']


    am_text = ""
    for item in americanas:
        if item != 'NaN':
            am_text += item + ', ' 
    
    ml_text = ""
    for item in mercado_livre:
        if item != 'NaN':
            ml_text += item + ', ' 
           
    st.write("")
    st.write("")
    st.text(f'Marcas disponíveis para a Americanas: \n \n {am_text}')
    st.write("")
    st.write("")
    st.text(f"Marcas disponíveis para o Mercado Livre: \n \n {ml_text}")

    


def filter_by_brand_page():

    with st.spinner('Buscando marcas disponíveis...'):
        brands = get_available_brands()

    americanas = brands['Americanas']
    mercado_livre = brands['Mercado Livre']

    _brands_options = list(set(americanas) | set(mercado_livre))

    brands_options = [x for x in _brands_options if x != 'NaN']

    selected_option = st.selectbox('Escolha uma marca:', brands_options)

    if st.button('Buscar'):
        with st.spinner('Buscando celulares para a marca selecionada...'):
            results = get_filtered_by_brand_results(brand=selected_option)

        df = pd.DataFrame(results)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Americanas")
            for index, row in df.iterrows():
                format_response(site='Americanas', row=row)


        with col2:
            st.subheader("Mercado Livre")
            for index, row in df.iterrows():
                format_response(site='Mercado Livre', row=row)
    



def filter_by_keyword_page():

    keyword = st.text_input('Digite uma palavra para buscar:')

    if st.button('Buscar'):
        with st.spinner('Buscando correspondências para a palavra digitada...'):
            results = get_filtered_by_keyword_results(keyword=keyword)

        if results != None and results != []:
            df = pd.DataFrame(results)

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Americanas")
                for index, row in df.iterrows():
                    format_response(site='Americanas', row=row)


            with col2:
                st.subheader("Mercado Livre")
                for index, row in df.iterrows():
                    format_response(site='Mercado Livre', row=row)
        
        else:
            st.write("Sem correspondências para a palavra digitada!")



