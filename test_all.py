from src.points import *
from src.data.data import generate_df

df = generate_df('src/data/query.sql')

df = df.sort_values(['terr',
                 'dcl',
                 'tier',
                 'sun_curr_vol',
                 'comp1_curr_vol',
                 'comp2_curr_vol'],

                ascending=[True,
                          False,
                          False,
                          False,
                          False,
                          False]
                    )

def testing_competitors_growing():

    print(df.head())

    df['test'] = df.apply(competitors_growing, axis=1)

testing_competitors_growing()
