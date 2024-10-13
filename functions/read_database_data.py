from fastapi import Body, HTTPException, APIRouter
from json_helpers.json_functions import get_connection
from dotenv import load_dotenv
import os
import psycopg2

router = APIRouter()

@router.get('/read_db_data', description="""Retorna as informações de todos celulares disponíveis no banco de dados. 
É necessário iniciar a conexão com o banco de dados, executando o endpoint 'get_db_connection'.""")
def read_db_data():

    try:
        connection = get_connection()

        cursor = connection.cursor()
        query = """SELECT * FROM comparativo"""
        
        cursor.execute(query)

        if cursor.description != None:
            results = cursor.fetchall()
            data = []
            for row in results:
                data.append({'Id': row[0], 'Mercado Livre': {'Código': row[1],
                                                        'Nome': row[2],
                                                        'Marca': row[3],
                                                        'Valor': f'R$ {row[4]}',
                                                        'Link': row[9]},
                                        'Americanas': {'Código': row[6],
                                                    'Nome': row[7],
                                                    'Marca': row[8],
                                                    'Valor': f'R$ {row[5]}',
                                                    'Link': row[10]}})
            return data
       
        else:
            return None
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao executar a consulta ao banco de dados: {e}")
    
    finally:
        cursor.close()
        connection.close()