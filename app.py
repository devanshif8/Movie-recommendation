import streamlit as st
import pickle
import pandas as pd
import os
# from dotenv import load_dotenv
import requests




api_key = "c7633645da556bf52bb3c968dbd6d375"   

#api_key = os.getenv('TMDB_API_KEY')
#access_token = os.getenv('TMDB_ACCESS_TOKEN')

#def fetch_poster(movie_id):
    #url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    #response = requests.get(url)
    #data = response.json()
    #print(data)
    #poster_path = data['poster_path']
    #full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    #return full_path

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url)
    data = response.json()
    print("Response keys:", data.keys())


    # Safely get the poster path
    poster_path = data.get('poster_path')

    if poster_path:
        # If poster exists, build the full image URL
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    else:
        # Handle missing posters (fallback)
        return "https://via.placeholder.com/500x750?text=No+Poster+Available"


def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id   # for movie id for pposter
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
    names,posters = recommend(selected_movie_name)
    st.subheader("Recommended Movies:")
    #for i in recommendations:
     #   st.write(i)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])