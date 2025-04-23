# naive_bayes.py

import numpy as np
import pandas as pd

class NaiveBayes:
    def fit(self, X, y):
        self.classes = np.unique(y)
        self.class_probs = {}
        self.word_probs = {}

        X = pd.DataFrame(X.toarray())  # Si usaste CountVectorizer
        for c in self.classes:
            X_c = X[np.array(y) == c]
            self.class_probs[c] = len(X_c) / len(X)
            total_wc = X_c.sum().sum()
            self.word_probs[c] = (X_c.sum() + 1) / (total_wc + X.shape[1])

    def predict(self, X):
        predictions = []
        X = pd.DataFrame(X.toarray())
        for i in range(X.shape[0]):
            row = X.iloc[i].values
            posteriors = {}
            for c in self.classes:
                log_prob = np.log(self.class_probs[c]) + np.sum(row * np.log(self.word_probs[c].values))
                posteriors[c] = log_prob
            predictions.append(max(posteriors, key=posteriors.get))
        return np.array(predictions)
