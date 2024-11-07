Here's a revised README for your project, updated for Gradio:

---

# Bulk Sentiment Analysis for Reviews

This project allows users to perform bulk sentiment analysis on customer reviews using two NLP models: **VADER** and **Transformers** (DistilBERT). Users can upload a CSV or Excel file with reviews and analyze the sentiment of each review in bulk. The application is built using Gradio for an interactive web interface.

## Features

1. **File Upload**: Upload a `.csv` or `.xlsx` file containing customer reviews. The app reads this file and prepares it for analysis. Only the first 1,000 reviews are processed to manage performance.
2. **Sentiment Analysis Models**:
   - **VADER**: A rule-based model particularly effective for social media text.
   - **Transformers (DistilBERT)**: A deep learning model that provides a robust analysis.
3. **Download Results**: After analysis, download the results as a CSV file with sentiment labels and scores.

## Getting Started

### Prerequisites

Make sure to have Python installed, then install the required packages using:

```bash
pip install -r requirements.txt
```

### Running the Application

To start the Gradio interface, run:

```bash
python app.py
```

Once the app is running, a local link will be displayed in the terminal. Open the link in your browser to interact with the application.

### Usage

1. **Upload a File**: Click "Upload your review file" and select a `.csv` or `.xlsx` file. Ensure the file has a column named `review` containing the text for sentiment analysis.
2. **Select Model**: Use the radio buttons to choose either "VADER" or "Transformers" for sentiment analysis.
3. **Analyze Sentiment**: After selecting a model, click "Run" to start the analysis. The results will display below.
4. **Download Results**: Click "Download CSV" to save the output.

## File Structure

- `app.py`: Main file containing the Gradio application setup.
- `sentiment_analysis/vader_analyzer.py`: VADER sentiment analysis implementation.
- `sentiment_analysis/transformers_analyzer.py`: Transformers (DistilBERT) sentiment analysis implementation.

## Future Enhancements

- **Integrate SpaCy models** for static and contextual embedding-based sentiment analysis.
- **Improved preprocessing** to handle non-English text and non-standard review formats.
- **Performance optimization** with caching and batch processing for large datasets.

## Contributing

Feel free to open issues or submit pull requests for improvements. All contributions are welcome!

---
