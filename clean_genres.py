import pandas as pd
#read file
df = pd.read_csv(r'C:\Users\احمد سامي\OneDrive\Desktop\tmdb\tmdb_5000_genres.csv')
#remove null values
df.dropna(subset=['genres'], inplace=True)
df['genres'] = df['genres'].str.strip()
df.to_csv(r'C:\Users\احمد سامي\OneDrive\Desktop\tmdb\tmdb_5000_genres.csv', index=False)