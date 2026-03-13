from Archivos import Archivos
from Animal import Animal

def menu_principal():
    manejador = Archivos()
    
    datos_clases = manejador.leer_csv('clases.csv')
    datos_zoo = manejador.leer_csv('zoo.csv')
    
    lista_animales = []
    for reg in datos_zoo:
        obj = Animal(reg['nombre_animal'], reg['clase'], reg)
        lista_animales.append(obj)

    while True:
        print("\n Menu principal")
        print("1. Animal por Clasificación")
        print("2. Animal por Característica")
        print("3. Agregar nuevo animal")
        print("4. Salir y Guardar")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nClases disponibles:")
            for c in datos_clases:
                print(f"{c['Clase_id']}: {c['Clase_tipo']}")
            
            id_buscado = input("Ingrese el ID de la clase: ")
            resultados = manejador.filtrar_por_clase(lista_animales, id_buscado)
            for res in resultados:
                print(res) 

        elif opcion == "2":
            carac = input("Ingrese característica (pelo, plumas, huevos, etc.): ").lower()
            resultados = manejador.filtrar_por_caracteristica(lista_animales, carac)
            for res in resultados:
                print(res)

        elif opcion == "3":
            nombre = input("Nombre del animal: ")
            print("IDs de clase: 1:Mamífero, 2:Ave, 3:Reptil, 4:Pez, 5:Anfibio, 6:Insecto, 7:Invertebrado")
            id_c = input("ID de clase: ")
            
            nueva_data = {k: '0' for k in datos_zoo[0].keys()}
            nueva_data['nombre_animal'] = nombre
            nueva_data['clase'] = id_c
            
            if input("¿Tiene plumas? (s/n): ").lower() == 's':
                nueva_data['plumas'] = '1'
            
            nuevo_animal = Animal(nombre, id_c, nueva_data)
            lista_animales.append(nuevo_animal)
            print("¡Animal agregado con éxito!")

        elif opcion == "4":
            campos = list(datos_zoo[0].keys())
            lista_para_guardar = [a.caracteristica for a in lista_animales]
            manejador.cambiar_csv('zoo.csv', campos, lista_para_guardar)
            print("Cambios guardados. Saliendo...")
            break

if __name__ == "__main__":
    menu_principal()