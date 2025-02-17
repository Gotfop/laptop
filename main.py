from fastapi import FastAPI, Depends
from shemas import User
from dependencies import get_current_user
from routers.auth import auth_router
from routers.laptop import laptop_router
from routers.notes import note_router
from routers.user import user_router




app = FastAPI()
app.include_router(auth_router)
app.include_router(laptop_router)
app.include_router(note_router)
app.include_router(user_router)


@app.get("/")
def root(user: User = Depends(get_current_user)):
    return {"message": user}





