import pandas as pd
from transformers import pipeline, AutoTokenizer
import torch

# Load your Excel file
try:
    df = pd.read_excel("Dataset baby youtube.xlsx")
    print("Column names in the Excel file:", df.columns.tolist())
    print("DataFrame shape:", df.shape)
    print("First 5 rows:\n", df.head())
except FileNotFoundError:
    print("Error: Input file not found. Please check the file path.")
    exit(1)
except Exception as e:
    print(f"Error loading Excel file: {str(e)}")
    exit(1)

# Verify 'text' column exists
if 'text' not in df.columns:
    print("Error: 'text' column not found. Available columns:", df.columns.tolist())
    exit(1)

# Drop empty or whitespace-only comments
df['text'] = df['text'].astype(str).str.strip()
df = df[df['text'] != ""].dropna(subset=['text'])
print("DataFrame shape after dropping empty comments:", df.shape)

# Load sentiment analysis pipeline and tokenizer
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline("sentiment-analysis", model=model_name, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)

# Define positivity scoring function with token-based truncation
def get_positivity_score(comment):
    try:
        # Tokenize and truncate to 512 tokens
        inputs = tokenizer(comment, truncation=True, max_length=512, return_tensors="pt")
        # Convert tokens back to text to pass to pipeline
        truncated_comment = tokenizer.decode(inputs['input_ids'][0], skip_special_tokens=True)
        result = classifier(truncated_comment)[0]
        if result['label'] == 'POSITIVE':
            return result['score']
        else:
            return 1 - result['score']
    except Exception as e:
        print(f"Error processing comment: {comment[:50]}... | Error: {str(e)}")
        return None

# Batch process comments for efficiency
batch_size = 16  # Adjust based on your system's memory
positivity_scores = []
for i in range(0, len(df), batch_size):
    batch_comments = df['text'].iloc[i:i+batch_size].tolist()
    # Tokenize and truncate comments
    inputs = tokenizer(batch_comments, truncation=True, max_length=512, padding=True, return_tensors="pt")
    # Decode back to text for pipeline
    batch_texts = [tokenizer.decode(input_ids, skip_special_tokens=True) for input_ids in inputs['input_ids']]
    results = classifier(batch_texts)
    batch_scores = [
        result['score'] if result['label'] == 'POSITIVE' else 1 - result['score']
        for result in results
    ]
    positivity_scores.extend(batch_scores)

# Add scores to DataFrame
df['positivity_score'] = positivity_scores

# Save result to new Excel file
try:
    df.to_excel("with_positivity_scores.xlsx", index=False)
    print("Output saved to 'with_positivity_scores.xlsx'")
except Exception as e:
    print(f"Error saving file: {str(e)}")