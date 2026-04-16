import re

from flask import Flask, render_template, request
from frases_celebres import Frase, carga_archivo_csv, crea_diccionario_titulos, buscar_palabras, buscar_palabras_ratio

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
        peliculas_list = diccionario_titulos.get(pelicula, [])
        return render_template("pelicula.html", peliculas_list=peliculas_list)
    else:
        return render_template("pelicula.html", peliculas_list=peliculas_list)

@app.route('/frases', methods =['GET','POST'])
def frase():
    if request.method == 'POST':
        frase_a_buscar = request.form['frase']
        frases_list = buscar_palabras_ratio(frases, frase_a_buscar, umbral=0.50)
        return render_template("frases.html", frases=frases_list)
    else:
        return render_template("frases.html", frases=frases)

if __name__ == "__main__":
    app.run(debug=True) 