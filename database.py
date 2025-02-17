
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///database.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass


class MarksModel(Base):
    __tablename__ = 'mark'
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    mark = Column(String,nullable=False)

class FilialsModel(Base):
    __tablename__ = 'filials'

    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String,nullable=False)
    address = Column(String)

class LaptopsModel(Base):
     __tablename__ = 'laptop'

     id = Column(Integer, autoincrement=True, primary_key=True)
     mark_id = Column(ForeignKey(MarksModel.id, ondelete="CASCADE"))
     model = Column(String,nullable=False)
     CPU = Column(String,nullable=False)
     CPU_cores = Column(Integer,nullable=False)
     CPU_frequency = Column(String,)
     RAM_amount = Column(String,nullable=False)
     video_card = Column(String,nullable=True)
     drive_type = Column(String)
     drive_amount = Column(Integer)
     filial_id = Column(ForeignKey(FilialsModel.id, ondelete="CASCADE"))


class NotesModel(Base):
    __tablename__ = 'note'

    id = Column(Integer, autoincrement=True, primary_key=True)
    date = Column(String)
    text = Column(String)
    user_id = Column(String)
    laptop_id = Column(ForeignKey(LaptopsModel.id, ondelete="CASCADE"))


class UserModel(Base):
    __tablename__ = 'user'
    
    id = Column(Integer,primary_key=True,autoincrement=True)
    nickname = Column(String,nullable=False)
    role = Column(String,nullable=False)
    tg_nickname = Column(String,nullable=True)
    password = Column(String)
    isactive = Column(Boolean, default=True)



Base.metadata.create_all(engine)