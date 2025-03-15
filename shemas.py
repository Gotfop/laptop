from enum import Enum
from pydantic import BaseModel


class RoleTypeEnum(str, Enum):
    user = 'user'
    admin = 'admin'
    sysadmin = 'sysadmin'


class DriveTypeEnum(str, Enum):
    ssd = 'SSD'
    hdd = 'HDD'

class Laptop(BaseModel):
     mark_id : int
     model : str
     CPU : str
     CPU_cores : int
     CPU_frequency : str
     RAM_amount : str
     video_card :str | None
     drive_type : DriveTypeEnum
     drive_amount : int



class Note(BaseModel):
    date : str
    text : str
    user_id : str
    laptop_id : int


class User(BaseModel):
    nickname : str
    password : str
    role : str = 'user'
    isactive : bool = True


class RegUser(BaseModel):
    nickname : str
    password : str

class Filial(BaseModel):
    filial : str
    isactive : bool = True
    