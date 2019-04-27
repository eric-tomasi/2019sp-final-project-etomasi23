from data.data import generate_df


df = generate_df('data/query.sql')

print(df.head())
