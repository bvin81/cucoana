
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

recipes = pd.read_csv("processed_recipes.csv")
vectorizer = CountVectorizer()
ingredients_matrix = vectorizer.fit_transform(recipes['ingredients'])

def recommend_cb(user_input, top_n=5):
    input_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(input_vec, ingredients_matrix)
    top_indices = similarity.argsort()[0][-top_n:][::-1]
    return recipes.iloc[top_indices]
