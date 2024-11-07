import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd

def analyze_sentiment_transformers(reviews):
    # Set device to "cpu" if CUDA (GPU) is unavailable
    # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Initialize tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
    model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased").to('cpu')

    results = []
    for review in reviews:
        # Tokenize with truncation and padding to max length
        tokenized_review = tokenizer(review, return_tensors="pt", truncation=True, padding="max_length", max_length=512)
        tokenized_review = {key: val.to('cpu') for key, val in tokenized_review.items()}  # Ensure tensors are on the correct device

        # Get the model's output (logits)
        with torch.no_grad():
            outputs = model(**tokenized_review)
        
        # Convert logits to probabilities
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
        
        # Get the predicted label and score
        score = probabilities.max().item()
        label = "POSITIVE" if torch.argmax(probabilities).item() == 1 else "NEGATIVE"
        
        # Append the result
        results.append({"label": label, "score": score})

    # Convert results to DataFrame
    sentiment_df = pd.DataFrame(results)
    return sentiment_df
