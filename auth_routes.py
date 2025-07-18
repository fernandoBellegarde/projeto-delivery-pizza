from fastapi import APIRouter, Depends
from models import User
from dependecies import catch_session

auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.get('/')
async def home():
    return {'mensagem': 'voce acessou a rota athenticator', 'authenticated': False}

@auth_router.post('/creat_user')
async def creat_user(name: str, email: str, password:str, session = Depends(catch_session)):
    user = session.query(User).filter(User.email==email).first()
    if user:
        return {'mensagem': 'ja existe um usuario com esse email'}    
    else:
        new_user = User(name, email, password)
        session.add(new_user)
        session.commit()
        return {'mensagem': 'usuario cadastrado com sucesso'}