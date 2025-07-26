# 📌 NarcisseIztapalapa

Nombre autoexplicativo del proyecto, con una breve descripción clara y directa de lo que hace.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-95%25-blue)

---

## 🧠 Descripción

Una descripción más detallada y técnica del proyecto, incluyendo sus principales características, su propósito y cómo funciona.

---

## 🖼️ Visuales

| Vista principal       | Función destacada           |
| --------------------- | --------------------------- |
| ![main](img/main.png) | ![feature](img/feature.gif) |

---

## 🚀 Empezando

Estas instrucciones te guiarán para obtener una copia de este proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

### 📋 Prerrequisitos

- Sistema Operativo: **Windows 10**
- Lenguaje de programación: **Python 3.10+**
- Framework: **Streamlit**
- Base de datos: **Supabase**

### 🔧 Instalación

```bash
# Paso 1: Clonar el repositorio por SSH
git clone git@gjoz:JozCrzBrgn/NarcisseIztapalapa.git

# Paso 2: Crear entorno virtual
python -m venv .venv
source .venv\Scripts\activate

# Paso 3: Instalar dependencias
pip install -r requirements.txt

# Paso 4: Configurar variables de entorno en .streamlit/secrets.toml
SUPABASE_URL
SUPABASE_KEY
BUCKET_GENERAL
TAB_INVENTARIO
API_CREAR_CREDENCIALES
CREDENCIALES_FILE_INPUT
CREDENCIALES_FILE_OUTPUT
COOKIE_NAME
COOKIE_KEY
COOKIE_EXPIRY_DAYS
NOMBRE_SUCURSAL

# Paso 5: Configurar las credenciales (si no se tienen) en .streamlit/credenciales_input.json

{
  "names": [
    "Name1 Ap1",
    "Name2 Ap2",
    "Name3 Ap3",
    "Name4 Ap4"
  ],
  "usernames": [
    "name1",
    "name2",
    "name3",
    "name4"
  ],
  "passwords": [
    "pass1",
    "pass2",
    "pass3",
    "pass4"
  ]
}

# Paso 6: Crear las credenciales encriptadas (si no se tienen)
make cred

# Paso 7: Guardar las credenciales creadas (si no se han guardado) en
Supabase > Storage > monitoreo_streamlit

# Paso 8: Ejecutar la aplicación
make run
```

---

## 🧪 Ejecutando las Pruebas

```bash
# Ejecutar todas las pruebas
pytest
```

### 🔄 Pruebas de Principio a Fin

Estas pruebas cubren flujos completos de usuario como autenticación, creación de entidades, etc.

### ⌨️ Pruebas de Estilo de Código

```bash
flake8 .
black --check .
```

---

## 📦 Despliegue

Para desplegar este proyecto en un entorno de producción:

- Crear contenedor Docker (opcional)
- Configurar servidor (Heroku, Railway, VPS)
- Ejecutar migraciones y cargar datos iniciales
- Configurar variables de entorno en producción

---

## 🛠️ Construido Con

- [Python](https://www.python.org/) - Lenguaje de programación
- [Django](https://www.djangoproject.com/) - Framework web
- [PostgreSQL](https://www.postgresql.org/) - Sistema de base de datos
- [Docker](https://www.docker.com/) - Contenedores para despliegue

---

## 🛣️ Roadmap

- [ ] Agregar autenticación por redes sociales
- [ ] Mejorar rendimiento con caching
- [ ] Agregar interfaz de usuario responsiva
- [ ] Panel de administración avanzado

---

## 🖇️ Contribuyendo

Las contribuciones son lo que hacen a la comunidad de código abierto un lugar increíble para aprender, inspirar y crear. ¡Cualquier aporte es bienvenido!


---

## 📖 Wiki

Puedes encontrar más documentación y guías en nuestra [Wiki](https://github.com/your/project/wiki)

---

## 🛟 Soporte

Si tienes algún problema o sugerencia, por favor abre un issue [aquí](https://github.com/your/project/issues).

---

## 📌 Versionado

Usamos [Git](https://git-scm.com) para el control de versiones y seguimos [Semantic Versioning](https://semver.org/).

Consulta las [etiquetas del repositorio](https://github.com/your/project/tags) para versiones disponibles.

---

## ✒️ Autor

[Josue Emmanuel Cruz Barragan](https://github.com/JozCrzBrgn)

---

## 📄 Licencia

Este proyecto está bajo la Licencia [Apache License Version 2.0](LICENSE.md).

---

## 🎁 Agradecimientos

Estamos agradecidos por las contribuciones de la comunidad a este proyecto. Si encontraste valor en este trabajo, puedes:

- Compartir el proyecto 📤
- Invitarnos un café ☕
- Iniciar un issue o PR 🙌
- Dejar tu agradecimiento con un comentario 💬

---

⌨️ con ❤️ por [Brayan Diaz C](https://github.com/brayandiazc) 😊




En .streamlit/credenciales_input.json escribe las credenciales necesarias y ejecuta el "make cred"