from catalogo import CatalogoPelicula
from pelicula import Pelicula


def mostrar_menu():
    print("\n===== MENÚ =====")
    print("1. Agregar Película")
    print("2. Listar Películas")
    print("3. Eliminar Catálogo")
    print("4. Cambiar de Catálogo")
    print("5. Listar Catálogos")
    print("6. Restaurar desde respaldo")
    print("0. Salir")


def main():
    nombre = input("Ingrese el nombre del catálogo: ")
    catalogo = CatalogoPelicula(nombre)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                nombre_p = input("Nombre: ")
                duracion = int(input("Duración (min): "))
                genero = input("Género: ")

                pelicula = Pelicula(nombre_p, duracion, genero)
                catalogo.agregar(pelicula)
                print("Película agregada correctamente.")

            elif opcion == "2":
                catalogo.listar()

            elif opcion == "3":
                seguro = input("¿Seguro? (s/n): ")
                if seguro.lower() == "s":
                    catalogo.crear_respaldo()
                    catalogo.eliminar_catalogo()
                    print("Catálogo eliminado con respaldo.")

            elif opcion == "4":
                nuevo = input("Nuevo catálogo: ")
                catalogo = CatalogoPelicula(nuevo)

            elif opcion == "5":
                CatalogoPelicula.listar_catalogos()

            elif opcion == "6":
                catalogo.restaurar_respaldo()
                print("Catálogo restaurado.")

            elif opcion == "0":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
