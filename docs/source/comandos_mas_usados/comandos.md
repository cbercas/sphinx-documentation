## Comandos utilizados al trabajar con Markdown, MyST-Parser, Sphinx

### **1. Crear un entorno virtual**
```
python -m venv venv
```

### **2. Activar el entorno virtual**
```
venv\Scripts\activate
```

### **3. Configuración inicial del proyecto Sphinx**

#### **Comando para iniciar un proyecto Sphinx**

```
sphinx-quickstart
``` 

-   Este comando inicializa un proyecto Sphinx, creando la estructura básica con carpetas como `docs`, `source`, y archivos como `conf.py`, `index.rst`, etc.

----------

#### **Comando para actualizar la versión de Sphinx**
```
pip install -U sphinx
``` 
1.  **`pip install`**: Instala un paquete de Python (en este caso, `sphinx`) desde el repositorio de PyPI (Python Package Index).
2.  **`-U` o `--upgrade`**: Actualiza el paquete a la versión más reciente disponible en PyPI.

### **4. Instalación de dependencias necesarias**

#### **Instalar Sphinx**

```
pip install sphinx
```

#### **Instalar MyST-Parser**

```
pip install myst-parser
```

-   Habilita el soporte para archivos Markdown en Sphinx.

#### **Instalar un tema**

```
pip install sphinx_rtd_theme
```

-   Instala el tema utilizado en la documentación.

----------

### **4. Generación de documentación**

#### **Para generar documentación en formato HTML**

```
make html
``` 

-   Genera la documentación en HTML. El resultado se encuentra en la carpeta `docs/build/html`.

#### **Para limpiar los archivos generados**

```
make clean
``` 

-   Elimina todos los archivos generados previamente (HTML, PDF, etc.).

----------
#### **Actualizar dependencias**

```
pip install --upgrade sphinx myst-parser
``` 
----------

