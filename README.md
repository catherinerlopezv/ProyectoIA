# Proyecto: Clasificador de Sentimientos Tweets usando Naïve Bayes

Este proyecto implementa un clasificador de sentimientos de tweets utilizando el algoritmo de Naïve Bayes desde cero, sin bibliotecas externas para el modelo.

## Requisitos

- Python 3.8 o superior
- Navegador web moderno (Chrome, Firefox, Safari, etc.)

## Estructura del Proyecto

- `app.py` — Backend en Python que implementa el modelo Naïve Bayes y el servidor Flask.
- `index.html` — Interfaz web para la clasificación de tweets.
- `startup.sh` — Script para iniciar automáticamente el backend y frontend.
- `modelo/` — (opcional) Carpeta donde se guarda el modelo entrenado o datos procesados.
- `Dataset` - Dataset Entrenado 03Lematized.csv

## Instalación

1. Clona este repositorio:
   ```bash
   git clone <URL-del-repositorio>
   cd <nombre-del-proyecto>
   
# ProyectoIA

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

## Resumen del Proyecto
| Archivo | Librerías principales | Propósito principal |
|---------|-----------------------|---------------------|
| 01 Limpieza |	pandas, re, nltk (stopwords, tokenización) |	Limpiar y preparar el texto |
|---------|-----------------------|---------------------|
| 02 Tokenización |	pandas, nltk (TweetTokenizer) |	Separar tweets en palabras respetando símbolos |
|---------|-----------------------|---------------------|
| 03 Lematización |	pandas, nltk (WordNet, pos_tag) |	Llevar palabras a su forma base según su tipo gramatical |
|---------|-----------------------|---------------------|
| 04 Vectorización |	pandas, sklearn (CountVectorizer) |	Transformar el texto en vectores numéricos |

## Procesamiento de Texto

1. Carga de Datos
   ↓
2. Limpieza de Texto
   - Eliminación de símbolos, números, URLs
   - Conversión a minúsculas
   - Eliminación de stopwords
   ↓
3. Tokenización
   - Uso de TweetTokenizer (manejo de hashtags, menciones, emoticonos)
   ↓
4. Lematización
   - Reducción de palabras a su forma base
   - Ajuste según su categoría gramatical
   ↓
5. Vectorización (Bag of Words)
   - Representación numérica de textos
   - Configuración de vocabulario (min_df, max_df, max_features)
   ↓
6. Dataset Final
   - Tweets vectorizados + etiquetas de sentimiento

## Flujo

   ![Flujo del proyecto](https://github.com/catherinerlopezv/ProyectoIA/raw/main/Flujo.png)

