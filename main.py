from distutils.log import INFO
from typing import List
import fastapi as api
import pydantic as pyd
import sqlalchemy.orm as ses
import students as ct
import sschemas as ss
import hashing as hs
import for_taken as tok
import oauth2 as ou
import logging
from fastapi.security import  OAuth2PasswordRequestForm
# DEBUG_LEVELV_NUM = 69 
# logging.addLevelName(DEBUG_LEVELV_NUM, "DEBUGV")
# def debugv(self, message, *args, **kws):
#     # Yes, logger takes its '*args' as 'args'.
#     self._log(DEBUG_LEVELV_NUM, message, args, **kws) 
# logging.Logger.debugv = debugv

loger=logging.getLogger('first_log')
loger.setLevel(logging.INFO)
form=logging.Formatter(' %(message)s-%(asctime)s', datefmt='%m/%d/%Y %I:%M:%S %p')
f_handler=logging.FileHandler('log.log')
f_handler.setLevel(logging.INFO)
f_handler.setFormatter(form)
loger.addHandler(f_handler)

ct.ba.metadata.create_all(bind=ct.engine)
def getting():
    dd=ct.se()
    try:
        yield dd
    finally:
        dd.close()

stu=api.FastAPI()
#logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
# logging.basicConfig(level=69,
#                     filename="basehistory.txt",
#                     format=' %(message)s-%(asctime)s', datefmt='%m/%d/%Y %I:%M:%S %p',
#                     filemode='w')

@stu.post('/new student/',response_model=ss.show_student,tags=['Students'])

def create(req:ss.newstudent, dd:ses.Session=api.Depends(getting)):
    hashedpass=hs.pwd_context.hash(req.pas)
    newuser=ct.student_details(stu_id=req.id, first_name=req.first_name,
                               middle_name=req.middle_name,last_name=req.last_name,pasword=hashedpass,phone_num=req.number,email=req.mail,course_name=req.coursename,semister_num=req.semister_num,attandance=req.attandance,branch=req.bran_name)
   
    loger.info(f"student {req.middle_name} created at" )
    dd.add(newuser)
    dd.commit()
    dd.refresh(newuser)
    return newuser

# loger.info("student  created at" )
from routers import new
stu.include_router(new.router)

# @stu.post('/new course',tags=['New '])
# def add_course(req:ss.new_course_details,dd:ses.Session=api.Depends(getting)):
#     newcour=ct.course(course_id=req.course_id,course_name=req.course_name)
#     loger.info(f"course {req.course_name} created at" )
#     dd.add(newcour)
#     dd.commit()
#     dd.refresh(newcour)
#     return newcour


@stu.post('/new BRANCH',tags=['New '])
def add_branch(req:ss.branch,dd:ses.Session=api.Depends(getting)):
    newcour=ct.branch(branch_name=req.branch_name)
    loger.info(f"branch {req.branch_name} created at" )
    dd.add(newcour)
    dd.commit()
    dd.refresh(newcour)
    return newcour

@stu.post('/new Semister',tags=['New '])
def add_sem(req:ss.sem_num,dd:ses.Session=api.Depends(getting)):
    newsem=ct.semister(semister_num=req.sem_num)
    dd.add(newsem)
    dd.commit()
    dd.refresh(newsem)
    return newsem

@stu.post('/new Subjects',tags=['New '])
async def add_sub(req:ss.subjects_info,dd:ses.Session=api.Depends(getting)):
    newsub=ct.subjects(subject_id=req.sub_id,subject_name=req.sub_name,faculty_name=req.faculty_name,course_name=req.course_name,semister_num=req.sem_num,branch_name=req.branch_name)
    dd.add(newsub)
    dd.commit()
    dd.refresh(newsub)
    return newsub


@stu.post('/new faculty',response_model=ss.show_faculty_details,tags=['Faculty'])

def add_faculty(req:ss.newfaculty, dd:ses.Session=api.Depends(getting)):
    hashedpass = hs.pwd_context.hash(req.pas)
    newfac=ct.faculty_details(fac_id=req.id, first_name=req.first_name, middle_name=req.middle_name,last_name=req.last_name,pasword=hashedpass,phone_num=req.number,email=req.mail,tec_sub=req.teaching_sub,tec_branch=req.teaching_branch)
    logging.critical('new faculty added')
    dd.add(newfac)
    dd.commit()
    dd.refresh(newfac)
    return newfac

