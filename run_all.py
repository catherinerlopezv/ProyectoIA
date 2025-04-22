import subprocess

def ejecutar_preprocesamiento():
    notebooks = [
        "01Limpieza.ipynb",
        "02Tokenizacion.ipynb",
        "03Lematizacion.ipynb",
        "04vectorizacion.ipynb"
    ]

    for nb in notebooks:
        print(f"Ejecutando {nb}...")
        subprocess.run([
            "jupyter", "nbconvert", "--to", "notebook",
            "--execute", "--inplace", nb
        ], check=True)
