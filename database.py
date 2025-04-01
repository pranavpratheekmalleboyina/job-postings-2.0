from sqlalchemy import create_engine,text

engine = create_engine("mysql+pymysql://root:pranavpratheek@127.0.0.1/pranavconsultancy")

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(result.all())