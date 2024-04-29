import pickle
import numpy as np
import streamlit as st


def find_similar(title, num_similar=3):
    index = movies[movies['title'] == title].index[0]
    vector = similarity[index, :]
    most_similar_indices = np.argsort(vector)[1:num_similar+1]
    most_similar_titles = [movies.iloc[idx, 1] for idx in most_similar_indices]
    return most_similar_titles

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values



def main():
    st.title("🎬 Movie Recommender System")

    selected_movie = st.selectbox(
        "Type or select a movie you like :",
        movie_list
    )

    if st.button('Show Recommendation'):
        st.write("Recommended Movies based on your interests are :")
        col1, col2, col3 = st.columns(3)
        recommended_movie_names = find_similar(selected_movie)

        with col1:
            st.text(recommended_movie_names[0])
        with col2:
            st.text(recommended_movie_names[1])
        with col3:
            st.text(recommended_movie_names[2])

if __name__ == "__main__":
    main()
