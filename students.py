import sqlalchemy as sql
import sqlalchemy.ext.declarative as dec
import sqlalchemy.orm as ses
from sqlalchemy.dialects.postgresql import UUID
import uuid
import datetime



#SQLALCHEMY_DATABASE_URL = "sqlite:///./base.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:manjith@localhost:5432/studentsdatabase"

engine = sql.create_engine(
    SQLALCHEMY_DATABASE_URL
)
se=ses.sessionmaker(autocommit=False, autoflush=False, bind=engine)

ba = dec.declarative_base()


class student_details(ba):
    __tablename__='Studentdetails'
   # id = sql.Column(sql.Integer, index=True)
    stu_id=sql.Column(sql.String,index=True, primary_key=True)
    first_name=sql.Column(sql.String)
    middle_name = sql.Column(sql.String)
    last_name = sql.Column(sql.String)
    email=sql.Column(sql.String)
    pasword=sql.Column(sql.String)
    phone_num=sql.Column(sql.String)
    course_name=sql.Column(sql.ForeignKey('coursedetails.course_name'))
    semister_num = sql.Column(sql.ForeignKey('semister.semister_num'))
    attandance=sql.Column(sql.Integer)
    branch=sql.Column(sql.String,sql.ForeignKey('Branchdetails.branch_name'))
    on=sql.Column(sql.DateTime,default=datetime.datetime.utcnow)
    # fee_relation=ses.relationship('fee_details',back_populates='stu_relation')



class faculty_details(ba):
    __tablename__='facultydetails'
    fac_id=sql.Column(sql.String,index=True, primary_key=True)
    first_name = sql.Column(sql.String)
    middle_name = sql.Column(sql.String)
    last_name = sql.Column(sql.String)
    email=sql.Column(sql.String)
    pasword=sql.Column(sql.String)
    phone_num=sql.Column(sql.String)
    tec_sub=sql.Column(sql.String,sql.ForeignKey('subjects.subject_name'))
    tec_branch=sql.Column(sql.String,sql.ForeignKey('Branchdetails.branch_name'))




class subjects(ba):
    __tablename__="subjects"
    subject_id=sql.Column(sql.String)
    subject_name=sql.Column(sql.String,index=True,primary_key=True)
    faculty_name=sql.Column(sql.String)
    course_name = sql.Column(sql.String)
    semister_num = sql.Column(sql.ForeignKey('semister.semister_num'))
    branch_name=sql.Column(sql.String,sql.ForeignKey('Branchdetails.branch_name'))

class fee_details(ba):
    __tablename__ = "feedetails"
    stu_id=sql.Column(sql.ForeignKey('Studentdetails.stu_id'),index=True,primary_key=True)
    paied=sql.Column(sql.String)
    remaining=sql.Column(sql.String)
    branch_name=sql.Column(sql.ForeignKey('Branchdetails.branch_name'))
    course_enroled=sql.Column(sql.ForeignKey('coursedetails.course_name'))
    semister=sql.Column(sql.ForeignKey('semister.semister_num'))
    # stu_relation=ses.relationship('student_details',back_populates='fee_relation')
    # bra_relation = ses.relationship('branch', back_populates='fee_relation')
    # cou_relation = ses.relationship('course', back_populates='fee_relation')
    # sem_relation = ses.relationship('semister', back_populates='fee_relation')


class branch(ba):
    __tablename__="Branchdetails"
    branch_name=sql.Column(sql.String,index=True,primary_key=True)
    #fee_relation = ses.relationship('fee_details', back_populates='bra_relation')




class course(ba):
    __tablename__="coursedetails"

    course_name=sql.Column(sql.String,index=True,primary_key=True)
    course_id = sql.Column(sql.String)
    #fee_relation = ses.relationship('fee_details', back_populates='cou_relation')

class semister(ba):
    __tablename__='semister'
    semister_num=sql.Column(sql.Integer,index=True,primary_key=True)
    #fee_relation = ses.relationship('fee_details', back_populates='sem_relation')


class student_marks(ba):
    __tablename__='student_grades'
    sno=sql.Column(sql.Integer,index=True,primary_key=True)
    stu_id=sql.Column(sql.ForeignKey('Studentdetails.stu_id'))
    semister_num=sql.Column(sql.ForeignKey('semister.semister_num'))
    #branch_name=sql.Column(sql.ForeignKey('Branchdetails.branch_name'))
    #course_name=sql.Column(sql.ForeignKey('coursedetails.course_name'))
    subject_name=sql.Column(sql.ForeignKey('subjects.subject_name'))
    marks=sql.Column(sql.Integer)

class hostel(ba):
    __tablename__='hostel'
    student_hostel_id=sql.Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    #stu_id=sql.Column(sql.ForeignKey('Studentdetails.stu_id'))
    room_num=sql.Column(sql.Integer)
    hostel_name=sql.Column(sql.String)













#ba.metadata.create_all(bind=engine)