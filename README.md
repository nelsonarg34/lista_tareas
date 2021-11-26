# Lista de Tareas

## Configuración inicial

Este proyecto incluye migraciones predeterminadas, también incluye una base de datos SQLITE con datos de ejemplo.

1.- Clonar este repositorio:

    git clone https://github.com/nelsonarg34/lista_tareas.git 

2.- Crear un entorno virtual:

    virtualenv venv

3.- Active el entorno virtual.

4.- Instalar librerias.

    (venv) pip install -r requirements.txt 

5.- Correr servidor:

    venv) python manage.py runserver 



## Autenticación y registro de usuarios

### Características
    * Registrar una cuenta
    * Iniciar y cerrar sesión
    * Restaurar contraseña

###     End points

http://localhost:8000/api/user/auth/login/

http://localhost:8000/api/user/auth/logout/

http://localhost:8000/api/user/auth/signup/

http://localhost:8000/api/user/auth/reset/

http://localhost:8000/api/user/profile/



## Listas de tareas de usuarios

Interacción entre los usuarios y listas de tareas

###     End points

Listas (GET, POST): http://127.0.0.1:8000/api/lists/

Listas (GET, PUT, PATCH, DELETE): http://127.0.0.1:8000/api/lists/1/

Tareas (GET, POST): http://127.0.0.1:8000/api/tasks/

Tareas (GET, PUT, PATCH, DELETE): http://127.0.0.1:8000/api/tasks/1/



## Búsquedas y filtros

- Búsqueda: Usando un texto y buscando coincidencias.
- Ordenación: Ascendente o descendente a partir de varios campos.
- Filtrado: En base a a partir de varios campos.

###     End points

http://127.0.0.1:8000/api/list_filters/
