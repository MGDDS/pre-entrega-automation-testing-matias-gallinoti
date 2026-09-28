# Automatización Web con Selenium y Python

## Propósito del proyecto

Este proyecto tiene como objetivo aplicar los conocimientos adquiridos hasta la Clase 8 del curso de **Talento Tech**, desarrollando una automatización básica de navegación y testing web.

La automatización se realiza sobre **SauceDemo**, una aplicación web creada especialmente para prácticas de testing, utilizando **Selenium WebDriver y Python**.

El proyecto permite practicar:

* Navegación e interacción con una página web.
* Localización de elementos mediante diferentes estrategias.
* Interacción con botones, campos y otros elementos.
* Validación de estados y resultados esperados.
* Estructuración de pruebas automatizadas.

## Tecnologías utilizadas

* **Python** – Lenguaje de programación principal.
* **Pytest** – Framework utilizado para estructurar y ejecutar las pruebas.
* **Selenium WebDriver** – Automatización de la navegación e interacción con el sitio web.
* **Git** – Control de versiones del proyecto.
* **GitHub** – Repositorio y gestión del código fuente.
* **SauceDemo** – Sitio web utilizado como entorno de práctica.

## Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>
```

### 2. Crear un entorno virtual

En Windows:

```bash
python -m venv venv
```

Activar el entorno virtual:

```bash
venv\Scripts\activate
```

En Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias

Con el entorno virtual activado, ejecutar:

```bash
pip install -r requirements.txt
```

Las principales dependencias del proyecto son:

```text
selenium
pytest
```

### 4. Ejecutar las pruebas

Para ejecutar todos los tests:

```bash
pytest
```

Para obtener una salida más detallada:

```bash
pytest -v
```

## Sitio utilizado

Las pruebas automatizadas se ejecutan sobre:

**https://www.saucedemo.com/**

## Estructura del proyecto

Una estructura posible para el proyecto es:

```text
proyecto-selenium/
│
├── tests/
│   └── test_saucedemo.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Objetivo de la pre-entrega

El proyecto busca demostrar el uso básico de **Selenium WebDriver con Python y Pytest**, aplicando estrategias de localización de elementos, interacción con la interfaz y validación de resultados mediante pruebas automatizadas.
