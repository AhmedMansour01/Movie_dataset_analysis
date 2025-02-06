import pandas as pd
#read file
df = pd.read_csv(r'C:\Users\احمد سامي\OneDrive\Desktop\tmdb\tmdb_5000_genres.csv')

#seperate the genres column into a genre_id and genre_name columns
df[['genre_id', 'genre_name']] = df['genres'].str.split('  ', expand=True)


df.to_csv(r'C:\Users\احمد سامي\OneDrive\Desktop\tmdb\tmdb_5000_genres.csv', index=False)