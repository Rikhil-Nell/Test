import streamlit as st
import pandas as pd
from sentiment_analysis.nltk_analyzer import analyze_sentiment_nltk
from sentiment_analysis.vader_analyzer import analyze_sentiment_vader
from sentiment_analysis.transformers_analyzer import analyze_sentiment_transformers

st.title("Bulk Sentiment Analysis for Store Reviews")

# Step 1: File Upload
uploaded_file = st.file_uploader("Upload your review file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read the file into a DataFrame
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("Data Preview:", df.head())

    # Step 2: Model Selection
    st.write("Select sentiment analysis models:")
    use_nltk = st.checkbox("NLTK")
    use_vader = st.checkbox("Vader")
    use_transformers = st.checkbox("Transformers")

    # Ensure "Review" column exists
    if 'Review' in df.columns:
        # Step 3: Process Reviews with Selected Models
        if use_nltk:
            df["NLTK Sentiment"] = df["Review"].apply(analyze_sentiment_nltk)
        if use_vader:
            df["Vader Sentiment"] = df["Review"].apply(analyze_sentiment_vader)
        if use_transformers:
            df["Transformers Sentiment"] = df["Review"].apply(analyze_sentiment_transformers)

        # Step 4: Display and Download Results
        st.write("Analysis Results", df)
        csv = df.to_csv(index=False)
        st.download_button("Download CSV", csv, "sentiment_analysis_results.csv", "text/csv")
    else:
        st.error("Please make sure the file has a 'Review' column with review text.")
