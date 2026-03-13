import itertools
import time
import re

def generar_diccionarios(longitudes):
    patrones = ['11', '12', '23', '35', '58']
    hex_chars = '0123456789ABCDEF'
    
    for L in longitudes:
        filename = f"diccionario_L{L}.txt"
        count = 0
        with open(filename, 'w') as f:
            # Generamos combinaciones. Nota: Para L=7 esto puede tardar un poco en generar.
            for p in itertools.product(hex_chars, repeat=L):
                clave = "".join(p)
                if any(patron in clave for patron in patrones):
                    f.write(clave + "\n")
                    count += 1
        print(f"Diccionario L={L} creado con {count} combinaciones.")

def ataque_diccionario(password_obj, diccionario_file):
    start_time = time.time()
    intentos = 0
    with open(diccionario_file, 'r') as f:
        for linea in f:
            intentos += 1
            if linea.strip() == password_obj:
                return intentos, time.time() - start_time
    return intentos, time.time() - start_time

def fuerza_bruta(password_obj):
    hex_chars = '0123456789ABCDEF'
    L = len(password_obj)
    start_time = time.time()
    intentos = 0
    for p in itertools.product(hex_chars, repeat=L):
        intentos += 1
        if "".join(p) == password_obj:
            return intentos, time.time() - start_time
    return intentos, time.time() - start_time

# Ejecución de la prueba
targets = ["B235A", "B235A0", "B235AB1"]
# Nota: La generación del dicc L=7 es pesada.