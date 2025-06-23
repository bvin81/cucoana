
import pandas as pd
from content_based import recommend_cb

def composite_score(row, w_ppi=0.4, w_hsi=0.3, w_esi=0.3):
    return w_ppi * row['PPI'] + w_hsi * row['HSI'] + w_esi * row['ESI']

recipes = pd.read_csv("processed_recipes.csv")
recipes['score'] = recipes.apply(composite_score, axis=1)

def recommend_hybrid(user_input, vectorizer, ingredients_matrix, top_n=5):
    from sklearn.metrics.pairwise import cosine_similarity
    input_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(input_vec, ingredients_matrix).flatten()
    recipes['similarity'] = similarity
    recipes['final_score'] = recipes['similarity'] * 0.5 + recipes['score'] * 0.5
    return recipes.sort_values('final_score', ascending=False).head(top_n)
