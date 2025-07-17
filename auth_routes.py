from fastapi import APIRouter
from models import User, db
from sqlalchemy.orm import sessionmaker

auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.get('/')
async def home():
    return {'mensagem': 'voce acessou a rota athenticator', 'authenticated': False}

@auth_router.post('/creat_user')
async def creat_user(name: str, email: str, password:str):
    Session = sessionmaker(bind=db)
    session = Session()
    user = session.query(User).filter(User.email==email).first()
    if user:
        return {'mensagem': 'ja existe um usuario com esse email'}    
    else:
        new_user = User(name, email, password)
        session.add(new_user)
        session.commit()
        return {'mensagem': 'usuario cadastrado com sucesso'}