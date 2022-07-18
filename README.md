proyecto_Komclima

# Instalación

Para ejecución en desarrollo se recomienda utilizar el módulo "virtualenv" de Python.

El siguiente comando permite instalar los módulos necesarios para que funcione el proyecto.

```python
pip install -r requirements.txt
```

# RUTAS

| Método | Ruta | Descripción | Autenticación | Rol requerido |
| --- | --- | --- | --- | --- |
| GET | / | Redirige a la vista principal de la aplicación. | False | --- |
| GET | /register | Redirige a una vista de registro de usuarios. | True | Admin |
| POST | /register | Valida los datos del formulario verificando que el correo y el rut no existan en la base de datos. | True | Admin |
| GET | /login | Redirige a la vista con el formulario de autenticación. | False | --- |
| POST | /login | Permite autenticar al usuario. | False | --- |
| GET | /dashboard | Dashboard para el usuario autenticado. | True | --- |