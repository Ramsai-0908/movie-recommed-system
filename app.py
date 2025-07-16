import pandas as pd
import streamlit as st

# Load movies.csv
movies = pd.read_csv('movies.csv')

# Input from user
keyword = st.text_input("Enter a keyword (e.g., love, war, hero):")

# Filter by checking in both title and genres
if keyword:
    filtered = movies[
        movies['title'].str.contains(keyword, case=False, na=False) |
        movies['genres'].str.contains(keyword, case=False, na=False)
    ]

    # Display results
    if not filtered.empty:
        st.write(filtered[['movieId', 'title']].head(10))
    else:
        st.write("No movies found matching your keyword.")