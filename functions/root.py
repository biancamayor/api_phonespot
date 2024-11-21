from fastapi import Body, HTTPException, APIRouter

router = APIRouter()

@router.get('/')
def root():
     return {"message": "Olá! Seja bem-vindo. Para acessar a documentação da API, acrescente um '/docs' à URL."}