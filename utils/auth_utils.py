from flask import redirect, url_for, session, flash
from functools import wraps

def login_required(view_function):
    @wraps(view_function)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login'))
        return view_function(*args, **kwargs)
    return wrapper