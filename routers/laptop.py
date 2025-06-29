from fastapi import APIRouter, Depends, status
from dependencies import get_current_user, get_sysadmin
from servise import LaptopServise
from shemas import Laptop, User, Mark

laptop_router = APIRouter(prefix='/laptop',tags=['laptop'])

@laptop_router.get('/')
def get_all():                                                                 #user: User = Depends(get_current_user)
    return LaptopServise.get_all()  


@laptop_router.post('/')
def add_laptop(laptop: Laptop):
    print(laptop)   
    id = LaptopServise.add_laptop(laptop)
    return {"message": id}

@laptop_router.get('/mark')
def get_mark():
    a = LaptopServise.get_mark()
    print(a)
    return a

@laptop_router.post('/mark')
def add_mark(mark: Mark):
    id = LaptopServise.add_mark(mark)
    return {"message": id}
    

@laptop_router.put('/{id: int}')
def update(id, sysadmin: User = Depends(get_sysadmin)):
    lpt = LaptopServise.get_by_id(id)

@laptop_router.delete('/{id: int}', status_code=status.HTTP_204_NO_CONTENT)

def delete_laptop(id):                                     # ,user: User = Depends(get_current_user)
    return LaptopServise.delete_laptop(id)


@laptop_router.get('/{id: int}')
def get_laptop_id(id):                                     # ,user: User = Depends(get_current_user)
    return LaptopServise.get_by_id(id)
