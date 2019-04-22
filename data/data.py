import pandas as pd
from sqlalchemy import types, create_engine
from sqlalchemy.orm import sessionmaker
import os


#SQL Alchemy connection
engine = create_engine('oracle://{}:{}@{}'.format(os.environ.get('USER'), os.environ.get('PW'), os.environ.get('DB')))

conn = engine.connect()

# Construct a sessionmaker object
Session = sessionmaker()

# Bind the sessionmaker to engine
Session.configure(bind=engine)

#Session
db_session = Session()




def sql_query(filename):
    # Open and read the file as a single buffer
    with open(filename, 'r') as fd:
        sqlFile = fd.read()
        return sqlFile



#df = pd.read_sql(sql_query('query.sql'), con=conn)


db_session.close()
conn.close()
