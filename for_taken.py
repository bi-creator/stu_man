from datetime import datetime, timedelta
from jose import JWTError, jwt
import sschemas as ss

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEYF = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f"

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token:str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        stu_id: str = payload.get("sub")
        if stu_id is None:
            raise credentials_exception
        token_data = ss.TokenDatas(stu_id=stu_id)
    except JWTError:
        raise credentials_exception



def create_access_tokenF(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEYF, algorithm=ALGORITHM)
    return encoded_jwt


def verify_tokenF(token:str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEYF, algorithms=[ALGORITHM])
        fac_id: str = payload.get("sub")
        if fac_id is None:
            raise credentials_exception
        token_data = ss.TokenDataf(fac_id=fac_id)
    except JWTError:
        raise credentials_exception
