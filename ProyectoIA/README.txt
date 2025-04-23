
# ProyectoIA - Clasificador de Sentimientos con Naive Bayes

## 📁 Estructura

- app.py         → API Flask con endpoints `/metrics` y `/predict`
- index.html     → Frontend HTML para ingresar y clasificar tweets
- 03lemmatized.csv → Debes colocarlo en la misma carpeta que `app.py`

## ⚙️ Instalación

1. Asegúrate de tener Python 3.7+
2. Instala Flask y Flask-CORS:

    pip install flask flask-cors scikit-learn pandas

3. Coloca `03lemmatized.csv` junto a `app.py`

## ▶️ Ejecución

1. En terminal, entra a la carpeta del proyecto:

    cd ProyectoIA

2. Ejecuta la API Flask:

    python app.py

3. En otra terminal, lanza un servidor local para el frontend:

    python -m http.server 8080

4. Abre en tu navegador:

    http://localhost:8080/index.html

Y listo: podrás clasificar tweets y ver métricas del modelo.

