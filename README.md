proyecto_Komclima

# Instalación

El siguiente comando permite instalar los módulos necesarios para que funcione el proyecto.

```python
pip install -r requirements.txt
```

# RUTAS

Blueprint: root (ruta raíz)

| Método | Ruta | Descripción |
| --- | --- | --- |
| GET | / | Redirige a la vista principal. |
| GET | /recoverPassword | Redirige a la vista para recuperar contraseña. | 

Blueprint: users

| Método | Ruta | Descripción |
| --- | --- | --- |
| POST | /users/register | Registra un nuevo usuario, obtiene la información a partir de un form-data (datos de formularios) |