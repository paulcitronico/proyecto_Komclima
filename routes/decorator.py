from functools import wraps
from flask_login import current_user
from flask import redirect, url_for

"""
Este modelo crea decoradores utilizados para proteger las vistas
de determinados roles de usuario.
"""

def admin_required(f):
    wraps(f)
    def decorated_function(*args, **kws):
        is_admin = getattr(current_user,"Type","admin")
        if not is_admin:
            return redirect(url_for("app.unauthorized"))
        return f(*args,**kws)
    return decorated_function

def superadmin_required(f):
    wraps(f)
    def decorated_function(*args, **kws):
        is_superadmin = getattr(current_user,"Type","Superadmin")
        if not is_superadmin:
            return redirect(url_for("app.unauthorized"))
        return f(*args,**kws)
    return decorated_function

def user_required(f):
    wraps(f)
    def decorated_function(*args, **kws):
        is_user = getattr(current_user,"Type","User")
        if not is_user:
            return redirect(url_for("app.unauthorized"))
        return f(*args,**kws)
    return decorated_function