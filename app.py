
from flask import Flask, jsonify, request
import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

from flask_cors import CORS
app = Flask(__name__)
CORS(app)

class NaiveBayes:
    def fit(self, X, y):
        self.classes = np.unique(y)
        self.class_probs = {}
        self.word_probs = {}
        for c in self.classes:
            X_c = X[y == c]
            self.class_probs[c] = X_c.shape[0] / X.shape[0]
            total_wc = X_c.sum()
            self.word_probs[c] = (X_c.sum(axis=0) + 1) / (total_wc + X.shape[1])

    def predict(self, X):
        predictions = []
        for i in range(X.shape[0]):
            posteriors = {}
            row = X[i].toarray()[0]
            for c in self.classes:
                log_prob = np.log(self.class_probs[c]) + np.sum(row * np.log(self.word_probs[c].A1))
                posteriors[c] = log_prob
            predictions.append(max(posteriors, key=posteriors.get))
        return np.array(predictions)

# Entrenamiento al inicio para mantener vectorizador y modelo en memoria
df = pd.read_csv("03lemmatized.csv")
df = df.dropna(subset=["text_lema", "sentiment"])
df = df[df["text_lema"].str.strip() != ""]

vectorizer = CountVectorizer(stop_words='english', min_df=5, max_df=0.8, max_features=3000)
X = vectorizer.fit_transform(df["text_lema"])
y = df["sentiment"].astype(str)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

model = NaiveBayes()
model.fit(X_train, y_train)

@app.route('/metrics', methods=['GET'])
def metrics():
    y_pred = model.predict(X_test)
    accuracy = (y_pred == y_test.values).mean()
    report = classification_report(y_test, y_pred, output_dict=True)
    conf_matrix = confusion_matrix(y_test, y_pred).tolist()

    return jsonify({
        "accuracy": round(accuracy, 4),
        "classification_report": report,
        "confusion_matrix": conf_matrix
    })

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    tweet = data.get("text", "")

    # Preprocesamiento básico como en entrenamiento
    tweet = tweet.lower()
    tweet = re.sub(r"http\S+|www\S+", "", tweet)
    tweet = re.sub(r"@\w+|#\w+", "", tweet)
    tweet = re.sub(r"[^a-z\s]", "", tweet)
    tweet = re.sub(r"\s+", " ", tweet).strip()

    tweet_vec = vectorizer.transform([tweet])
    prediccion = model.predict(tweet_vec)[0]

    return jsonify({"prediccion": prediccion})

if __name__ == '__main__':
    app.run(debug=True)
