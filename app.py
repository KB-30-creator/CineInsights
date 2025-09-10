#Importing libraries
import streamlit as st
import pickle
import requests


#loading data
movies = pickle.load(open('movie_list.pkl','rb'))
movies_list= movies['title'].values
similarity = pickle.load(open('similarity.pkl','rb'))


# 🎨 Custom CSS for fonts, background, sidebar
st.markdown(
    """
    <style>
    /* Main App background with cinema vibe */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1524985069026-dd778a71c7b4");
        background-size: cover;
        background-attachment: fixed;
        color: white;
    }

    /* Title styling */
    .big-title {
        font-size: 42px !important;
        color: #FFD700;  /* Gold color */
        font-weight: bold;
        text-align: center;
        margin-bottom: -10px;
        text-shadow: 2px 2px 4px #000000;
    }

    /* Tagline styling */
    .tagline {
        font-size: 18px;
        color: #f5f5f5;
        text-align: center;
        margin-bottom: 30px;
        font-style: italic;
        text-shadow: 1px 1px 3px #000000;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: rgba(30, 30, 30, 0.95);
        color: white;
    }
    [data-testid="stSidebar"] .css-1d391kg {
        color: white;
    }

    /* Movie card styling */
    .movie-card {
        background-color: rgba(38, 39, 48, 0.9);
        padding: 12px;
        border-radius: 10px;
        margin: 8px 0;
        color: white;
        font-size: 18px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.6);
    }
    </style>
    """,
    unsafe_allow_html=True
)


# 🎬 Website Branding
st.markdown('<p class="big-title">🎥 CineInsights</p>', unsafe_allow_html=True)
st.markdown('<p class="tagline">Smart Movie Recommendations</p>', unsafe_allow_html=True)


# Sidebar
st.sidebar.title("⚡ What's the next watch?")
st.sidebar.write("Select a movie from the dropdown to get recommendations!")


# Dropdown
selected_movie_name = st.selectbox(
    "🎬 Select a movie",
    movies_list
)


# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append((movies.iloc[i[0]].title, i[1]))  # include similarity score
    return recommended_movies



# Button
if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    st.subheader("✨ Recommended Movies for You:")
    for movie_name, score in recommendations:
        st.markdown(
            f"""
            <div class="movie-card">
                🎬 <b>{movie_name}</b><br>
                🔗 Similarity Score: {round(score*100, 2)}%
            </div>
            """,
            unsafe_allow_html=True
        )