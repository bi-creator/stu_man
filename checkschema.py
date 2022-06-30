import pydantic as pyd

from typing import List

class newstudent(pyd.BaseModel):
    first_name:str
    middle_name:str
    last_name:str
    id:str
    number:str
    mail: str
    pas: str
    # coursename:str
    # semister_num:int
    # bran_name:str
    # attandance:int

class sturesponce(pyd.BaseModel):

    first_name:str
    middle_name:str
    last_name:str
    stu_id:str
    phone_num:str
    email: str
    #pas: str
    # coursename:str
    # semister_num:int
    # bran_name:str
    # attandance:int
    class Config:
        orm_mode=True