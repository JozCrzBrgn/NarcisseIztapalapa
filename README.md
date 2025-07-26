# NarcisseIztapalapa

Python Version: 3.10

Crear una carpeta .streamlit 

En .streamlit/secrets.toml crear las variables de entorno:

#? Database
SUPABASE_URL
SUPABASE_KEY
BUCKET_GENERAL
TAB_INVENTARIO
# Credenciales y permisos
API_CREAR_CREDENCIALES
CREDENCIALES_FILE_INPUT
CREDENCIALES_FILE_OUTPUT
COOKIE_NAME
COOKIE_KEY
COOKIE_EXPIRY_DAYS
NOMBRE_SUCURSAL

En .streamlit/credenciales_input.json escribe las credenciales necesarias y ejecuta el "make cred"