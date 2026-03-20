import pandas as pd
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# ---------------- CLEAN TEXT ----------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z ]', '', text)
    return text


# ---------------- TRAIN MODEL ----------------
def train_nlp_model():

    df = pd.read_csv("nlp_dataset.csv")

    df["description"] = df["description"].apply(clean_text)

    X_text = df["description"]
    y = df["category"]

    vectorizer = TfidfVectorizer(max_features=3000, ngram_range=(1,2))
    X = vectorizer.fit_transform(X_text)

    model = LogisticRegression(max_iter=200)
    model.fit(X, y)

    # Save model
    pickle.dump(model, open("category_model.pkl", "wb"))
    pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

    print("✅ NLP Model Trained & Saved")


# ---------------- LOAD MODEL ----------------
def load_nlp_model():
    model = pickle.load(open("category_model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    return model, vectorizer


# ---------------- PREDICT ----------------
def predict_category(text):

    model, vectorizer = load_nlp_model()

    text = clean_text(text)

    text_vec = vectorizer.transform([text])

    return model.predict(text_vec)[0]