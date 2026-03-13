import csv
import os 

class Archivos:
    def leer_csv(self, filename):
        ruta_base = os.path.dirname(__file__)
        ruta_completa = os.path.join(ruta_base, filename)
 
        with open(ruta_completa, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]


    def cambiar_csv(self, filename, fields, lista_dicts):
            with open(filename, mode='w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                writer.writerows(lista_dicts)

    def filtrar_por_clase(self, animales, id_clase):
        return [a for a in animales if str(a.id_clase) == str(id_clase)]

    def filtrar_por_caracteristica(self, animales, caracteristica):
        return [a for a in animales if a.caracteristica.get(caracteristica) == '1']