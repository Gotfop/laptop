import passlib
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone
from config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_accsess_token(data: dict) -> str:
  to_encode = data.copy()
  expire = datetime.now(timezone.utc) + timedelta(minutes=30)
  to_encode.update({'exp': expire})
  encode_jwt = jwt.encode(
      to_encode, settings.SECRET_KEY, settings.ALGORITHM
  )
  return encode_jwt