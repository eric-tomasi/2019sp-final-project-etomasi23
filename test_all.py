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



def test_flat_decline_sun():

    df['test'] = df.apply(flat_decline_sun, axis=1)

    assert df.iloc[23,-1] == 5
    assert df.iloc[19,-1] == -5
    assert df.iloc[17,-1] == -7
    assert df.iloc[1,-1] == 0


def test_high_comp():

    df['test'] = df.apply(high_comp, axis=1)

    assert df.iloc[0,-1] == 0
    assert df.iloc[2,-1] == 2
    assert df.iloc[15,-1] == 2


def test_sun_250():

    df['test'] = df.apply(sun_250, axis=1)

    assert df.iloc[0,-1] == 0.5
    assert df.iloc[26,-1] == 0
