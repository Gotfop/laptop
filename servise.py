from database import MarksModel, session
from sqlalchemy import select,insert
from database import LaptopsModel,NotesModel,UserModel
from shemas import Laptop,Note

class LaptopServise:

    @classmethod
    def get_mark(cls):
        with session() as sess:
            query = select(MarksModel)
            return(sess.execute(query).scalars().all())

    @classmethod
    def get_all(cls):
        with session() as sess:
            query = select(LaptopsModel)
            return(sess.execute(query).scalars().all())
        

    @classmethod
    def get_by_id(cls,id):
        with session() as sess:
            query = select(LaptopsModel).filter_by(id = id)
            return(sess.execute(query).scalar_one_or_none())
        
    @classmethod
    def add_laptop(cls,laptop: Laptop):
        lpt_dict = laptop.model_dump()
        laptop_object = LaptopsModel(**lpt_dict)
        with session() as sess:
            sess.add(laptop_object)
            sess.commit()
            return laptop_object.id        
        
class NoteServise:

    @classmethod
    def get_by_lpt(cls,id):
        with session() as sess:
            query = select(NotesModel).filter_by(laptop_id = id)
            return(sess.execute(query).scalars().all())
        
    @classmethod
    def add_note(cls,note: Note):
        note_dict = note.model_dump()
        note_object = NotesModel(**note_dict)
        with session() as sess:
            sess.add(note_object)
            sess.commit()
            return note_object.id
        
class UserServise:
  

    @classmethod
    def create_user(cls, **data):
        with session() as sess:
            query = insert(UserModel).values(**data).returning(UserModel.id)
            sess.execute(query)
            sess.commit()


    @classmethod
    def get_by_nickname(cls,nickname):
        with session() as sess:
            query = select(UserModel).filter_by(nickname = nickname, isactive = True)
            return(sess.execute(query).scalar_one_or_none())
    
    
    @classmethod
    def get_all(cls):
        with session() as sess:
            query = select(UserModel).filter_by(isactive = True)
            return(sess.execute(query).scalars().all())
        

    @classmethod
    def delete_user(cls, id):
        with session() as sess:
            query = select(UserModel).filter_by(id = id)
            user = sess.execute(query).scalar_one_or_none()
            if user:
                user.isactive = False
                sess.add(user)
                sess.commit()   
                return True
            return False
        

    @classmethod
    def update_user_role(cls, id, role):
        with session() as sess:
            query = select(UserModel).filter_by(id = id)
            user = sess.execute(query).scalar_one_or_none()
            if user:
                user.role = role
                sess.add(user)
                sess.commit()
                return True
            return False
