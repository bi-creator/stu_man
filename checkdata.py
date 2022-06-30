import sqlalchemy as sql
import sqlalchemy.ext.declarative as dec
import sqlalchemy.orm as ses



#SQLALCHEMY_DATABASE_URL = "sqlite:///./base.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:manjith@localhost:5432/checkdata"

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
    # course_name=sql.Column(sql.ForeignKey('coursedetails.course_name'))
    # semister_num = sql.Column(sql.ForeignKey('semister.semister_num'))
    # attandance=sql.Column(sql.Integer)
    # branch=sql.Column(sql.String,sql.ForeignKey('Branchdetails.branch_name'))
    # fee_relation=ses.relationship('fee_details',back_populates='stu_relation')
