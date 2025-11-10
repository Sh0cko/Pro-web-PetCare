import re
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse


class LoginRequiredMiddleware:
    """
    Obliga a que todas las rutas requieran autenticación, excepto las exentas.
    Exenciones configurables en settings.LOGIN_EXEMPT_URLS (regex relativas, sin '/').
    Siempre exime STATIC_URL y MEDIA_URL.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        # Compilar patrones exentos definidos en settings
        exempt = getattr(settings, 'LOGIN_EXEMPT_URLS', [])
        self.exempt_urls = [re.compile(expr) for expr in exempt]

    def __call__(self, request):
        path = request.path_info.lstrip('/')

        # Permitir estáticos y media
        static_url = (settings.STATIC_URL or '').lstrip('/')
        media_url = (getattr(settings, 'MEDIA_URL', '') or '').lstrip('/')
        if static_url and path.startswith(static_url):
            return self.get_response(request)
        if media_url and path.startswith(media_url):
            return self.get_response(request)

        # Permitir rutas exentas
        for pattern in self.exempt_urls:
            if pattern.match(path):
                return self.get_response(request)

        # Si está autenticado, seguir
        if request.user.is_authenticated:
            return self.get_response(request)

        # Redirigir a login con next
        login_target = settings.LOGIN_URL
        if not str(login_target).startswith('/'):
            try:
                login_target = reverse(login_target)
            except Exception:
                login_target = '/login/'
        return redirect(f"{login_target}?next=/{path}")
