from fastapi import HTTPException, APIRouter
from json_helpers.json_functions import get_connection
import pandas as pd

router = APIRouter()

@router.get('/get_available_brands', description='Retorna uma lista com todas as marcas de celulares cadastrados no banco de dados.')
def get_brands():

    try:
            connection = get_connection()

            cursor = connection.cursor()
            query = """
                    SELECT DISTINCT m_marca AS marca, 'Mercado Livre' AS origem
                    FROM comparativo
                    WHERE m_marca IS NOT NULL

                    UNION ALL

                    SELECT DISTINCT a_marca AS marca, 'Americanas' AS origem
                    FROM comparativo
                    WHERE a_marca IS NOT NULL
                    
                    """
            
            cursor.execute(query)

            if cursor.description != None:
                results = cursor.fetchall()
                
                data = {}
                americanas=[]
                mercado_livre = []
    
                for row in results:
                    if row[1] == "Americanas":
                        americanas.append(row[0])
                    elif row[1] == "Mercado Livre":
                         mercado_livre.append(row[0])

                data["Americanas"] = americanas
                data["Mercado Livre"] = mercado_livre

                return data
            
            else:
                return None
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao executar a consulta ao banco de dados: {e}")
    
    finally:
        cursor.close()
        connection.close()