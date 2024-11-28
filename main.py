
import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['movie_name'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:4]

    recommended_movies =[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].movie_name)
    return recommended_movies

movies_dict = pickle.load(open('C:/Users/Balu/ML Projects/Recommendation engine using GraphRAG architecture/movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('C:/Users/Balu/ML Projects/Recommendation engine using GraphRAG architecture/similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Tell me which movie you like. I will recommend similar movies...',
    movies['movie_name'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

