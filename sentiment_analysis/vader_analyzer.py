import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon if not already available
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

def analyze_sentiment_vader(reviews):
    sia = SentimentIntensityAnalyzer()
    results = []
    for review in reviews:
        score = sia.polarity_scores(review)
        results.append(score)
    sentiment_df = pd.DataFrame(results)
    return sentiment_df
