from functools import wraps
from flask_login import current_user
from flask import abort

"""
Este modelo crea decoradores utilizados para proteger las vistas
de determinados roles de usuario.
"""

def admin_required(f):
    wraps(f)
    def decorated_function(*args, **kws):
        is_admin = getattr(current_user,"Type","admin")
        print(is_admin)
        if is_admin == "User" or is_admin == "Superadmin":
            return abort(403)
        return f(*args,**kws)
    return decorated_function

def superadmin_required(f):
    wraps(f)
    def decorated_function(*args, **kws):
        is_superadmin = getattr(current_user,"Type","Superadmin")
        if is_superadmin == "User" or is_superadmin == "admin":
            return abort(403)
        return f(*args,**kws)
    return decorated_function

def user_required(f):
    wraps(f)
    def decorated_function(*args, **kws):
        is_user = getattr(current_user,"Type","User")
        if is_user == "admin" or is_user == "Superadmin":
            return abort(403)
        return f(*args,**kws)
    return decorated_function