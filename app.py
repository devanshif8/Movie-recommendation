import streamlit as st
import pickle
import pandas as pd
import os
# from dotenv import load_dotenv
import requests





api_key = os.getenv('TMDB_API_KEY')
access_token = os.getenv('TMDB_ACCESS_TOKEN')

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url)
    data = response.json()
    print(data)
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path



def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id=i[0]    # for movie id for pposter
        recommended_movies.append(movies.iloc[i[0]].title)
        #feth poster from api 
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movie_posters


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
  

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.text(recommendations[0][0])
    st.image(recommendations[1][0])
with col2:
    st.text(recommendations[0][1])
    st.image(recommendations[1][1])
with col3:
    st.text(recommendations[0][2])
    st.image(recommendations[1][2])
with col4:
    st.text(recommendations[0][3])
    st.image(recommendations[1][3])
with col5:
    st.text(recommendations[0][4])
    st.image(recommendations[1][4])