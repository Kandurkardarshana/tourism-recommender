# recommender.py

import pandas as pd

# --- 1. SIMULATED DATASET ---
tourist_data = [
    {"name": "Taj Mahal", "region": "North", "budget": "Medium", "interest": "History", "score": 4.9},
    {"name": "Varanasi Ghats", "region": "North", "budget": "Low", "interest": "Culture", "score": 4.5},
    {"name": "Kerala Backwaters", "region": "South", "budget": "High", "interest": "Nature", "score": 4.7},
    {"name": "Hampi Ruins", "region": "South", "budget": "Low", "interest": "History", "score": 4.6},
    {"name": "Goa Beaches", "region": "West", "budget": "Medium", "interest": "Adventure", "score": 4.2},
    {"name": "Ranthambore Safari", "region": "West", "budget": "High", "interest": "Nature", "score": 4.8},
    {"name": "Sikkim Mountains", "region": "East", "budget": "Medium", "interest": "Nature", "score": 4.7},
    {"name": "Kolkata Art District", "region": "East", "budget": "Low", "interest": "Culture", "score": 4.0},
]

df = pd.DataFrame(tourist_data)

# --- 2. RECOMMENDATION FUNCTION ---
def get_recommendations(region, budget, interest, top_n=5):

    region = region.lower()
    budget = budget.lower()
    interest = interest.lower()

    filtered_df = df[
        (df['region'].str.lower() == region) &
        (df['budget'].str.lower() == budget) &
        (df['interest'].str.lower() == interest)
    ]

    if len(filtered_df) < 2 and len(filtered_df) < len(df):
        filtered_df = df[
            (df['region'].str.lower() == region) &
            (df['interest'].str.lower() == interest)
        ]

    recommended_df = filtered_df.sort_values(by='score', ascending=False)
    top_recommendations = recommended_df.head(top_n)

    return top_recommendations.to_dict('records')


if __name__ == '__main__':
    recs = get_recommendations(region="South", budget="Low", interest="History")
    print(recs)
