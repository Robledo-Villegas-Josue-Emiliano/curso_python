import csv

class Archivos:
    def leer_csv(self):
        with open(filename, 'w', encoding='utf-8') as f:
            reader = csv.DictReader(f)
        return [row for row in reader]

    def cambiar_csv(self):
        with open(filename, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(lista_dicts)

    def filtrar_por_clase(animales, id_clase):
        return [a for a in animales if a.clase_id == id_clase]

    def filtrar_por_caracteristica(animales, caracteristica):
        return [a for a in animales if a.atributos.get(caracteristica) == 1]