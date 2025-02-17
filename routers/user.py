from fastapi import APIRouter, Depends
from dependencies import get_admin, get_current_user
from servise import UserServise
from shemas import RoleTypeEnum, User

user_router = APIRouter(prefix='/user', tags=['user'])

@user_router.get('/')
def get_all(user: User = Depends(get_current_user)):
    return UserServise.get_all()

@user_router.get('/{nickname}')
def get_by_nickname(nickname: str,user: User = Depends(get_current_user)):
    return UserServise.get_by_nickname(nickname)

@user_router.delete('/{id}')
def delete_user(id: int,admin : User = Depends(get_admin)):
    return UserServise.delete_user(id)

@user_router.put('/{id}')
def update_role(id: int,role: RoleTypeEnum,admin : User = Depends(get_admin)):
    return UserServise.update_user_role(id,role)