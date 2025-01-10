## **Comandos utilizados al trabajar con Markdown, MyST-Parser, Sphinx**

### Crear un entorno virtual
```
python -m venv venv
```

### Activar el entorno virtual
```
env\Scripts\activate
```

### Configuración inicial del proyecto Sphinx

#### Comando para iniciar un proyecto Sphinx

```
sphinx-quickstart
``` 

-   Este comando inicializa un proyecto Sphinx, creando la estructura básica con carpetas como `docs`, `source`, y archivos como `conf.py`, `index.rst`, etc.

----------

#### Comando para actualizar la versión de Sphinx
```
pip install -U sphinx
``` 
1.  **`pip install`**: Instala un paquete de Python (en este caso, `sphinx`) desde el repositorio de PyPI (Python Package Index).
2.  **`-U` o `--upgrade`**: Actualiza el paquete a la versión más reciente disponible en PyPI.

### Instalación de dependencias necesarias

#### Instalar Sphinx

```
pip install sphinx
```

#### Instalar MyST-Parser

```
pip install myst-parser
```

-   Habilita el soporte para archivos Markdown en Sphinx.

#### Instalar un tema

```
pip install sphinx_rtd_theme
```

-   Instala el tema utilizado en la documentación.

----------

### Generación de documentación

#### Para documentación automáticamente desde código

```
sphinx-apidoc -o ./docs/source ../src --separate --suffix .md
``` 

- Crea automáticamente archivos de documentación desde el código fuente, (La opción --separate genera archivos independientes por cada módulo).


#### Para generar documentación en formato HTML

```
make html
``` 

-   Genera la documentación en HTML. El resultado se encuentra en la carpeta `docs/build/html`.

#### Para limpiar los archivos generados

```
make clean
``` 

-   Elimina todos los archivos generados previamente (HTML, PDF, etc.).

----------
#### Actualizar dependencias

```
pip install --upgrade sphinx myst-parser
``` 
----------

#### Generar HTML

``` 
start .\build\html\index.html
``` 

- Esto crea la salida HTML en `docs/build/html`. Se abre `index.html` en el navegador para ver el resultado.

#### Generar PDF

``` 
make.bat latex
``` 
- Genera los archivos fuente de LaTeX a partir de la documentación escrita en Sphinx.

``` 
pdflatex documento.tex
``` 
- Compila el archivo .tex generado por LaTeX para producir un archivo PDF final.