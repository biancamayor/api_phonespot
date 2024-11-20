import os
import hmac
import hashlib
from dotenv import load_dotenv
from fastapi import Request, HTTPException

load_dotenv()

async def is_ip_allowed(request: Request, call_next): 
    def generate_signature(ip:str):
        """
        Gera uma assinatura HMAC para o IP usando a SECRET_KEY.
        """
        SECRET_KEY = os.getenv("SECRET_KEY")
        return hmac.new(SECRET_KEY.encode(), ip.encode(), hashlib.sha256).hexdigest()

    allowed_ip = os.getenv("allowed_ip")

    client_ip = request.client.host   
    client_signature = generate_signature(client_ip)
    expected_signature = generate_signature(allowed_ip)

    if not hmac.compare_digest(client_signature, expected_signature):
        raise HTTPException(status_code=403, detail="Acesso negado: IP não autorizado")
    
    if client_ip != allowed_ip:
        raise HTTPException(status_code=403, detail="Acesso negado: IP não autorizado")
    
    response = await call_next(request)
    return response
