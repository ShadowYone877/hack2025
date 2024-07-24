  

from functools import wraps

from flask import abort

from flask_login import current_user


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        is_admin = getattr(current_user, 'is_admin', False)
        if not is_admin:
            abort(401)
        return f(*args, **kws)
    return decorated_function

def gestorDBA_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        is_gestorDBA = getattr(current_user, 'rol_id', 1)
        if is_gestorDBA not in [1,5]:
            abort(401)
        return f(*args, **kws)
    return decorated_function
