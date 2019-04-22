import pandas as pd
from sqlalchemy import types, create_engine
from sqlalchemy.orm import sessionmaker
import os


def sql_query(filename):
    '''reads in a .sql file and returns string so it can be read into pandas.'''

    # Open and read the file as a single buffer
    with open(filename, 'r') as fd:
        sqlFile = fd.read()
        return sqlFile


def generate_df(query_file):
    '''input a .sql file as a string. returns pandas dataframe from the result set'''
    #SQL Alchemy connection
    engine = create_engine('oracle://{}:{}@{}'.format(os.environ.get('USER'), os.environ.get('PW'), os.environ.get('DB')))

    conn = engine.connect()

    # Construct a sessionmaker object
    Session = sessionmaker()

    # Bind the sessionmaker to engine
    Session.configure(bind=engine)

    #Session
    db_session = Session()

    df = pd.read_sql(sql_query(query_file), con=conn)

    db_session.close()
    conn.close()

    return df
