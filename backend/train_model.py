# backend/train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import pickle
import os

# ✅ Load dataset from URL (automatic download)
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df = pd.read_csv(url, sep='\t', header=None, names=['label', 'text'])

print(f"Loaded dataset with {len(df)} messages")

# Split
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], random_state=42, test_size=0.2)

# Use TF-IDF instead of CountVectorizer (more accurate)
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

# Evaluate accuracy
accuracy = model.score(X_test, y_test)
print(f"✅ Model trained with accuracy: {accuracy:.2%}")

# Save model
os.makedirs("backend", exist_ok=True)
with open("backend/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("🎉 Saved improved model as backend/model.pkl")
