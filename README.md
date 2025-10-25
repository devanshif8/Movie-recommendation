# 🎬 Movie Recommendation System

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![TMDB](https://img.shields.io/badge/TMDB-API-green.svg)](https://www.themoviedb.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An intelligent movie recommendation system built with Python and Streamlit that suggests movies based on user preferences using content-based filtering and the TMDB API.

## 🚀 Features

- Content-based movie recommendations
- Real-time movie poster fetching from TMDB
- Interactive web interface using Streamlit
- Movie similarity scoring based on cast, crew, genres, and keywords
- Support for 5000+ movies from TMDB dataset

## 🛠️ Technologies Used

- **Python** - Primary programming language
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **Scikit-learn** - Machine learning operations
- **TMDB API** - Movie data and poster fetching
- **Python-dotenv** - Environment variable management

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/devanshif8/Movie-recommendation.git
cd Movie-recommendation
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your TMDB API key:
     ```
     TMDB_API_KEY=your_api_key_here
     ```

## 🚀 Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`
3. Select a movie from the dropdown menu
4. Click "Show Recommendation" to get similar movie suggestions

## 📊 Data Sources

The system uses two primary datasets from TMDB:
- `tmdb_5000_movies.csv` - Contains movie metadata including genres, keywords, and overview
- `tmdb_5000_credits.csv` - Contains cast and crew information

## 🔍 How It Works

1. **Data Preprocessing**
   - Merges movies and credits datasets
   - Extracts relevant features (cast, crew, genres, keywords)
   - Processes text data for similarity calculation

2. **Similarity Calculation**
   - Uses CountVectorizer for text feature extraction
   - Implements cosine similarity for movie comparison
   - Generates similarity scores between movies

3. **Recommendation Engine**
   - Takes user input for movie selection
   - Finds movies with highest similarity scores
   - Fetches movie posters using TMDB API
   - Presents top recommendations

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (\`git checkout -b feature/AmazingFeature\`)
3. Commit your changes (\`git commit -m 'Add some AmazingFeature'\`)
4. Push to the branch (\`git push origin feature/AmazingFeature\`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [TMDB](https://www.themoviedb.org/) for providing the movie database and API
- [Streamlit](https://streamlit.io/) for the amazing web framework
- The open-source community for various tools and libraries

## 📞 Contact

Devanshi Faldu - [@devanshif8](https://github.com/devanshif8)

Project Link: [https://github.com/devanshif8/Movie-recommendation](https://github.com/devanshif8/Movie-recommendation)

---
Keywords: movie recommendation system, python, streamlit, tmdb api, content-based filtering, machine learning, data science, movie suggestions, recommendation engine
