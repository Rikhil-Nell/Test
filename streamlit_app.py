import streamlit as st
import pandas as pd
from sentiment_analysis.vader_analyzer import analyze_sentiment_vader
from sentiment_analysis.transformers_analyzer import analyze_sentiment_transformers

st.title("Bulk Sentiment Analysis for Reviews")

# Step 1: File Upload
uploaded_file = st.file_uploader("Upload your review file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read the file into a DataFrame
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Check the number of entries and truncate if needed
    if len(df) > 1000:
        df = df.head(1000)
        st.error("The file contains more than 1,000 entries. Only the first 1,000 reviews are processed.")

    st.write("Data Preview:", df.head())

    # Step 2: Model Selection
    st.write("Select sentiment analysis models:")
    use_vader = st.checkbox("Vader")
    use_transformers = st.checkbox("Transformers")

    # Ensure "review" column exists
    df.columns = df.columns.str.lower()
    if 'review' in df.columns:
        # Step 3: Process reviews with Selected Models
        if use_vader:
            vader_results = analyze_sentiment_vader(df["review"])
            df = pd.concat([df, vader_results], axis=1)
            st.write("Vader Analysis Results", df.head())

        if use_transformers:
            transformers_results = analyze_sentiment_transformers(df["review"])
            df = pd.concat([df, transformers_results], axis=1)
            st.write("Transformers Analysis Results", df.head())

        # Step 4: Download Results
        csv = df.to_csv(index=False)
        st.download_button("Download CSV", csv, "sentiment_analysis_results.csv", "text/csv")
    else:
        st.error("Please make sure the file has a 'review' column with review text.")
