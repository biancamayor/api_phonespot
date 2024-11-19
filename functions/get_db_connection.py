import json
import os
import sys
import logging 
import uuid
import psycopg2
from fastapi import Body, HTTPException, APIRouter
from pydantic import BaseModel
from json_helpers.json_functions import add_connection_on_json_file
from dotenv import load_dotenv


router = APIRouter()

class Credentials(BaseModel):
    host: str
    database: str
    user: str
    password: str


@router.post('/get_db_connection', description='Estabelece uma conexão com o banco de dados.')
def get_db_connection(credentials: Credentials = Body(...)):
    try:
        logging.info("Recebendo credenciais: %s", credentials)
        connection_ = psycopg2.connect(
            host=credentials.host,
            database=credentials.database,
            user=credentials.user,
            password=credentials.password
        )
    
        load_dotenv()

        connection_token = str(uuid.uuid4())  

        add_connection_on_json_file(file_path = os.getenv('CONNECTIONS_PATH'), 
                                    connection_token=connection_token, 
                                    credentials=credentials)

        return {"status": "success", "message": "Conexão estabelecida com sucesso.",  "connection_token": connection_token}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao conectar ao banco de dados: {e}")



