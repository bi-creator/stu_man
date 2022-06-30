import pydantic as pyd
from typing import List
import uuid

from uuid import UUID
class newstudent(pyd.BaseModel):
    first_name:str
    middle_name:str
    last_name:str
    id:str
    number:str
    mail: str
    pas: str
    coursename:str
    semister_num:int
    bran_name:str
    attandance:int

    class Config:
        orm_mode = True
class show_student(pyd.BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    stu_id: str
    phone_num: str
    email: str
    course_name: str
    semister_num: int
    branch: str
    attandance: int

    class Config:
        orm_mode=True

class newfaculty(pyd.BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    id:str
    number:str
    mail: str
    pas: str
    teaching_sub:str
    teaching_branch:str


class login(pyd.BaseModel):
    id:str
    pas:str


class new_course_details(pyd.BaseModel):
    course_name: str
    course_id:str



class show_faculty_details(pyd.BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    fac_id: str
    phone_num: str
    email: str
    tec_sub: str
    tec_branch: str

    class Config:
        orm_mode=True




class branch(pyd.BaseModel):
    branch_name:str

class sem_num(pyd.BaseModel):
    sem_num:int

class subjects_info(pyd.BaseModel):
    sub_id:str
    sub_name:str
    faculty_name:str
    course_name:str
    branch_name:str
    sem_num:int

class student_marks(pyd.BaseModel):
    student_id:str
    subject_name:str
    semister_num:int
    subject_marks:int
    sno:int

class fee_details(pyd.BaseModel):
    stu_id:str
    paid:str
    remaining:str
    branch:str
    course:str
    semister:str


class show_fee_details(pyd.BaseModel):
    stu_id:str
    paid:str
    remaining:str
    branch:str
    course:str
    semister:str
    stu_relation:show_student
    class Config:
        orm_mode=True


class show_only_name(pyd.BaseModel):
    stu_id:str
    class Config:
        orm_mode=True
class hostel(pyd.BaseModel):
    uuid_id: UUID = pyd.Field(default_factory=uuid.uuid4)
    room_num:int
    hostel_name:str

class show_hostel(pyd.BaseModel):
    room_num:int
    hostel_name:str
    class Config:
        orm_mode=True


class TokenDatas(pyd.BaseModel):
    stu_id: str | None = None


class TokenDataf(pyd.BaseModel):
    fac_id: str | None = None


class show_marks_semister(pyd.BaseModel):
    subject_name:str
    marks:int
    class Config:
        orm_mode=True
