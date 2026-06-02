# =========================================================
# IMPORT LIBRARIES
# =========================================================

import streamlit as st
import pickle
import joblib
import base64

from sklearn.metrics.pairwise import cosine_similarity
from streamlit_option_menu import option_menu

from pages.trending import show_trending_page

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="CineScout",
    page_icon="🎬",
    layout="wide"
)

# =========================================================
# LOAD FILES
# =========================================================

movies = pickle.load(open("movies_list.pkl", "rb"))

vectors = joblib.load("vectors.pkl")

movies_list = movies['title'].values

# =========================================================
# BACKGROUND IMAGE FUNCTION
# =========================================================

def add_bg_from_local(image_file):

    with open(image_file, "rb") as image:

        encoded_string = base64.b64encode(image.read()).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{

            background-image:
                linear-gradient(
                    rgba(0,0,0,0.88),
                    rgba(0,0,0,0.88)
                ),
                url("data:image/png;base64,{encoded_string}");

            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# LOAD BACKGROUND IMAGE
# =========================================================

try:
    add_bg_from_local("bg.png")

except:
    pass

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* Hide Streamlit Branding */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}
            

/* Main Container */

.block-container {

    padding-top: 1rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

            
/* Logo */

.logo-text {
    font-family:
            "Lucida Handwriting",
            "Lucida Calligraphy",
            cursive;
    font-size: 65px;
    font-weight: 600;
    margin-top: 10px;
    letter-spacing: -1px;
    background:
        linear-gradient(
            135deg,
            #ff3366 0%,
            #b30000 100%
        );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter:
        drop-shadow(
            3px 5px 8px rgba(0, 0, 0, 0.2)
        );
    transition: transform 0.3s ease;
}

.logo-text:hover {
    transform: scale(1.03) rotate(-3deg);
}

            
/* Main Heading */

.main-title {
    text-align: center;
    color: #ff0000;
    font-size: 65px;
    font-weight: 600;
    margin-top: 40px;
}

.sub-title {
    text-align: center;
    color: white;
    font-size: 22px;
    margin-bottom: 40px;
}

            
/* Movie Cards */

.movie-card {
    background: rgba(255,255,255,0.08);
    padding: 15px;
    border-radius: 15px;
    transition: 0.3s;
    text-align: center;
    margin-bottom: 20px;
}

.movie-card:hover {
    transform: scale(1.05);
    background: rgba(255,255,255,0.12);
}

            
/* Buttons */

.stButton > button {
    background-color: #ff0000;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px 25px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    background-color: #cc0000;
    transform: scale(1.05);
}

            
/* Dropdown */

label {
    font-size: 24px !important;
    font-weight: 700 !important;
    color: white !important;
}

div[data-baseweb="select"] div {
    font-size: 20px !important;
    font-weight: 600 !important;
    color: white !important;
}

div[data-baseweb="select"] > div {
    min-height: 48px;
    background-color: rgba(255,255,255,0.08);
    border-radius: 14px;
    padding-left: 30px;
    border: 1px solid black;
}

ul {
    font-size: 22px !important;
}

li {
    font-size: 20px !important;
    font-weight: 600 !important;
    color: white !important;
    padding-top: 14px !important;
    padding-bottom: 14px !important;
}

li:hover {
    background-color:
        rgba(255,0,0,0) !important;
    color: red !important;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# POSTER FUNCTION
# =========================================================

FALLBACK_POSTER = (
    "https://via.placeholder.com/"
    "500x750.png?text=No+Image"
)

def fetch_poster(poster_path):

    try:
        if poster_path and poster_path != "":

            full_path = (
                "https://image.tmdb.org/t/p/w500"
                + poster_path
            )

            return full_path
        return FALLBACK_POSTER

    except:
        return FALLBACK_POSTER

# =========================================================
# RECOMMENDATION FUNCTION
# =========================================================

def recommend(movie):

    movie_index = movies[
        movies['title'] == movie
    ].index[0]

    movie_vector = vectors[movie_index]

    similarity = cosine_similarity(
        movie_vector,
        vectors
    ).flatten()

    distances = sorted(
        list(enumerate(similarity)),
        reverse=True,
        key=lambda x: x[1]
    )[1:11]

    recommended_movies = []

    recommended_posters = []

    for i in distances:

        movie_data = movies.iloc[i[0]]

        recommended_movies.append(
            movie_data.title
        )

        poster_path = movie_data.get(
            'poster_path',
            ''
        )

        recommended_posters.append(
            fetch_poster(poster_path)
        )

    return recommended_movies, recommended_posters

# =========================================================
# TOP SECTION
# =========================================================

left_col, right_col = st.columns([2, 1])

# =========================================================
# LOGO
# =========================================================

with left_col:

    st.markdown(
        """
        <div class="logo-text">
            CineScout
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# NAVBAR
# =========================================================

with right_col:

    selected = option_menu(

        menu_title=None,

        options=[
            "Home",
            "Trending"
        ],

        icons=[
            "house-fill",
            "fire"
        ],

        default_index=0,

        orientation="horizontal",

        styles={

            "container": {
                "padding": "0px",
                "background-color": "#050b18",
                "border-radius": "12px",
                "width": "100%",
                "margin": "1px",
            },

            "icon": {
                "color": "white",
                "font-size": "16px",
            },

            "nav-link": {
                "font-size": "16px",
                "font-weight": "600",
                "text-align": "center",
                "padding": "10px 0px",
                "color": "white",
                "--hover-color": "#111",
            },

            "nav-link-selected": {
                "background-color": "red",
                "border-radius": "10px",
            },
        }
    )

# =========================================================
# HOME PAGE
# =========================================================

if selected == "Home":

    st.markdown(
        """
        <div class="main-title">
            <h1>Movie Recommendation Engine</h1>
        </div>

        <div class="sub-title">
            Discover the Movies of Your Favorite Genres 🎬
        </div>
        """,
        unsafe_allow_html=True
    )

    selected_movie = st.selectbox(
        "Select a Movie",
        movies_list
    )

    if st.button("Show Recommendation"):

        recommend_movie, recommend_poster = recommend(
            selected_movie
        )

        # FIRST ROW

        cols = st.columns(5)

        for col, title, poster in zip(
            cols,
            recommend_movie[:5],
            recommend_poster[:5]
        ):

            with col:

                st.markdown(
                    "<div class='movie-card'>",
                    unsafe_allow_html=True
                )

                st.image(
                    poster,
                    use_container_width=True
                )

                st.markdown(
                    f"""
                    <h4 style='color:white;'>
                    {title}
                    </h4>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                )

        # SECOND ROW

        cols2 = st.columns(5)

        for col, title, poster in zip(
            cols2,
            recommend_movie[5:10],
            recommend_poster[5:10]
        ):

            with col:

                st.markdown(
                    "<div class='movie-card'>",
                    unsafe_allow_html=True
                )

                st.image(
                    poster,
                    use_container_width=True
                )

                st.markdown(
                    f"""
                    <h4 style='color:white;'>
                    {title}
                    </h4>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                )

# =========================================================
# TRENDING PAGE
# =========================================================

elif selected == "Trending":
    show_trending_page()
