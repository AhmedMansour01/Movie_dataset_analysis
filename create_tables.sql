CREATE TABLE public.movies
(
    budget NUMERIC,
    genres TEXT,
    homepage TEXT,
    ID INT PRIMARY KEY,
    keywords TEXT,
    original_language TEXT,
    original_title TEXT,
    overview TEXT,
    popularity NUMERIC,
    production_companies TEXT,
    production_countries TEXT,
    release_date DATE,
    revenue NUMERIC,
    runtime NUMERIC,
    spoken_languages TEXT,
    movie_status TEXT,
    tagline TEXT,
    title TEXT,
    vote_average NUMERIC,
    vote_count NUMERIC
);

CREATE TABLE public.credits
(
    movie_id INT,
    title TEXT,
    the_cast TEXT,
    the_crew TEXT,
    FOREIGN KEY (movie_id) REFERENCES public.movies (ID)
);

CREATE TABLE public.genres
(
    movie_id INT,
    original_title TEXT,
    runtime NUMERIC,
    title TEXT,
    genre_id INT,
    genre_name TEXT,
    FOREIGN KEY (movie_id) REFERENCES public.movies (ID)
);