# Verificar si el archivo .streamlit/secrets.toml existe
ifeq (,$(wildcard .streamlit/secrets.toml))
$(error El archivo secrets.toml NO existe.)
endif

# Carga variables desde .streamlit/secrets.toml
include .streamlit/secrets.toml
export

run: #? Ejecuta el programa
	streamlit run streamlit_app.py

cred: #? Crea las credenciales
	@curl -X POST \
	$(API_CREAR_CREDENCIALES) \
	-H 'accept: application/json' \
	-H 'Content-Type: application/json' \
	-d @$(CREDENCIALES_FILE_INPUT) \
	-o $(CREDENCIALES_FILE_OUTPUT)
