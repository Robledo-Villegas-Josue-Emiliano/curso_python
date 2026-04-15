import re

from flask import Flask, render_template, request
from frases_celebres import Frase, carga_archivo_csv, crea_diccionario_titulos, buscar_palabras

app = Flask(__name__)

frases = carga_archivo_csv("C:\\Users\\emili\\OneDrive\\Desktop\\Curso_python ( no borrar )\\curso_python\\Frases_Celebres\\frases_consolidadas.csv")
diccionario_titulos = crea_diccionario_titulos(frases)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/pelicula', methods=['GET','POST'])
def pelicula():
    if request.method == 'POST':
        pelicula = request.form['pelicula']
        resultados = diccionario_titulos.get(pelicula, [])
        return render_template("pelicula.html", resultados=resultados, pelicula=pelicula)
    else:
        return render_template("pelicula.html", resultados=resultados, pelicula=pelicula)

@app.route('/frase', methods =['GET','POST'])
def frase():
    if request.method == 'POST':
        frase_a_buscar = request.form['frase']
        resultados = buscar_palabras(frases, frase_a_buscar)
        return render_template("frase.html", resultados=resultados, frase_a_buscar=frase_a_buscar)
    else:
        return render_template("frase.html", resultados=resultados, frase_a_buscar=frase_a_buscar)
    
if __name__ == "__main__":
    app.run(debug=True) 