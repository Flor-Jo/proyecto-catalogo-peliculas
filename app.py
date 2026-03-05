from catalogo import CatalogoPelicula
from peliculas import Pelicula

#FUNCION QUE MUESTRA EL MENU DEL SISTEMA
def mostrar_menu():
    print("\n===== MENÚ =====") #\n imprime un salto de linea
    print("1. Agregar Película")
    print("2. Listar Películas")
    print("3. Eliminar Catálogo")
    print("4. Cambiar de Catálogo")
    print("5. Listar Catálogos")
    print("6. Restaurar desde respaldo")
    print("0. Salir")

#FUNCION PRINCIPAL DEL PROGRAMA
def main():
    nombre = input("Ingrese el nombre del catálogo: ")
    
    #Crea un objeto de la clase CatalogoPelicula
    #Esto tamb crea el archivo "txt." si no existe
    catalogo = CatalogoPelicula(nombre)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        #Bloque tyr para capturar errores y evitar que el programa se rompa
        try:
            
            #OPCION 1: AGREGAR PELICULA
            if opcion == "1":
                nombre_p = input("Nombre: ")
                duracion = int(input("Duración (min): ")) #convierte el input a entero
                genero = input("Género: ")

                #Crea un objeto de la clase Pelicula
                pelicula = Pelicula(nombre_p, duracion, genero)
                catalogo.agregar(pelicula)
                print("Película agregada correctamente.")

            #OPCION 2: LISTAR PELICULAS
            elif opcion == "2":
                catalogo.listar() #imprime todas las peliculas guardadas

            #OPCION 3: ELIMINAR CATALOGO
            elif opcion == "3":
                seguro = input("¿Seguro? (s/n): ")
                if seguro.lower() == "s":  #convierte en minusculas para que no haya errores
                    catalogo.crear_respaldo()
                    catalogo.eliminar_catalogo()
                    print("Catálogo eliminado con respaldo.")

            #OPCION 4: CAMBIAR DE CATALOGO
            elif opcion == "4":
                nuevo = input("Nuevo catálogo: ")
                catalogo = CatalogoPelicula(nuevo) #crea un nuevo objeto en CatalogoPelicula

            #OPCION 5: LISTAR CATALOGOS
            elif opcion == "5":
                CatalogoPelicula.listar_catalogos() #muestra todos los archivos catalogo disponible

            #OPCION 6: RESTAURAR RESPALDO
            elif opcion == "6":
                catalogo.restaurar_respaldo()
                print("Catálogo restaurado.")

            #OPCION 0: SALIR DEL PROGRWAMA
            elif opcion == "0":
                print("Saliendo del sistema...")
                break #Rompe el bucle while y termina el programa

            else:
                print("Opción inválida.") #Si la opcion no existe

        except Exception as e:
            print(f"Error: {e}") #por si hay errores


if __name__ == "__main__":
    main()           #vuelve al programa de 0
