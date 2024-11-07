import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiment_vader(reviews):
    """
    Analyzes sentiment using Vader for a list of reviews.
    
    Parameters:
        reviews (pd.Series or list of str): List or Series containing review texts.
        
    Returns:
        pd.DataFrame: A DataFrame with Vader sentiment scores for each review.
    """
    # Initialize the SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()
    
    # Analyze sentiment for each review
    results = []
    for review in reviews:
        score = sia.polarity_scores(review)
        results.append(score)
    
    # Convert results to DataFrame
    sentiment_df = pd.DataFrame(results)
    
    return sentiment_df
