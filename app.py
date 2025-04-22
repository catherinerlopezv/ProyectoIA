from flask import Flask, render_template, jsonify, request
from run_all import ejecutar_preprocesamiento

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preprocesar', methods=['POST'])
def preprocesar():
    try:
        ejecutar_preprocesamiento()
        return jsonify({"mensaje": "✅ Preprocesamiento completado con éxito"})
    except Exception as e:
        return jsonify({"mensaje": f"❌ Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
