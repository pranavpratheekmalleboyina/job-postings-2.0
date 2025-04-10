from sqlalchemy import create_engine,text
from dotenv import load_dotenv
import os

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