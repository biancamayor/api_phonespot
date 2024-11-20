import streamlit as st
import requests
import pandas as pd


def get_all_results():
    API_URL = "http://localhost:8000/read_db_data"
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        return response.json()  
    else:
        st.error(f"Erro ao buscar os dados: {response.status_code}")
        return []
    


def get_ordered_by_price_results(asc:bool, americanas:bool):
    API_URL = f"http://127.0.0.1:8000/order_data_by_price?asc={asc}&americanas={americanas}"
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        return response.json()  
    else:
        st.error(f"Erro ao buscar os dados: {response.status_code}")
        return []
    


def get_filtered_by_price_results(min_value, max_value):
    API_URL = f"http://127.0.0.1:8000/filter_data_by_price?min_value={min_value}&max_value={max_value}"

    response = requests.get(API_URL)
    
    if response.status_code == 200:
        return response.json()  
    else:
        st.error(f"Erro ao buscar os dados: {response.status_code}")
        return []


def format_response(site, row):
    if site == 'Americanas':
        format = st.markdown(f"""
                    <div style="border: 4px solid #6A8595; border-radius: 10px; padding: 15px; margin-bottom: 10px; background-color: #1C282E; height: 400px; color: #FFFFFF; display: flex; flex-direction: column;">
                        <p><strong>ID:</strong> {row['Id']}</p>
                        <p><strong>Modelo:</strong> {row['Americanas']['Nome']}</p>
                        <p><strong>Marca:</strong> {row['Americanas']['Marca']}</p>
                        <p><strong>Preço:</strong> {row['Americanas']['Valor']}</p>
                        <p><strong>Código Anatel:</strong> {row['Americanas']['Código']}</p>
                        <br>
                        <div style="display: flex; justify-content: flex-end; align-items: flex-end; margin-top: auto;">
                            <a href={row['Americanas']['Link']} target="_blank">
                            <button style="background-color: #273F4B; color: white; border: none; border-radius: 5px; padding: 5px; cursor: pointer; margin-top: auto">
                                Visitar o produto
                            </button>
                            </a>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
        
    elif site == 'Mercado Livre':
        format = st.markdown(f"""
                <div style="border: 4px solid #6A8595; border-radius: 10px; padding: 15px; margin-bottom: 10px; background-color: #1C282E; height: 400px; color: #FFFFFF; display: flex; flex-direction: column;">
                    <p><strong>ID:</strong> {row['Id']}</p>
                    <p><strong>Modelo:</strong> {row['Mercado Livre']['Nome']}</p>
                    <p><strong>Marca:</strong> {row['Mercado Livre']['Marca']}</p>
                    <p><strong>Preço:</strong> {row['Mercado Livre']['Valor']}</p>
                    <p><strong>Código Anatel:</strong> {row['Mercado Livre']['Código']}</p>
                    <br>
                    <div style="display: flex; justify-content: flex-end; align-items: flex-end; margin-top: auto;">
                        <a href={row['Mercado Livre']['Link']} target="_blank">
                        <button style="background-color: #273F4B; color: white; border: none; border-radius: 5px; padding: 5px; cursor: pointer; margin-top: auto">
                            Visitar o produto
                        </button>
                        </a>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    return format


def get_available_brands():
    API_URL = f"http://127.0.0.1:8000/get_available_brands"
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        return response.json()  
    else:
        st.error(f"Erro ao buscar os dados: {response.status_code}")
        return []


def get_filtered_by_brand_results(brand):
    API_URL = f"http://127.0.0.1:8000/filter_by_brand?keyword={brand}"
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        return response.json()  
    else:
        st.error(f"Erro ao buscar os dados: {response.status_code}")
        return []
    
    

def get_filtered_by_keyword_results(keyword):
    API_URL = f" http://127.0.0.1:8000/filter_by_keyword?keyword={keyword}"
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        return response.json()  
    else:
        st.error(f"Erro ao buscar os dados: {response.status_code}")
        return []
   