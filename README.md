Optional-Project: Cryptography Machine
Descripción
Este proyecto implementa una máquina de cifrados clásicos en Python. Incluye algoritmos de cifrado y descifrado de varios métodos históricos y educativos de criptografía, con una interfaz de menú interactiva para usarlos fácilmente desde consola. Está orientado a la experimentación y estudio de técnicas criptográficas.

Características principales
Implementación de varios cifrados clásicos:

Cifrado César (Caesar cipher)

ROT13

Vigenère

Autokey

Beaufort

Playfair

Two-Square

Four-Square

Rail Fence

Interfaz de usuario en consola con menú para seleccionar método, ingresar texto y parámetros, y realizar cifrado o descifrado.

Código modular y legible con funciones independientes para cada cifrado.

Pruebas unitarias básicas para validar la correcta funcionalidad de los algoritmos implementados.

Soporte para manejo de mayúsculas y caracteres permitidos, preservando espacios y otros símbolos sin cambios.

Instalación
Clonar el repositorio y ejecutar el script principal con Python 3.x:

bash
git clone https://github.com/Bania1/Optional-Project.git
cd Optional-Project
python crytography_machine.py
No hay dependencias externas, solo utiliza la librería estándar de Python.

Uso
Al ejecutar el programa, se muestra un menú numérico para seleccionar el cifrado deseado. Luego se solicitan los textos, claves, desplazamientos o parámetros necesarios. El usuario puede elegir entre cifrar o descifrar según el método elegido.

Por ejemplo, para el cifrado César se pide un texto y un valor de desplazamiento; para Vigenère y otros, se solicita además la clave.

El programa sigue ejecutándose hasta que se elige la opción de salir.

Estructura del código
Clases y funciones independientes para cada cifra.

Función menu() para mostrar las opciones.

Función main() con bucle para interactuar con el usuario.

Tests unitarios usando la librería unittest para algunos métodos.

Estado actual y mejoras futuras
Actualmente algunas pruebas unitarias están comentadas, y se pueden extender para cubrir más casos. También se puede mejorar la gestión de entradas con validaciones más robustas y añadir interfaces gráficas o soporte para más alfabetos/caracteres.

Autor
Proyecto desarrollado para fines educativos y de práctica en criptografía clásica con Python.
