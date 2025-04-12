from fastapi import APIRouter, HTTPException, Response, status

from servise import FilialsServise, LaptopServise
from shemas import Filial

filial_router = APIRouter(prefix='/filials',tags=['filials'])


@filial_router.get('/')
def get_all():                                                                 #user: User = Depends(get_current_user)
    return FilialsServise.get_all()

@filial_router.post('/')
def add_filial(filial :Filial): 
    id = FilialsServise.add_filial(filial)
    return {"message": id}

@filial_router.delete('/{id}')
def delete_filial(id: int):
    laptops = LaptopServise.get_all()
    for laptop in laptops:
        if laptop.filial_id == id:
            return {"message": 'filial is not empty'}
    return FilialsServise.delete_filial(id)

