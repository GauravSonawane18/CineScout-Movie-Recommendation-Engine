# 🎬 CineScout — Movie Recommendation Engine

CineScout is a modern AI-powered movie recommendation web application built using **Machine Learning**, **TF-IDF Vectorization**, and **Streamlit**.

The application recommends similar movies based on movie metadata and also provides a **live Trending Movies section** powered by the TMDB API.

---

# 🚀 Features

## ✅ AI-Based Movie Recommendation

* Recommends similar movies instantly
* Uses TF-IDF vectorization
* Dynamic cosine similarity computation
* Memory optimized architecture

---

## ✅ Live Trending Movies

* Real-time trending movies from TMDB API
* Displays:

  * Movie Posters
  * Ratings
  * Release Dates

---

## ✅ Modern OTT-Style UI

* Netflix-inspired dark theme
* Responsive movie cards
* Animated hover effects
* Cinematic background

---

## ✅ Optimized Architecture

* Dynamic recommendation generation
* Modular project structure
* Scalable production-ready approach

---

# 🛠️ Tech Stack

## Frontend

* Streamlit
* Custom CSS

## Backend / ML

* Python
* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity

## APIs

* TMDB API

## Libraries Used

* pandas
* numpy
* requests
* pickle
* joblib
* streamlit
* streamlit-option-menu
* python-dotenv

---

# 📂 Project Structure

```bash
CineScout/
│
├── App.py
│
├── pages/
│   └── trending.py
│
├── vectors.pkl
├── movies_list.pkl
├── vectorizer.pkl
│
├── bg.png
│
├── .env
├── requirements.txt
└── README.md
```

---

# 🧠 Recommendation System Architecture

## Optimized Approach ✅

### Step 1

TF-IDF converts movie tags into vectors.

### Step 2

User selects a movie.

### Step 3

Cosine similarity is dynamically computed:

```python
cosine_similarity(movie_vector, vectors)
```

### Step 4

Top similar movies are returned instantly.

---

# 📊 Machine Learning Workflow

## Dataset Processing

* Clean movie metadata
* Combine important textual features
* Generate tags

---

## Feature Engineering

Used:

* Genres
* Overview
* Cast
* Director
* Original language

---

## Vectorization

Implemented:

```python
TfidfVectorizer
```

Benefits:

* Memory efficient
* Better semantic importance
* Production-level optimization

---

# 🔥 Trending Movies System

The Trending section uses:

```bash
TMDB Trending Movies API
```

Endpoint:

```bash
https://api.themoviedb.org/3/trending/movie/week
```

Features:

* Live trending movies
* Real-time updates
* Dynamic posters
* Ratings & release dates

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/CineScout.git
```

---

## 2️⃣ Navigate to Project

```bash
cd CineScout
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

### Activate Environment

```bash
.venv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Setup TMDB API Key

Create a `.env` file:

```env
TMDB_API_KEY=your_api_key_here
```

Get API key from:

https://developer.themoviedb.org/

---

# ▶️ Run the Application

```bash
python -m streamlit run App.py
```

---

# 📸 UI Preview

## Home Page

* Movie recommendation system
* Modern OTT interface
* AI recommendations

## Trending Page

* Real-time trending movies
* Dynamic TMDB integration

---

# 🧩 Future Improvements

* Watchlist Feature
* Semantic AI Search
* Movie Details Page
* Trailer Integration
* FastAPI Backend
* Docker Deployment

---

# 📈 Performance Optimizations

## ✅ Removed Huge Similarity Matrix

Saved large memory consumption.

## ✅ Dynamic Similarity Computation

Only computes similarity when needed.

## ✅ TF-IDF Sparse Vectors

Improved scalability and performance.

---

# 💡 Learning Outcomes

This project helped in understanding:

* Recommendation Systems
* NLP Vectorization
* Cosine Similarity
* Streamlit UI Development
* API Integration
* Modular Python Architecture
* Production Optimization

---

# 👨‍💻 Author

## Gaurav Sonawane

Software Engineer | AI/ML Enthusiast | Full Stack Developer

### Interests

* Artificial Intelligence
* Machine Learning
* Generative AI
* FastAPI
* Django
* Recommendation Systems

---

# 📜 License

This project is for educational and portfolio purposes.

---

⭐ If you liked this project, feel free to star the repository!
