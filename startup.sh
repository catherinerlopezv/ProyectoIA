#!/bin/bash

# Ir al directorio del script
cd "$(dirname "$0")"

# Ejecutar Flask API
echo "🚀 Iniciando Flask API en http://127.0.0.1:5000 ..."
nohup python3 app.py > flask.log 2>&1 &

# Esperar un momento para asegurar que Flask arranca
sleep 2

# Iniciar servidor web para frontend
echo "🌐 Iniciando servidor local en http://localhost:8000 ..."
nohup python3 -m http.server 8000 > frontend.log 2>&1 &

# Esperar brevemente y abrir index.html en navegador
sleep 2
open http://localhost:8000/index.html
