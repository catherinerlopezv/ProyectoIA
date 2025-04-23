from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd
from run_all import ejecutar_preprocesamiento

# 👇 Clase NaiveBayes copiada directamente aquí
class NaiveBayes:
    def fit(self, X, y):
        self.classes = np.unique(y)
        self.class_probs = {}
        self.word_probs = {}

        X = pd.DataFrame(X.toarray())  # Aseguramos formato
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

# 👇 Cargar modelo y vectorizador DESPUÉS de definir la clase
model = joblib.load('modelo_nb.pkl')
vectorizer = joblib.load('vectorizer.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/preprocesar', methods=['POST'])
def preprocesar():
    try:
        ejecutar_preprocesamiento()
        return jsonify({"mensaje": "✅ Preprocesamiento completado con éxito"})
    except Exception as e:
        return jsonify({"mensaje": f"❌ Error: {str(e)}"}), 500

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    texto = data.get('texto', '')

    if not texto:
        return jsonify({'error': 'No se proporcionó texto'}), 400

    vector = vectorizer.transform([texto])
    pred = model.predict(vector)

    return jsonify({'sentimiento': pred[0]})

if __name__ == '__main__':
    app.run(debug=True)
