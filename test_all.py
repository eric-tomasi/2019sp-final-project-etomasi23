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



def test_competitors_growing():

    df['test'] = df.apply(competitors_growing, axis=1)

    assert df.iloc[0,-1] == 4
    assert df.iloc[3,-1] == 0
