# IMPORTACIONES

import os
import shutil
from peliculas import Pelicula

# CLASE CATALOGO
class CatalogoPelicula:
    """
    Gestiona un catálogo de películas.

    Conceptos POO:
    - Composición (lista de objetos Pelicula)
    - Responsabilidad única
    - Abstracción
    """

    def __init__(self, nombre: str):
        if not nombre.strip():
            raise ValueError("El nombre del catálogo no puede estar vacío.")

        self.nombre = nombre.strip()
        self.ruta_archivo = f"{self.nombre}.txt"

        # Crear archivo si no existe
        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, "w", encoding="utf-8"):
                pass

  
    # MÉTODO PRIVADO DE LECTURA
    def _leer_peliculas(self):
        """Lee todas las películas del archivo."""
        peliculas = []
        with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    peliculas.append(linea)
        return peliculas

  
    # AGREGAR PELÍCULA
    def agregar(self, pelicula: Pelicula):
        peliculas = self._leer_peliculas()

        # Evitar duplicados
        if any(pelicula.nombre in p for p in peliculas):
            raise ValueError("La película ya existe en el catálogo.")

        with open(self.ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(str(pelicula) + "\n")

  
    # LISTAR PELÍCULAS
        peliculas = self._leer_peliculas()

        if not peliculas:
            print("El catálogo está vacío.")
            return

        print(f"\nCatálogo: {self.nombre}")
        for i, pelicula in enumerate(peliculas, 1):
            print(f"{i}. {pelicula}")

   
    # ELIMINAR CATÁLOGO
        def eliminar_catalogo(self):
         if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
         else:
            raise FileNotFoundError("El catálogo no existe.")

   
    # RESPALDO
    def crear_respaldo(self):
        respaldo = f"{self.nombre}_respaldo.txt"
        shutil.copy(self.ruta_archivo, respaldo)

   
    # RESTAURAR
    def restaurar_respaldo(self):
        respaldo = f"{self.nombre}_respaldo.txt"
        if os.path.exists(respaldo):
            shutil.copy(respaldo, self.ruta_archivo)
        else:
            raise FileNotFoundError("No existe respaldo para este catálogo.")

    
    # LISTAR TODOS LOS CATÁLOGOS
    @staticmethod
    def listar_catalogos():
        print("\nCatálogos disponibles:")
        for archivo in os.listdir():
            if archivo.endswith(".txt") and not archivo.endswith("_respaldo.txt"):
                print("-", archivo[:-4])
