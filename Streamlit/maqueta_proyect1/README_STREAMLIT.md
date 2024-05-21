# Aplicación de Streamlit

## Descripción del Proyecto

Esta aplicación de Streamlit está estructurada de la siguiente manera:

1. **Archivo `requirements.txt`**: Contiene todas las dependencias y paquetes necesarios para ejecutar la aplicación.
2. **Archivo `app.py`**: Es el archivo principal que corre la aplicación y la página principal.
3. **Archivo `utils.py`**: Aquí se encuentran todas las funciones necesarias para que nuestra aplicación funcione correctamente.
4. **Carpeta `imagenes`**: Contiene todas las imágenes utilizadas en el fondo de la aplicación.
5. **Carpeta `pages`**: Contiene la segunda página de la aplicación, donde se encuentra nuestro modelo de predicción. En esta página se llaman a nuestras funciones y a nuestra API para generar las predicciones.
6. **Carpeta comprimida `modelo_vectorizador.zip`**: Contiene el modelo de predicción y el vectorizador utilizados en la aplicación.

## Funcionalidades

- **Página Principal**: Interfaz inicial de la aplicación donde puedes navegar a diferentes secciones.
- **Página de Predicción**: Sección donde se encuentra nuestro modelo de predicción. Aquí se llaman a las funciones definidas en `utils.py` y se utiliza la API para generar predicciones.

## Nota Importante

Debido a que los modelos son muy pesados, no se cargan directamente en este repositorio. Si necesitas acceso a los modelos, por favor contacta a los siguientes miembros del equipo:

- David González (Dgasensi)
- Celia García (Celia-code13)
- Joel de Andrade (Joel1695)

## Estructura del Proyecto


```plaintext


/mi_proyecto_streamlit
│
├── app.py                        # Archivo principal de la aplicación
├── requirements.txt              # Dependencias necesarias
├── utils.py                      # Funciones de utilidad
│
├── /imagenes                     # Carpeta con las imágenes de fondo
│   └── fondo.png                 # Ejemplo de imagen de fondo
│
├── /pages                        # Carpeta con las páginas adicionales de la aplicación
│   └── prediccion.py             # Página con el modelo de predicción
│
└── modelo_vectorizador.zip       # Carpeta comprimida con el modelo y el vectorizador
