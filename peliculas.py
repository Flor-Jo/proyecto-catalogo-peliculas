# CLASE PELICULA
class Pelicula:
    """
    Representa una película individual.
    
    Conceptos POO aplicados:
    - Encapsulamiento (atributo privado __duracion)
    - Abstracción (modela una entidad real)
    - Polimorfismo (__str__)
    """

    def __init__(self, nombre: str, duracion: int, genero: str):
        # Validación de nombre
        if not nombre.strip():
            raise ValueError("El nombre de la película no puede estar vacío.")

        # Validación de duración
        if not isinstance(duracion, int) or duracion <= 0:
            raise ValueError("La duración debe ser un número entero positivo.")

        # Validación de género
        if not genero.strip():
            raise ValueError("El género no puede estar vacío.")

        self.nombre = nombre.strip()
        self.__duracion = duracion      # Atributo privado (encapsulamiento)
        self.genero = genero.strip()

    @property
    def duracion(self):
        """Getter del atributo privado duración."""
        return self.__duracion

    def __str__(self):
        """
        Método mágico que devuelve representación en texto.
        Se usa automáticamente al hacer print(objeto).
        """
        return f"{self.nombre} - {self.__duracion} min - {self.genero}"
