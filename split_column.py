import pandas as pd

#read file
df = pd.read_csv(r'C:\Users\احمد سامي\OneDrive\Desktop\tmdb\tmdb_5000_movies.csv')

#clean the genre column
df['genres'] = df['genres'].replace(['\[','\]'], ['',''], regex=True)
df['genres'] = df['genres'].replace(['"','{','name','id',':',','], ['','','','','',''], regex=True)
df['genres'] = df['genres'].str.strip()

#split column
df['genres'] = df['genres'].str.split('}')
df = df.explode('genres')

#input the data into the new file
df.to_csv(r'C:\Users\احمد سامي\OneDrive\Desktop\tmdb\tmdb_5000_genres.csv', index=False)
