from transformers import pipeline
import pandas as pd

def analyze_sentiment_transformers(reviews):
    sentiment_analyzer = pipeline("sentiment-analysis")
    results = []
    for review in reviews:
        score = sentiment_analyzer(review)
        results.append(score)

    sentiment_df = pd.DataFrame(results)
    return sentiment_df