from sqlalchemy import create_engine, text
import os

connection_string=os.environ['DB_CONNECTION_STING']

engine = create_engine(connection_string, connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })

#get some information out of engine by making connection to database
def load_jobs_db():
  with engine.connect() as connection:
    result = connection.execute(text("select * from jobs"))
    jobs_list=[]
    for row in result:
        row_dict=row._mapping
        jobs_list.append(row_dict)
    return jobs_list