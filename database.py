from sqlalchemy import create_engine, text

connection_string="mysql+pymysql://vzfm70vr3wrhj37etz1n:pscale_pw_LecQhcjYx5RH6T5oLY01MWHIfcQvbYOBtHvxEs0Zs8E@aws.connect.psdb.cloud/trial-career-web?charset=utf8mb4"

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