@stu.post('/enter student marks',tags=['Faculty'])
def student_marks_entry(req:ss.student_marks,dd:ses.Session=api.Depends(getting)):
    marks=ct.student_marks(sno=req.sno,stu_id=req.student_id,semister_num=req.semister_num,subject_name=req.subject_name,marks=req.subject_marks)
    dd.add(marks)
    dd.commit()
    dd.refresh(marks)
    return marks

@stu.post('/update fee details',tags=['Admin'])
def fee_entry(req:ss.fee_details,dd:ses.Session=api.Depends(getting)):
    feed=ct.fee_details(stu_id=req.stu_id,semister=req.semister,branch_name=req.branch,course_enroled=req.course,paied=req.paid,remaining=req.remaining)
    dd.add(feed)
    dd.commit()
    dd.refresh(feed)
    return feed


@stu.post('/Hostel',response_model=ss.show_hostel,tags=['Hostel'])
def hos_entry(req:ss.hostel,dd:ses.Session=api.Depends(getting)):
    feed=ct.hostel(room_num=req.room_num,hostel_name=req.hostel_name)
    dd.add(feed)
    dd.commit()
    dd.refresh(feed)
    return feed
@stu.get('/all students',response_model=List[ss.show_only_name],tags=['Faculty','Admin'])
def all_students(dd:ses.Session=api.Depends(getting)):
    det=dd.query(ct.student_details).all()
    return det

@stu.get('/students with id/{id}',response_model=ss.show_student,tags=['Students','Admin'])
async def all_id(id,dd:ses.Session=api.Depends(getting)):
    det=dd.query(ct.student_details).filter(ct.student_details.stu_id==id).first()
    return det

@stu.get('/students with branch',tags=['Faculty'])
def all_branch(branch,dd:ses.Session=api.Depends(getting)):
    det=dd.query(ct.student_details).filter(ct.student_details.branch==branch).all()
    return det

@stu.get('/fetch student marks with semister and id ',response_model=list[ss.show_marks_semister],tags=['Faculty'])
def all_branch(semister,id,dd:ses.Session=api.Depends(getting)):
    det=dd.query(ct.student_marks).filter(ct.student_marks.semister_num==semister,ct.student_marks.stu_id==id).all()
    return det
@stu.get('/fetch marks with student id',tags=['Students','Admin','Faculty'])
def all_branch(id,dd:ses.Session=api.Depends(getting)):
    det=dd.query(ct.student_marks).filter(ct.student_marks.stu_id==id).all()
    return det


@stu.get('/fee details with student id', response_model=ss.show_fee_details,tags=['Students','Admin'])
def fee_details(id,dd:ses.Session=api.Depends(getting)):
    det=dd.query(ct.fee_details).filter(ct.fee_details.stu_id==id).first()
    return det


@stu.get('/students semister subjects',tags=['joins'])
def fee_details(dd:ses.Session=api.Depends(getting)):
    det=dd.query(ct.subjects).select_from(ct.student_details).filter(ct.student_details.branch=='string').all()
    return det
@stu.post('/Update student Details',tags=['Admin'])
def update():
    pass


@stu.post('/Update faculty Details',tags=['Admin'])
def update():
    pass


@stu.post('/Authorization faculty',tags=['Login'])
def Login_faculty(req:OAuth2PasswordRequestForm=api.Depends(),dd:ses.Session=api.Depends(getting)):
    user=dd.query(ct.faculty_details).filter(ct.faculty_details.fac_id==req.username).first()
    if not user:
        raise api.HTTPException(status_code=404,detail="invalid user")
    if not hs.verify(user.pasword,req.password):
        raise api.HTTPException(status_code=404, detail= "wrong pass")

    access_token = tok.create_access_tokenF(
        data={"sub": user.fac_id})
    return {"access_token": access_token, "token_type": "bearer"}




@stu.post('/Authorization student',tags=['Login'])
def Login_student(req:OAuth2PasswordRequestForm=api.Depends(),dd:ses.Session=api.Depends(getting)):
    user=dd.query(ct.student_details).filter(ct.student_details.stu_id==req.username).first()
    if not user:
        raise api.HTTPException(status_code=404,detail="invalid user")
    if not hs.verify(user.pasword,req.password):
        raise api.HTTPException(status_code=404, detail= "wrong pass")


    access_token = tok.create_access_token(
        data={"sub": user.stu_id})
    return {"access_token": access_token, "token_type": "bearer"}



