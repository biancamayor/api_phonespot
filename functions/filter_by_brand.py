from fastapi import HTTPException, APIRouter
from json_helpers.json_functions import get_connection

router = APIRouter()

@router.get("/filter_by_brand", description='Realiza busca no banco de dados com base em uma marca específica.')
def filter_by_brand(keyword):
    connection = get_connection()

    cursor = connection.cursor()

    query = """select * 
            from comparativo  
            where lower("m_marca") like %s  
            or lower("a_marca") like %s 
            """
    
    keyword = f"%{keyword.lower()}%"

    try:
        cursor.execute(query, (keyword, keyword))

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
    
