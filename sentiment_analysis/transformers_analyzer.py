from transformers import AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd
import torch
def analyze_sentiment_transformers(reviews):

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
    model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased").to(device)

    results = []
    for review in reviews:
        # Tokenize with truncation and padding to max length
        tokenized_review = tokenizer(review, return_tensors="pt", truncation=True, padding="max_length", max_length=512).to(device)

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

        sentiment_df = pd.DataFrame(results)

    return sentiment_df