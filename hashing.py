from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify(user_pass,normal_pass):
    return pwd_context.verify(normal_pass,user_pass)