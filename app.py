import streamlit as st
import requests
import pickle 
import pandas as pd
import lzma

with open("movie_dict.pickle","rb") as file:
    movies_dict = pickle.load(file)
movies = pd.DataFrame(movies_dict)

with lzma.open("similarity3.xz", "rb") as file:
    similarity = pickle.load(file)


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=7179d8558db0ffd107a6329fbecee361&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_poster_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
    return full_poster_path
    
    
def recommend(movie):
    movie_index = movies[movies["title"]==movie].index[0]
    distances = similarity[movie_index]
    recommends = sorted(list(enumerate(distances)) , reverse=True , key=lambda x:x[1])[1:11]
    recommended_movies_posters = []
    recommended_movies = []
    for i in recommends:
        recommended_movies_posters.append(fetch_poster(movies["id"].iloc[i[0]]))
        recommended_movies.append(movies["title"].iloc[i[0]])
    return recommended_movies_posters , recommended_movies
    
    
st.title("Movie Rcommender System")

selected_movie = st.selectbox("Select Movie" , (movies["title"].values))

if st.button("Recommend"):
    recommended_movies_posters , recommended_movies = recommend(selected_movie)
          
    col1 , col2 , col3 , col4 , col5  = st.columns(5)
    col6 , col7 , col8 , col9 , col10 = st.columns(5)
    
    with col1:
        st.write(recommended_movies[0])
        st.image(recommended_movies_posters[0])
    with col2:
        st.write(recommended_movies[1])
        st.image(recommended_movies_posters[1])
    with col3:
        st.write(recommended_movies[2])
        st.image(recommended_movies_posters[2])
    with col4:
        st.write(recommended_movies[3])
        st.image(recommended_movies_posters[3])
    with col5:
        st.write(recommended_movies[4])
        st.image(recommended_movies_posters[4])
        
    with col6:
        st.write(recommended_movies[5])
        st.image(recommended_movies_posters[5])
    with col7:
        st.write(recommended_movies[6])
        st.image(recommended_movies_posters[6])
    with col8:
        st.write(recommended_movies[7])
        st.image(recommended_movies_posters[7])
    with col9:
        st.write(recommended_movies[8])
        st.image(recommended_movies_posters[8])
    with col10:
        st.write(recommended_movies[9])
        st.image(recommended_movies_posters[9])    
    
