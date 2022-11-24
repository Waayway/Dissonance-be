from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt

from database import crud, schemas
import os, json



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

router = APIRouter()

JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"


async def get_current_user(token: str = Depends(oauth2_scheme)) -> schemas.User:
    try:
        payload = jwt.decode(token,JWT_SECRET,algorithms=[ALGORITHM])
        user = crud.get_user(payload.get("id"))
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not logged in")
    
    return user

@router.get('/users/me', response_model=schemas.User)
async def get_myself(user: str = Depends(get_current_user)):
    return user

@router.post('/login')
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = crud.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    userJSON = json.loads(user.json())

    token = jwt.encode(userJSON, JWT_SECRET)

    return {'access_token': token, 'token-type': 'bearer'}

@router.post('/users', response_model=schemas.User)
async def create_user(user: schemas.UserCreate):
    print(user)
    user_obj = crud.create_user(user)
    return user_obj
