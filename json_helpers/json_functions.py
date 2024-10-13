import os
import json
from dotenv import load_dotenv
import psycopg2
from fastapi import HTTPException


def load_json_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                connections = json.load(file)
                return connections
            
            except json.JSONDecodeError:
                return {} 



def get_connection():
    load_dotenv()
    connection = load_json_file(os.getenv('CONNECTIONS_PATH'))

    if connection is None:
        raise HTTPException(status_code=404, detail="Conexão não encontrada.")


    connection_data_list = list(connection.values())
    connection_data = connection_data_list[0]

    try:
        connection = psycopg2.connect(
            host=connection_data['host'],
            database=connection_data['database'],
            user=connection_data['user'],
            password=connection_data['password']
        )
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao acessar conexão do banco de dados: {e}")
    
    return connection



def add_connection_on_json_file(file_path, connection_token, credentials):
    data = {}
    
    with open(file_path, 'w') as file:
        data[connection_token] = {
        "host": credentials.host,
        "database": credentials.database,
        "user": credentials.user,
        "password": credentials.password
    }
        json.dump(data, file, indent=4)

