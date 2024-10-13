import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '')))
from functions.read_database_data import read_db_data
from json_helpers.json_functions import get_connection
from fastapi import HTTPException, APIRouter


router = APIRouter()

@router.get('/order_data_by_price', description="""Retorna os dados dos celulares filtrados 
em ordem crescente / decrescente de preço. A coluna usada como filtro para preço pode ser do
Mercado Livre ou da Americanas. Por padrão, a coluna de preço da Americanas será utilizada,
mas isso pode ser alterado mudando o parâmetro 'americanas' de 'True' para 'False'. 
Além disso, para exibir os valores em ordem descrescente de preço, visto que, por padrão, 
os resultados são exibidos em ordem crescente, basta modificar o valor do parâmetro 'asc' 
de 'True' para 'False' e os resultados virão em ordem decrescente de preço.""")
def order_by_price(asc:bool=True, americanas:bool=True):

    column = 'a_valor' if americanas == True else 'm_valor'

    query = ''

    if asc == True:
        query = f""" SELECT * 
                    FROM COMPARATIVO 
                    ORDER BY CAST(REPLACE(CAST({column} AS TEXT), 'R$', '') AS FLOAT) ASC;     
                """
        
    elif asc == False:
        query = f""" SELECT * 
                    FROM COMPARATIVO 
                    ORDER BY CAST(REPLACE(CAST({column} AS TEXT), 'R$', '') AS FLOAT) desc;     
                """

    try:
        connection = get_connection()

        cursor = connection.cursor()

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
                                            'Americanas': {'Valor': f'R$ {row[5]}',
                                                        'Código': row[6],
                                                        'Nome': row[7],
                                                        'Marca': row[8],
                                                        'Link': row[10]}})
            return data

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao executar a consulta ao banco de dados: {e}")
    
    finally:
        cursor.close()
        connection.close()






