import fastapi as api
import for_taken as ft
from fastapi.security import OAuth2PasswordBearer

oauth2_schemeF = OAuth2PasswordBearer(tokenUrl="Authorization faculty")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="Authorization student")


def get_current_user(token: str = api.Depends(oauth2_scheme)):
    credentials_exception = api.HTTPException(
        status_code=api.status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return ft.verify_token(token, credentials_exception)


def get_current_userF(token: str = api.Depends(oauth2_schemeF)):
    credentials_exception = api.HTTPException(
        status_code=api.status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return ft.verify_tokenF(token, credentials_exception)