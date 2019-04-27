from data.data import generate_df


def filter_df(roi):
    '''Inputs the roi dataframe and applies various filters and sorts it and returns the new dataframe'''

    roi['wk'] = roi['wk'].astype('int')

    roi = roi.sort_values('wk', ascending=True).reset_index()

    del roi['index']

    roi['t'] = roi.index + 1

    return roi

roi = generate_df('data/roi.sql')
roi = filter_df(roi)

print(roi.head())
