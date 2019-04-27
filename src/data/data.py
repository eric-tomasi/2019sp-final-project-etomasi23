import pandas as pd
from sqlalchemy import types, create_engine
from sqlalchemy.orm import sessionmaker
import os
import hashlib


def sql_query(filename):
    '''reads in a .sql file and returns string so it can be read into pandas.'''

    # Open and read the file as a single buffer
    with open(filename, 'r') as fd:
        sqlFile = fd.read()
        return sqlFile


def hash_col(val):
    '''uses sha256 algorithm to hash a single string. returns hexidecimal value with 8 characters'''

    #.env file contains secret key called SALT
    salt = os.environ.get('SALT')

    m = hashlib.sha256()
    m.update(val.to_csv(header=False).encode())
    m.update(salt.encode())

    return m.hexdigest()[:8]

def generate_df(query_file):
    '''Input a .sql file as a string and return a dataframe of the result set. ID column uses sha256 hash with SALT'''
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

    if query_file == 'data/query.sql':
        df['id'] = df.apply(hash_col,axis=1)

    db_session.close()
    conn.close()

    return df
