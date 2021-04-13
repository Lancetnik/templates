from typing import Optional
from datetime import datetime, timedelta

from passlib.context import CryptContext
from jose import jwt

from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator

from pydantic import BaseModel


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Token(BaseModel):
    access_token: str
    token_type: str

class UserInput(BaseModel):
    username: str
    password: str

class UserModel(Model):
    username = fields.CharField(max_length=30)
    hashed_password = fields.TextField()

    class PydanticMeta:
        exclude = ["id"]

class TokenModel(Model):
    access_token = fields.TextField(pk=True, max_length=30)
    user = fields.ForeignKeyField('models.UserModel', related_name='user', unique=True)

UserData = pydantic_model_creator(UserModel)


def verify_password(plain_password: str, hashed_password: str) -> str:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def authenticate_user(username: str, password: str):
    user_model = await UserModel.get_or_none(username=username)
    if not user_model:
        return False

    user = await UserData.from_tortoise_orm(user_model)
    if not verify_password(password, user.hashed_password):
        return False

    return user_model



# views
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/logout/")
# token: str = Depends(oauth2_scheme) - check Authentication header
async def logout(token: str = Depends(oauth2_scheme)):
    token = await TokenModel.get(pk=token)
    await token.delete()
    return {'message': 'successful delete'}

@app.post('/sign-up/', response_model=UserData)
async def sign_up(user: UserInput):
    hashed_password = get_password_hash(user.password)
    u = await UserModel.create(username=user.username, hashed_password=hashed_password)
    return u

@app.post("/token/", response_model=Token)
async def login_for_access_token(user: UserInput):
    user_model = await authenticate_user(username=user.username, password=user.password)
    if not user_model:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = await UserData.from_tortoise_orm(user_model)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    await TokenModel.create(user=user_model, access_token=access_token)
    return {"access_token": access_token, "token_type": "bearer"}