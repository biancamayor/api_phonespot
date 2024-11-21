import os
import sys
from fastapi import Body, HTTPException, APIRouter
from functions.read_database_data import read_db_data
import logging

router = APIRouter()

@router.get('/filter_data_by_price', description='''Retorna apenas celulares que possuem valores no intervalo 
de "min_value" (valor minimo) e "max_value" (valor máximo).''')

def filter_data_by_price(min_value:float, max_value:float):

    def clean_price(price:str):
        price_ = price.replace('R$', '').replace(',','.').strip()       
        return float(price_)
    
    try:
        results = read_db_data()

       
        filtered_results = []

        for row in results:
            mercado_livre_price = clean_price(row['Mercado Livre']['Valor'])
            americanas_price = clean_price(row['Americanas']['Valor'])

            logging.warning(f"Valores Mercado Livre: {mercado_livre_price}, Americanas: {americanas_price}")  

            if (min_value <= mercado_livre_price <= max_value) and (min_value <= americanas_price <= max_value):
                filtered_results.append(row)

        logging.warning("Resultados filtrados:", filtered_results)  


        return filtered_results
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao filtrar dados: {e}")
        

