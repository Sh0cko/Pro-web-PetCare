from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from functools import wraps

def admin_required(view_func):
    """Solo para superusuarios"""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.is_superuser:
            from django.contrib import messages
            messages.error(request, 'No tienes permisos de administrador para acceder a esta página.')
            return redirect('index')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def staff_required(view_func):
    """Para staff y administradores"""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.is_staff and not request.user.is_superuser:
            from django.contrib import messages
            messages.error(request, 'No tienes permisos para acceder a esta página.')
            return redirect('index')
        return view_func(request, *args, **kwargs)
    return _wrapped_view