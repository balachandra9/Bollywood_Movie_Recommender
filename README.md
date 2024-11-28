# Bollywood_Movie_Recommender
Recommends movies based on preferences

A simple movie recommendation system built using a Bollywood movie dataset. This project uses a content-based filtering approach to recommend similar movies based on user input. The system is implemented in Python with a Streamlit front-end for easy interaction.

# Features
User Input: Select a movie from a dropdown menu.
Recommendations: Provides top 3 similar movies based on content similarity.
Interactive UI: Built using Streamlit for seamless user experience.

# Dataset
Source: Kaggle - 10,000 Bollywood Dataset
Columns:
Unique_Id: Unique identifier for each movie.
imdb-id: IMDb identifier.
movie_name: Title of the movie.
year_of_release: Year the movie was released.
runtime: Runtime in minutes.
IMDB_rating: IMDb user rating.
no_of_votes: Number of votes on IMDb.
plot_description: Brief plot summary.
director: Director of the movie.
actors: Lead actors.
combined_features: Concatenation of plot, director, and actors for similarity computation.

# Architecture
Workflow:
1. Dataset Preparation:
Preprocessed to generate combined_features column.

2. Similarity Matrix:
Used Cosine Similarity to calculate the closeness between movies based on combined_features.

3. Recommendation Engine:
Retrieves the top 3 movies most similar to the selected movie.

4. Frontend:
Streamlit app to take input and display recommendations.

# Setup Instructions

1. Clone the Repository

git clone https://github.com/yourusername/Movie-Recommendation-System.git  
cd Movie-Recommendation-System  

2. Install Dependencies
Ensure you have Python installed. Then, run:
pip install -r app/requirements.txt  

3. Run the Application
streamlit run app/app.py

This will start the app in your browser.


# Folder Structure: 

Movie-Recommendation-System/  
├── data/  
│   ├── bollywood_dataset.csv                     # Raw movie dataset  
│   ├── preprocessed_data.csv                     # Preprocessed movie dataset
│   ├── movie_dict.pkl                            # Pickled dictionary of the dataset 
│   ├── movies.pkl           
│   ├── similarity.pkl                            # Pickled similarity matrix  
├── notebooks/
│   ├── Bollywood_Movie_Recommendation.ipynb      # Code for data cleaning and feature generation
├── app/  
│   ├── app.py                                    # Streamlit application code    
├── README.md                                     # Project description and instructions  


# Example Output
Input: "3 Idiots"
Recommendations:
Taare Zameen Par
PK
Munna Bhai M.B.B.S


Future Enhancements
Add collaborative filtering for better recommendations.
Incorporate user feedback to refine results.
Expand to include Hollywood or other regional cinema datasets.

# Credits
Dataset: Kaggle - Bollywood Movies Dataset
Libraries Used: Streamlit, Pandas, Scikit-learn

# License
This project is open-source and licensed under the MIT License.




