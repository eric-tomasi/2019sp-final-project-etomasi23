from data.data import generate_df


df = generate_df('data/query.sql')

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

print(df.columns)
