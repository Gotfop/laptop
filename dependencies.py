from fastapi import HTTPException, Request, status, Depends
from config import settings
from jose import JWTError, jwt
from servise import UserServise
from datetime import datetime, timezone
from shemas import User



def get_token(request: Request):
  token = request.cookies.get('laptop_access_token')
  if not token:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token not found')
  return token

def get_current_user(token: str = Depends(get_token)):
  try:
    payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
  except JWTError as e:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')

  expire: str = payload.get('exp')
  if (not expire) or datetime.now(timezone.utc) > datetime.fromtimestamp(int(expire), tz=timezone.utc):
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token expired')

  user_login: str = payload['sub']
  if not user_login:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token does not contain user info')

  user = UserServise.get_by_nickname(user_login)
  if not user:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')
  return user

def get_admin(user : User = Depends(get_current_user)):
  if user.role != 'admin':
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You don\'t have permission to access')
  return user


def get_sysadmin(user : User = Depends(get_current_user)):
  if user.role != 'sysadmin':
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You don\'t have permission to access')
  return user
