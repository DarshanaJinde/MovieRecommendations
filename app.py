import pickle
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu



def recommend(movie):
    index = movies[movies['Series_Title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        recommended_movie_posters.append(movies.iloc[i[0]].Poster_Link)
        recommended_movie_names.append(movies.iloc[i[0]].Series_Title)

    return recommended_movie_names,recommended_movie_posters

movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
popular = pickle.load(open('popular.pkl','rb'))

title = popular['Series_Title'].to_list()
image = popular['Poster_Link'].to_list()


with st.sidebar:
    page = option_menu(
        menu_title = None,
        options = ["Home","Search"],
        icons = ["house","search"],
    )
if page == "Search":
    st.title("Movie Recommendation System")

    movie_list = movies['Series_Title'].values
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )

    if st.button('Show Recommendation'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    
        cols = st.columns(5)
    
        for i in range(5):
            with cols[i]:
                st.text(recommended_movie_names[i])
                st.image(recommended_movie_posters[i])
    

if page == "Home":

    st.header("Most Popular Movies")
    
    for i in range(0, len(image), 5):
    # Create columns for each group of 5 items
        col1, col2, col3, col4, col5 = st.columns(5)

    # Iterate over the range of the 5 columns (index 0 to 4) and display content
        for j, col in enumerate([col1, col2, col3, col4, col5]):
            index = i + j  # The index for the current item
            if index < len(image):  # To avoid going out of bounds
                with col:
                    st.image(image[index])
                    st.text(title[index])