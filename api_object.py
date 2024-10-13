from functions.get_db_connection import router as get_db_connection
from functions.read_database_data import router as read_data_router
from functions.filter_data_by_price import router as filter_data_by_price
from functions.order_data_by_price import router as order_data_by_price
from functions.get_available_brands import router as get_available_brands
from functions.filter_by_keyword import router as filter_by_keyword
from functions.filter_by_brand import router as filter_by_brand
from fastapi import FastAPI


#TODO: Get connection sempre necessario antes de qualquer endpoint?

#TODO: Inserir autenticação PARA QUEM PODE USAR A API (CONFIG CORES) E O BANCO


api = FastAPI()

api.include_router(get_db_connection)
api.include_router(read_data_router)
api.include_router(filter_data_by_price)
api.include_router(order_data_by_price)
api.include_router(get_available_brands)
api.include_router(filter_by_keyword)
api.include_router(filter_by_brand)