
from hybrid_model import recommend_hybrid

if __name__ == "__main__":
    query = input("Introduceți ingredientele preferate: ")
    results = recommend_hybrid(query)
    for index, row in results.iterrows():
        print(f"\nRețetă: {row['title']}\nScor final: {row['final_score']:.2f}")
