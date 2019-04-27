from data.data import generate_df


def competitors_growing(df):
    '''Assigns 4 points to record if competitor volume is growing'''

    if ( (df['comp1_curr_vol'] > df['comp2_prev_vol']) or (df['comp2_curr_vol'] > df['comp2_prev_vol']) ):
        return 4
    else:
        return 0


def flat_decline_sun(df):
    '''Assigns 5 points if declining in non-competitor volume, and penalizes if non-comptetior is growing'''

    if ((df['sun_curr_vol']) <= (df['sun_prev_vol'])):
        return 5
    elif ((df['sun_curr_vol']) > (1.5*df['sun_prev_vol'])):
        return -7
    elif ((df['sun_curr_vol']) > (1.25*df['sun_prev_vol'])):
        return -6
    elif ((df['sun_curr_vol']) > (1.1*df['sun_prev_vol'])):
        return -5
    else:
        return 0


def high_comp(df):
    '''Assigns 2 points to records that have high competitor volume'''

    if (df['comp1_curr_vol'] > 600):
        return 2
    elif (df['comp2_curr_vol'] > 600):
        return 2
    else:
        return 0


def sun_250(df):
    '''Assigns .5 points if record has moderate non-competitor volume'''

    if (df['sun_curr_vol'] > 250):
        return 0.5
    else:
        return 0.0


def decile(df):
    '''Assigns points to record on sliding scale based on decile'''

    if (df['dcl'] == 10) or (df['dcl'] == 9) or (df['dcl'] == 8) or (df['dcl'] == 7):
        return 1.0
    elif (df['dcl'] == 6) or (df['dcl'] == 5):
        return 0.5
    elif (df['dcl'] == 4) or (df['dcl'] == 3):
        return 0.25
    else:
        return 0.0


def any_comp(df):
    '''Assigns .25 points to record if they have any competitor volume'''

    if ((df['comp1_curr_vol'] > 0) or (df['comp2_curr_vol'] > 0)):
        return 0.25
    else:
        return 0.0


def any_sun(df):
    '''Assigns .25 points to record if they have any non-competitor volume'''

    if (df['sun_curr_vol'] > 0):
        return 0.25
    else:
        return 0


def tier_points(df):

    if (df['tier'] == 'TIER 1'):
        return 2.5
    elif (df['tier'] == 'TIER 2') or (df['tier'] == 'TIER 3'):
        return 2.0
    elif (df['tier'] == 'TIER 4'):
        return 1.0
    elif (df['tier'] == 'TIER 5'):
        return -1.0
    else:
        return 0


def apply_funcs(df):
    '''Applies all functions to existing datarame and stores results in a new column. Returns new df'''

    func_list = [competitors_growing, flat_decline_sun, high_comp, sun_250, decile, any_comp, any_sun, tier_points]

    for func in func_list:
        df[func.__name__] = df.apply(func, axis=1)

    return df


def total_points(df):
    '''Calculate total points from columns derived by the apply_funcs function'''

    df = apply_funcs(df)

    col_list = ['competitors_growing', 'flat_decline_sun', 'high_comp', 'sun_250', 'decile', 'any_comp', 'any_sun', 'tier_points']

    df['TOTAL_POINTS'] = df[col_list].sum(axis=1)

    return df


def final_target_list(df):
    '''Input initial datafram from generate_df and return final datafram consisting of top 20 targets by territory'''

    df = total_points(df)

    df = df.sort_values(['terr',
                     'TOTAL_POINTS',
                     'dcl',
                     'tier',
                     'sun_curr_vol',
                     'comp1_curr_vol',
                     'comp2_curr_vol'],

                    ascending=[True,
                              False,
                              False,
                              True,
                              False,
                              False,
                              False]
                        )

    df['RANK'] = df.groupby('terr').cumcount()+1

    final_target_list = df[['id', 'terr', 'RANK']]
    final_target_list = final_target_list[final_target_list['RANK'] <= 20]
    final_target_list = final_target_list[final_target_list['terr'] != 'H99699992']

    return final_target_list


df = generate_df('data/query.sql')
df2 = total_points(df)


#in main.py, send both dfs from total_points and final_target_list to an excel workbook.


print(df2.head())
