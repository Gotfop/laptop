from fastapi import APIRouter, Depends
from dependencies import get_current_user, get_sysadmin
from servise import LaptopServise
from shemas import Laptop, User

laptop_router = APIRouter(prefix='/laptop',tags=['laptop'])

@laptop_router.get('/')
def get_all():                                                                 #user: User = Depends(get_current_user)
    return LaptopServise.get_all()  


@laptop_router.post('/')
def add_laptop(laptop: Laptop):
    print(laptop)
    id = LaptopServise.add_laptop(laptop)
    return {"message": id}


@laptop_router.put('/{id}')
def update(id, sysadmin : User = Depends(get_sysadmin)):
    lpt = LaptopServise.get_by_id(id)



@laptop_router.get('/{id}')
def get_laptop_id(id,user: User = Depends(get_current_user)):
    return LaptopServise.get_by_id(id)

@laptop_router.get('/mark')
def get_mark():
    return LaptopServise.get_mark()