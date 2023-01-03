import pandas as pd
import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

st.title("Sourabh's Movie Recommender System")

selected_movie_name = st.selectbox(
    'Enter your movie for recommendations ?',
    movies['title'].values)

st.write('You selected:', selected_movie_name)

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=7d5c1ec2c66bf38b6b7f38baab3ca291&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(enumerate(distances), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

similarity=pickle.load(open('similarity.pkl','rb'))

if st.button('Show Recommendations'):
    recommend_movie_names,recommend_movie_poster =recommend(selected_movie_name)

    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(recommend_movie_names[0])
        st.image(recommend_movie_poster[0])
    with col2:
        st.text(recommend_movie_names[1])
        st.image(recommend_movie_poster[1])
    with col3:
        st.text(recommend_movie_names[2])
        st.image(recommend_movie_poster[2])
    with col4:
        st.text(recommend_movie_names[3])
        st.image(recommend_movie_poster[3])
    with col5:
        st.text(recommend_movie_names[4])
        st.image(recommend_movie_poster[4])


#movies_list_df = pickle.load(open('movies.pkl','rb'))
#movies_list_df = movies_list_df['title'].values
