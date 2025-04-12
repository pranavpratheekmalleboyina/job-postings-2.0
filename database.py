from sqlalchemy import create_engine,text
from dotenv import load_dotenv
import os
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
load_dotenv() #loads from the .env file

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs")).mappings().all()
        result_dicts = []
    
        for row in result:
            result_dicts.append(dict(row))
        
        return result_dicts
    
def load_job_from_db(job_id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs where id= :val"),{"val" : job_id}).mappings().all()
        rows = result
    
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0])
        
def save_application_to_db(job_id,data): 
    with engine.connect() as conn:
        query = text("insert into applications(job_id,full_name,email,linkedin_url,education,work_experience,resume_url) values(:job_id,:full_name,:email,:linkedin_url,:education,:work_experience,:resume_url)") 
        transaction = conn.begin()
        try:
            status = conn.execute(query,{
                      "job_id":job_id,
                      "full_name": data['full_name'],
                      "email" : data['email'],
                      "linkedin_url" :data['linkedin_url'],
                      "education": data['education'],
                      "work_experience": data['work_experience'],
                      "resume_url" : data['resume_url']
                      } )  
            transaction.commit()   #used for all the insert statements
        except:
            transaction.rollback()         