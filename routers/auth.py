from fastapi import APIRouter, HTTPException, Response, status

from utils import create_accsess_token, get_password_hash, verify_password
from servise import UserServise
from shemas import User, RegUser

auth_router = APIRouter(prefix='/auth',tags=['auth'])

@auth_router.post('/login')
def login_user(response : Response, user : RegUser):
    userBD = UserServise.get_by_nickname(user.nickname)
    if userBD and verify_password(user.password, userBD.password):
        token = create_accsess_token({'sub': user.nickname})
        response.set_cookie('laptop_access_token', token, httponly=True)
        return {'laptop_access_token': token}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        



@auth_router.post('/register')
def create_user(user : RegUser):
    userBD = UserServise.get_by_nickname(user.nickname)
    if userBD:
        return {"message": 'Введите другое'}
    has_pass = get_password_hash(user.password)
     
    UserServise.create_user(nickname= user.nickname ,password = has_pass,role = 'user')
    return{"message": 'Готово'}
