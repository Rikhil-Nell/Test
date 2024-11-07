---
title: BulkSentimentAnalysis
app_file: app.py
sdk: gradio
sdk_version: 5.5.0
---
# Bulk Sentiment Analysis for Reviews

This project provides a tool for bulk sentiment analysis of store reviews. Using various sentiment analysis models, including VADER and Hugging Face's Transformers, users can analyze reviews in CSV or Excel format to understand the overall sentiment. Results can be downloaded in CSV format, making it easy to leverage insights for decision-making.

## Features

- **Bulk Upload:** Upload CSV or Excel files of reviews for analysis.
- **Model Options:** Choose from multiple sentiment analysis models:
  - **VADER** for rule-based sentiment analysis.
  - **SpaCy (Static Embeddings)** and **SpaCy (Contextual Embeddings)** for improved flexibility (coming soon).
  - **Transformers** for deep learning-based sentiment analysis using pretrained models from Hugging Face.
- **Download Results:** Export analyzed reviews with sentiment scores and labels as a CSV.

## Installation

To get started, clone this repository and install the dependencies.

```bash
git clone https://github.com/yourusername/bulk-sentiment-analysis
cd bulk-sentiment-analysis
pip install -r requirements.txt
```

Ensure your environment supports GPU processing, especially for Transformer-based models, to handle large datasets more efficiently.

### Dependencies

- Python 3.7+
- [Streamlit](https://streamlit.io/) for building the user interface
- [Pandas](https://pandas.pydata.org/) for data handling
- [NLTK](https://www.nltk.org/) and [VADER](https://github.com/cjhutto/vaderSentiment) for sentiment analysis
- [SpaCy](https://spacy.io/) (optional, for static and contextual embedding-based analysis)
- [Transformers](https://huggingface.co/transformers/) by Hugging Face for deep learning sentiment models

To install these, you can run:
```bash
pip install streamlit pandas nltk torch transformers spacy
```

For GPU support, install the appropriate CUDA version of PyTorch, following instructions from the [official PyTorch website](https://pytorch.org/get-started/locally/).

## Usage

1. **Run the Application**

   Launch the Streamlit app with:
   ```bash
   streamlit run app.py
   ```

2. **Upload Your File**

   Upload a CSV or Excel file containing reviews. Make sure there is a column labeled `Review` with the text you want to analyze.

3. **Choose a Model**

   Select one or more sentiment analysis models:
   - **VADER** for quick, rule-based analysis.
   - **Transformers** for more accurate, context-based sentiment detection.

4. **Analyze and Download Results**

   After processing, the app will display results in the UI. You can download the full results as a CSV file.

### Example of CSV Output

The output CSV will contain the original reviews alongside new columns with sentiment scores and labels, depending on the models chosen.

## Folder Structure

- **`app.py`**: Main Streamlit application script.
- **`sentiment_analysis/`**: Contains modular functions for each sentiment analysis model (e.g., `vader_analyzer.py`, `spacy_static.py`, etc.).
- **`requirements.txt`**: List of required dependencies.

## Future Enhancements

- **Integrate SpaCy models** for static and contextual embedding-based sentiment analysis.
- **Improved preprocessing** to handle non-English text and non-standard review formats.
- **Performance optimization** with caching and batch processing for large datasets.

## Contributing

Feel free to open issues or submit pull requests for improvements. All contributions are welcome!

---

This README should give users a clear understanding of what the project does, how to set it up, and how to use it. Let me know if you'd like any more specific instructions or additional sections!