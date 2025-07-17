from fastapi import APIRouter

auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.get('/')
async def authenticator():
    return {'mensagem': 'voce acessou a rota athenticator', 'authenticated': False}