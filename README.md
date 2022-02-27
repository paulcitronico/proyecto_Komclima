proyecto_Komclima

# Instalación

Para ejecución en desarrollo se recomienda utilizar el módulo "virtualenv" de Python.

El siguiente comando permite instalar los módulos necesarios para que funcione el proyecto.

```python
pip install -r requirements.txt
```

# RUTAS

| Método | Ruta | Descripción |
| --- | --- | --- |
| GET | / | Redirige a la vista principal de la aplicación. |
| GET | /register | Redirige a una vista de registro de usuarios. |
| POST | /register | Valida los datos del formulario verificando que el correo y el rut no existan en la base de datos. |