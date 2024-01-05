# Portafolio Personal y Redes Sociales

Este proyecto consiste en una página web estática que funciona mi portafolio personal, mostrando información sobre mi perfil profesional y enlaces a mis redes sociales. La página está construida utilizando Reflex.dev y Python.

## Contenido

1. [Instalación](#instalación)
2. [Estructura del Proyecto](#estructura-del-proyecto)
3. [Uso](#uso)
4. [Personalización](#personalización)
5. [Tecnologías Utilizadas](#tecnologías-utilizadas)
6. [Licencia](#licencia)

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/yharyarias/personal_web_site_reflex.git
    ```

2. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

3. Ejecuta la aplicación:

    ```bash
    reflex run
    ```

La aplicación estará disponible en [http://localhost:3000](http://localhost:3000).

## Estructura del Proyecto

- `static/`: Contiene los archivos estáticos como imágenes, estilos CSS, etc.
- `templates/`: Contiene las plantillas HTML para la página.
- `personal_web_site_reflex.py`: Archivo principal de la aplicación Reflex.

## Uso

Abre tu navegador y visita [http://localhost:3000](http://localhost:3000) para ver tu portafolio y enlaces a tus redes sociales.

## Personalización

1. Modifica los archivos en la carpeta `static/` para agregar tus imágenes y estilos personalizados.
2. Edita los archivos en la carpeta `templates/` para personalizar el contenido de tu página.

## Tecnologías Utilizadas

- [Reflex.dev](https://reflex.dev/): Framework para el desarrollo web estático con Python.
- [Python](https://www.python.org/): Utilizado para la lógica del servidor mediante Flask.

## Licencia

Este proyecto está bajo la Licencia [MIT](LICENSE).
