from fastapi import APIRouter,Depends
from main import getting
import sschemas as ss
from sqlalchemy.orm import Session 
import students as ct


router=APIRouter()

@router.post('/new course',tags=['New '])
def add_course(req:ss.new_course_details,dd:Session=Depends(getting)):
    newcour=ct.course(course_id=req.course_id,course_name=req.course_name)
    # loger.info(f"course {req.course_name} created at" )
    dd.add(newcour)
    dd.commit()
    dd.refresh(newcour)
    return newcour