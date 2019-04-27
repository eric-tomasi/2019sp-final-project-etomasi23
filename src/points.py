from data.data import generate_df


df = generate_df('data/query.sql')

def competitors_growing(df):
    '''Assigns 4 points to record if competitor volume is growing'''

    if ( (df['comp1_curr_vol'] > df['comp2_prev_vol']) or (df['comp2_curr_vol'] > df['comp2_prev_vol']) ):
        return 4
    else:
        return 0


def flat_decline_sun(df):

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

print(df.columns)
