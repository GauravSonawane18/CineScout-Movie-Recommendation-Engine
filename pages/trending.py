import streamlit as st
import requests
# from dotenv import load_dotenv
# import os

# =========================================================
# API KEY
# =========================================================

# load_dotenv()

API_KEY = st.secrets["TMDB_API_KEY"]

FALLBACK_POSTER = "https://via.placeholder.com/500x750.png?text=No+Image"

# =========================================================
# FETCH TRENDING MOVIES
# =========================================================

def fetch_trending_movies():

    url = (
        f"https://api.themoviedb.org/3/"
        f"trending/movie/week?api_key={API_KEY}"
    )

    try:
        response = requests.get(url)
        data = response.json()

        # SAFE CHECK
        if 'results' in data:
            return data['results']

        else:
            st.error("TMDB API Error")
            return []

    except Exception as e:
        st.error(f"Error: {e}")
        return []

# =========================================================
# TRENDING PAGE UI
# =========================================================

def show_trending_page():

    st.markdown(
    """
    <style>

    .trending-header {
        text-align: center;
        margin-bottom: 50px;
    }

    .trending-header h1 {
        color: #ff0000;
        font-size: 65px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .trending-header p {
        color: white;
        font-size: 24px;
    }

    </style>
    """,
    unsafe_allow_html=True
    )

    trending_movies = fetch_trending_movies()

    cols = st.columns(5)

    for idx, movie in enumerate(trending_movies[:15]):

        with cols[idx % 5]:

            title = movie.get('title', 'No Title')

            poster_path = movie.get('poster_path')

            vote = movie.get('vote_average', 'N/A')

            release_date = movie.get(
                'release_date',
                'Unknown'
            )

            if poster_path:

                poster_url = ("https://image.tmdb.org/t/p/w500" + poster_path)

            else:

                poster_url = FALLBACK_POSTER

            st.markdown(
                "<div class='movie-card'>",
                unsafe_allow_html=True
            )

            st.image(poster_url)

            st.markdown(
                f"""
                <h3 style='
                    color:white;
                    text-align:center;
                    min-height:70px;
                '>
                {title}
                </h3>

                <p style='
                    color:#ff4b4b;
                    text-align:center;
                    font-size:18px;
                    font-weight:600;
                '>
                ⭐ {vote}
                </p>

                <p style='
                    color:#cccccc;
                    text-align:center;
                    font-size:15px;
                '>
                📅 {release_date}
                </p>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )