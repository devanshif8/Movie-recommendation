import streamlit as st
import pickle
import pandas as pd
from dotenv import load_dotenv

api_key = os.getenv('IMDB_API_KEY')
api_secret = os.getenv('IMDB_API_SECRET')


def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id=i[0]    # for movie id for pposter
        #feth poster from api 
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


# Load data
movies_dict1 = pickle.load(open("movies_dict1.pkl", "rb"))
movies = pd.DataFrame(movies_dict1)
similarity = pickle.load(open("similarity.pkl", "rb"))

# App layout
st.title("Movie Recommender System")

selected_movie_name = st.selectbox("Select a movie:", movies["title"].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    st.subheader("Recommended Movies:")
    for i in recommendations:
        st.write(i)
  


# we will fecth poster usin id