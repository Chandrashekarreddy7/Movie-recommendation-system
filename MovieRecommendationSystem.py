import pickle
import streamlit as st
import requests
import base64
import pandas as pd

def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=177c5b9e95c4fae80d94cba297af69d3".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path="http://image.tmdb.org/t/p/w500/"+poster_path
    return full_path




def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distances=sorted(list(enumerate(similar[index])),reverse=True,key=lambda x:x[1] )
    recommend_movies_name=[]
    recommend_movies_poster=[]
    for i in distances[1:6]:
        movie_id=movies.iloc[i[0]].movie_id
        recommend_movies_poster.append(fetch_poster(movie_id))
        recommend_movies_name.append(movies.iloc[i[0]].title)
    return recommend_movies_name,recommend_movies_poster




st.set_page_config(page_title="Movie Recommendation System")
st.header("Movie Recommendation System Using ML")
movies=pd.read_pickle(open("saving/movie_list.pkl",'rb'))
similar=pd.read_pickle(open("saving/similarity.pkl",'rb'))

movie_list=movies['title'].values
selected_movie=st.selectbox(
    "Type any Movie Here",
    movie_list
)

if st.button("Show Recommendation"):
    recommend_movies_name, recommend_movies_poster =recommend(selected_movie)
    #recommend_movies_poster=recommend(selected_movie)
    a,b,c,d,e=st.columns(5)
    with a:
        st.text(recommend_movies_name[0])
        st.image(recommend_movies_poster[0])
    with b:
        st.text(recommend_movies_name[1])
        st.image(recommend_movies_poster[1])
    with c:
        st.text(recommend_movies_name[2])
        st.image(recommend_movies_poster[2])
    with d:
        st.text(recommend_movies_name[3])
        st.image(recommend_movies_poster[3])
    with e:
        st.text(recommend_movies_name[4])
        st.image(recommend_movies_poster[4])

# Convert image to base64
def load_image(image_file):
    with open(image_file, "rb") as image:
        return base64.b64encode(image.read()).decode()

# Load the image
background_image = load_image("background.jpg")  # Ensure the image is in the same directory

# Set the title of the app


# Add CSS to set the background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{background_image}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        height: 100vh;
    }}
    </style>
    """,
    unsafe_allow_html=True
)