import fastapi as api
import sqlalchemy.orm as ses
import checkdata as cd
import checkschema as cs
import hashing as hs


cd.ba.metadata.create_all(bind=cd.engine)
def getting():
    dd=cd.se()
    try:
        yield dd
    finally:
        dd.close()

checkstu=api.FastAPI()
@checkstu.post("/new student", response_model=cs.sturesponce)

def create(req:cs.newstudent, dd:ses.Session=api.Depends(getting)):
    hashedpass=hs.pwd_context.hash(req.pas)
    newuser=cd.student_details(stu_id=req.id, first_name=req.first_name,
                               middle_name=req.middle_name,last_name=req.last_name,pasword=hashedpass,phone_num=req.number,email=req.mail)
    dd.add(newuser)
    dd.commit()
    dd.refresh(newuser)
    newuser=dd.query(cd.student_details).filter(cd.student_details.stu_id==req.id).first()
    return newuser
