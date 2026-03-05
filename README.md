#  Catálogo de Películas en Python

Aplicación de consola desarrollada en **Python** para gestionar catálogos de películas utilizando **Programación Orientada a Objetos (POO)** y manejo de archivos.

 **Proyecto Final Integrador** del curso **"Introducción a Python"** de la institución **ADA ITW**.

---

#  Descripción del proyecto

El objetivo del proyecto es desarrollar un programa que permita **llevar un registro de películas** aplicando conceptos de **programación orientada a objetos**.

El sistema permite crear un catálogo de películas almacenado en un **archivo `.txt`**, donde posteriormente se pueden agregar, listar o eliminar películas.

Cuando el programa se ejecuta:

* Se solicita ingresar el **nombre del catálogo**
* Si el catálogo **no existe**, se crea automáticamente
* Si el catálogo **ya existe**, se continúa trabajando sobre ese archivo

---

#  Funcionalidades del sistema

El menú del programa permite realizar las siguientes operaciones:

1️⃣ Agregar película
2️⃣ Listar películas del catálogo
3️⃣ Eliminar catálogo de películas
4️⃣ Cambiar de catálogo
5️⃣ Listar catálogos disponibles
6️⃣ Restaurar catálogo desde respaldo
0️⃣ Salir del sistema

---

#  Conceptos de Python aplicados

En este proyecto se aplican conceptos fundamentales de programación:

* Programación Orientada a Objetos (POO)
* Encapsulamiento
* Abstracción
* Polimorfismo
* Manejo de archivos
* Manejo de excepciones
* Modularización del código

---

#  Estructura del proyecto

```
catalogo-peliculas/

│
├── pelicula.py      # Clase Pelicula
├── catalogo.py      # Clase CatalogoPelicula
├── app.py           # Programa principal con menú
└── README.md
```

---

#  Clases implementadas

### Clase `Pelicula`

Representa una película dentro del catálogo.

Atributos:

* `nombre`
* `duracion`
* `genero`

Características:

* Encapsulamiento mediante atributo privado
* Validación de datos
* Método mágico `__str__` para representación en texto

---

###  Clase `CatalogoPelicula`

Gestiona el catálogo de películas almacenado en archivos `.txt`.

Atributos:

* `nombre`
* `ruta_archivo`

Métodos principales:

* `agregar()`
* `listar()`
* `eliminar_catalogo()`
* `crear_respaldo()`
* `restaurar_respaldo()`
* `listar_catalogos()`

---

#  Ejemplo de menú

```
===== MENÚ =====

1. Agregar Película
2. Listar Películas
3. Eliminar Catálogo
4. Cambiar de Catálogo
5. Listar Catálogos
6. Restaurar desde respaldo
0. Salir
```

---

#  Requerimientos del proyecto (ADA ITW)

Según la consigna del proyecto final:

* Implementar **Programación Orientada a Objetos**
* Crear la **clase Pelicula**
* Crear la **clase CatalogoPelicula**
* Utilizar **archivos `.txt` para almacenar los datos**
* Implementar las operaciones:

  * Agregar película
  * Listar películas
  * Eliminar catálogo
* Subir el proyecto a **GitHub**
* Realizar **al menos 3 commits**

---

# Tecnologías utilizadas

* Python 3
* Programación Orientada a Objetos
* Manejo de archivos (`os`, `shutil`)
* Git y GitHub

---

#  Autor

**Florencia Salinas**

Proyecto final realizado para el curso **Introducción a Python – ADA ITW**.
