from fastapi import APIRouter, Depends
from dependencies import get_current_user
from servise import NoteServise
from shemas import Note, User

note_router = APIRouter(prefix='/note',tags=['note'])

@note_router.post('/')
def add_note(Note: Note,user: User = Depends(get_current_user)):
    id = NoteServise.add_note(Note)
    return {"message": id}


@note_router.get('/{id}')
def get_note(id,user: User = Depends(get_current_user)):
    return NoteServise.get_by_lpt(id)