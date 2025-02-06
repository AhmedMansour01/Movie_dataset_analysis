# import pandas with shortcut 'pd' 
import pandas as pd 
  
df = pd.read_csv(r'C:\Users\احمد سامي\OneDrive\Desktop\tmdb\tmdb_5000_genres.csv') 

#delete unwanted columns
df.pop('budget')
df.pop('genres')
df.pop('homepage')
df.pop('keywords')
df.pop('original_language')
df.pop('overview')
df.pop('popularity')
df.pop('production_companies')
df.pop('production_countries')
df.pop('release_date')
df.pop('revenue')
df.pop('spoken_languages')
df.pop('status')
df.pop('tagline')
df.pop('vote_average')
df.pop('vote_count')

df.to_csv(r'C:\Users\احمد سامي\OneDrive\Desktop\tmdb\tmdb_5000_genres.csv', index=False)