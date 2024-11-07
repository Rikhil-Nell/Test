import gradio as gr
import pandas as pd
from sentiment_analysis.vader_analyzer import analyze_sentiment_vader
from sentiment_analysis.transformers_analyzer import analyze_sentiment_transformers

def analyze_reviews(file, use_vader, use_transformers):
    # Read the uploaded file
    if file.name.endswith(".csv"):
        df = pd.read_csv(file)
    elif file.name.endswith(".xlsx"):
        df = pd.read_excel(file)
    else:
        return "Please upload a CSV or Excel file."

    # Check the number of entries and truncate if needed
    if len(df) > 1000:
        df = df.head(1000)
        error_message = "The file contains more than 1,000 entries. Only the first 1,000 reviews are processed."
    else:
        error_message = "No Errors Found"

    # Ensure the "review" column exists
    df.columns = df.columns.str.lower()
    if 'review' not in df.columns:
        return "Please make sure the file has a 'review' column with review text."

    # Apply selected sentiment analysis models
    if use_vader:
        vader_results = analyze_sentiment_vader(df["review"])
        df = pd.concat([df, vader_results], axis=1)

    if use_transformers:
        transformers_results = analyze_sentiment_transformers(df["review"])
        df = pd.concat([df, transformers_results], axis=1)

    # Save the result to a CSV file
    output_file = "sentiment_analysis_results.csv"
    df.to_csv(output_file, index=False)
    
    return output_file, error_message, df.head()  # Return the output file, error message, and preview

# Define Gradio interface
interface = gr.Interface(
    fn=analyze_reviews,
    inputs=[
        gr.File(label="Upload your review file (CSV or XLSX)"),
        gr.Radio(["Vader", "Transformers"], label="Select Sentiment Analysis Model"),
    ],
    outputs=[
        gr.File(label="Download CSV"),
        gr.Textbox(label="Error Message"),
        gr.Dataframe(label="Data Preview"),
    ],
    title="Bulk Sentiment Analysis for Reviews",
    description="Upload a file with a 'review' column to analyze sentiment using Vader and Transformers models."
)

# Launch the Gradio app
interface.launch(share=True)
