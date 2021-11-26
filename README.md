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
    -Registrar una cuenta
    -Iniciar y cerrar sesión
    -Restaurar contraseña

### End points

http://localhost:8000/api/user/auth/login/
http://localhost:8000/api/user/auth/logout/
http://localhost:8000/api/user/auth/signup/
http://localhost:8000/api/user/auth/reset/
http://localhost:8000/api/user/profile/